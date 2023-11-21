import requests
from json import loads

NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
NEWS_API_KEY = '29e05503b1704fd3872d835d7627a065'
ARTICLES_API = 'articles'

CNN = 'cnn'
DEFAULT_SOURCES = [CNN]

SORT_BY_TOP = 'top'

def buildUrl(end_point = NEWS_API_ENDPOINT, api_name = ARTICLES_API):
	return end_point + api_name

def getNewsFromSource(sources=[DEFAULT_SOURCES], sortBy=SORT_BY_TOP):
	articles = []
	for source in sources:
		payload = {'apiKey' : NEWS_API_KEY,
					'source' : source,
					'sortBy' : sortBy}
		response = requests.get(buildUrl(), params = payload)
		res_json = loads(response.content)
		# Extract info from response
		if (res_json and
			res_json['status'] == 'ok' and
			res_json['source']):
			
			# populate news source in each articles
			for news in res_json['articles']:
				news['source'] = res_json['source']

			articles.extend(res_json['articles'])

	return articles



# import requests
# from json import loads

# NEWS_API_ENDPOINT = 'https://newsapi.org/v2/'
# NEWS_API_KEY = '29e05503b1704fd3872d835d7627a065'
# ARTICLES_API = 'top-headlines?country=us'

# CNN = 'cnn'
# DEFAULT_SOURCES = [CNN]

# SORT_BY_TOP = 'popularity'

# def buildUrl(end_point = NEWS_API_ENDPOINT, api_name = ARTICLES_API):
# 	return end_point + api_name

# def getNewsFromSource(sources=[DEFAULT_SOURCES], sortBy=SORT_BY_TOP):
# 	articles = []
# 	print("========test 1=========")
# 	for source in sources:
# 		payload = {'apiKey' : NEWS_API_KEY,
# 					'source' : source,
# 					'sortBy' : sortBy}
# 		response = requests.get(buildUrl(), params = payload)
# 		res_json = loads(response.content)
# 		# Extract info from response
# 		if (res_json and
# 			res_json['status'] == 'ok' and
# 			res_json['source']):
			
# 			# populate news source in each articles
# 			for news in res_json['articles']:
# 				news['source'] = res_json['source']

# 			articles.extend(res_json['articles'])

# 	return articles