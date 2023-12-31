# -*- coding: utf-8 -*-

import os
import sys
import redis
import hashlib
import datetime
from json import dumps

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))

from news_pipeline_config import *
import news_api_client
from cloudAMQP_client import CloudAMQPClient

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

import json
with open('./test/monitor_test_data.json', 'r') as json_file:
	test_data = json.load(json_file)

while True:
	# news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)
	news_list = test_data

	num_of_new_news = 0
	for news in news_list:
		# news_digest = hashlib.md5(news['title'].encode('utf-8')).digest().encode('base64')
		# news_digest = hashlib.md5(news['title'].encode('utf-8')).hexdigest()
		title = news.get('title', '')
		news_digest = hashlib.md5(title.encode('utf-8')).hexdigest()

		if redis_client.get(news_digest) is None:
			num_of_new_news += 1
			news['digest'] = news_digest

			if news['publishedAt'] is None:
				news['publishedAt'] = datetime.datetime.utcnow().strftime("%Y-%m-%%dT%H:%M:%SZ")

			# convert into string
			# news = dumps(news)
			#redis_client.hmset(news_digest, news)
			redis_client.set(news_digest, dumps(news))
			redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)

			cloudAMQP_client.sendMessage(news)

	print("Fetched %d news." % num_of_new_news)

	cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)
	break
