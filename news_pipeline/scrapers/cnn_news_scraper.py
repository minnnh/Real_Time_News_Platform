import os
import random
import requests
from bs4 import BeautifulSoup
#from lxml import html


# load user agents
USER_AGENTS_FILE = os.path.join(os.path.dirname(__file__), 'user_agents.txt')
USER_AGENTS = []

# GET_CNN_NEWS_XPATH = """//p[contains(@class, 'zn-body__paragraph')]//text() | //div[contains(@class, 'zn-body__paragraph')]//text()"""
GET_CNN_NEWS_XPATH = """//p[contains(@class, 'paragraph inline-placeholder')]//text() | //h2//text()"""
GET_CNN_NEWS_FORMAT = 'p'
GET_CNN_NEWS_CLASS = 'paragraph inline-placeholder'

with open(USER_AGENTS_FILE, 'r') as uaf:
	for ua in uaf.readlines():
		if ua:
			USER_AGENTS.append(ua.strip()[1:-1])
random.shuffle(USER_AGENTS)

def getHeader():
	ua = random.choice(USER_AGENTS)
	headers = {
				"Connection" : "close",
				"User-Agent" : ua
				}

	return headers

def extract_news(news_url):
	# fetch html	
	session_requests = requests.session()
	response = session_requests.get(news_url, headers=getHeader())

	news = {}

	try:
		# parse html
		# tree = html.fromstring(response.content)

		tree = BeautifulSoup(response.content, "html.parser")

		# rextract infomation
		paragraphs = tree.find_all(GET_CNN_NEWS_FORMAT, class_=GET_CNN_NEWS_CLASS)

		news = ""
		news += ''.join([paragraph.get_text() for paragraph in paragraphs])

		# news = tree.xpath(GET_CNN_NEWS_XPATH)
		# news = ''.join(news)
		
	except Exception as e:
		print (e)
		return {}

	return news
