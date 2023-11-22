import datetime
import os
import sys

from dateutil import parser
from sklearn.feature_extraction.text import TfidfVectorizer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))

from news_pipeline_config import *
import mongodb_client
import news_topic_modeling_service_client

from cloudAMQP_client import CloudAMQPClient 

# SLEEP_TIME_IN_SECONDS = 1

# NEWS_TABLE_NAME = "news-test"

# SAME_NEWS_SIMILARITY_THRESHOLD = 0.8
cloudAMQP_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)


def handle_message(msg):
	if msg is None or not isinstance(msg, dict):
		print ('message is broken')
		return

	task = msg
	text = str(task['text'].encode('utf-8'))
	if text is None:
		return

	# get all recent news
	published_at = parser.parse(task['publishedAt'])
	published_at_day_begin = datetime.datetime(published_at.year, published_at.month, published_at.day-3, 0,0,0,0)
	published_at_day_end = published_at_day_begin + datetime.timedelta(days=4)

	db = mongodb_client.get_db()
	recent_news_list = list(db[NEWS_TABLE_NAME].find({'publishedAt':{'$gte':published_at_day_begin, '$lt':published_at_day_end}}))

	if recent_news_list and len(recent_news_list) > 0:
		documents = [str(news['text'].encode('utf-8')) for news in recent_news_list]
		documents.insert(0, text)

		# calculate similarity matrix
		tfidf = TfidfVectorizer().fit_transform(documents)
		pairwise_sim = tfidf * tfidf.T

		print (pairwise_sim.A)
		rows, _ = pairwise_sim.shape

		for row in range(1, rows):
			if pairwise_sim[row, 0] > SAME_NEWS_SIMILARITY_THRESHOLD:
				# Duplicate news, Ignore'
				print ('Duplicate news, Ignore')
				# log_client.logger.info('Duplicate news, Ignore')
				return
	task['publishedAt'] = parser.parse(task['publishedAt'])

	#Classify news
	title = task['title']
	if (title):
		topic = news_topic_modeling_service_client.classify(title)
		task['class'] = topic

	db[NEWS_TABLE_NAME].replace_one({'digest': task['digest']}, task, upsert=True)
	print('got message! after insert')

while True:
	if cloudAMQP_client:
		msg = cloudAMQP_client.getMessage()
		if msg:
			try:
				handle_message(msg)
			except Exception as e:
				print (e)
				pass
		cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)
