import os
import sys
from newspaper import Article

# from bs4 import BeautifulSoup
# import subprocess

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))

from news_pipeline_config import *
import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

# SLEEP_TIME_IN_SECONDS = 5

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
