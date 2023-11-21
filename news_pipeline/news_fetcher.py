import os
import sys
from newspaper import Article

# from bs4 import BeautifulSoup
# import subprocess

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = 'amqps://eviywzfr:Eu1cq8176zK4dfANwzaQVp57XIakXaT_@fish.rmq.cloudamqp.com/eviywzfr'
DEDUPE_NEWS_TASK_QUEUE_NAME = 'tap-news-dedupe-news-task-queue'
SCRAPE_NEWS_TASK_QUEUE_URL = 'amqps://ahkufdzq:AVcDKu5oRlZd0bohjcB2wnIAiiR_E_XY@fish.rmq.cloudamqp.com/ahkufdzq'
SCRAPE_NEWS_TASK_QUEUE_NAME = 'tap-news-scrape-news-task-queue'

SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
	if msg is None or not isinstance(msg, dict):
		print ('message is broken')
		return

	task = msg
	article = Article(task['url'])
	article.download()
	article.parse()

	task['text'] = article.text

	dedupe_news_queue_client.sendMessage(task)

while True:
	# fetch msg from queue
	if scrape_news_queue_client:
		msg = scrape_news_queue_client.getMessage()
		if msg:
			try:
				handle_message(msg)
			except Exception as e:
				print (e)
				pass
		scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
