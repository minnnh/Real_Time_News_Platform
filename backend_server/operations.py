import json
import os
import pickle
import random
import redis
import sys

from bson.json_util import dumps
from datetime import datetime

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))

from backend_server_config import *

import mongodb_client 
import news_recommendation_service_client

from cloudAMQP_client import CloudAMQPClient 

# REDIS_HOST = "localhost"
# REDIS_PORT = 6379

# NEWS_TABLE_NAME = "news-test"
# CLICK_LOGS_TABLE_NAME = 'click_logs'

# NEWS_LIST_BATCH_SIZE = 10
# NEWS_LIMIT = 200
# USER_NEWS_TIME_OUT_IN_SECONDS = 60

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)
cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def getOneNews():
    """Get one news"""
    db = mongodb_client.get_db()
    news = db[NEWS_TABLE_NAME].find_one()
    # if news is None:
    #     return [
    #     {'id':"testing",
    #     'name':"aa",
    #     'digest':"happy",
    #     'source':"chinese"
    #     }]
    return json.loads(dumps(news))

def getNewsSummariesForUser(user_id, page_num):
    page_num = int(page_num)
    begin_index = (page_num - 1) * NEWS_LIST_BATCH_SIZE
    end_index = page_num * NEWS_LIST_BATCH_SIZE

    # The final list of news to be returned.
    sliced_news = []
    if redis_client.get(user_id) is not None:
        # print("in redis")
        news_digests = pickle.loads(redis_client.get(user_id))

        # If begin_index is out of range, this will return empty list;
        # If end_index is out of range (begin_index is within the range), this
        # will return all remaining news ids.
        sliced_news_digests = news_digests[begin_index:end_index]
        db = mongodb_client.get_db()
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest':{'$in':sliced_news_digests}}))
    else:
        # print("in mongodb")
        db = mongodb_client.get_db()

        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT))
        total_news_digests = [x['digest'] for x in total_news]

        redis_client.set(user_id, pickle.dumps(total_news_digests))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SECONDS)

        sliced_news = total_news[begin_index:end_index]

    # Get preference for the user
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        # Remove text field to save bandwidth.
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
            
        news['published_date'] = news['publishedAt'].strftime('%Y-%m-%d')
        
    return json.loads(dumps(sliced_news))


def logNewsClickForUser(user_id, news_id):
    # Send log task to machine learning service for prediction
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    cloudAMQP_client.sendMessage(message)
