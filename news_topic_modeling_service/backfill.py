import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_topic_modeling_service_client

if __name__ == '__main__':
    db = mongodb_client.get_db()
    cursor = db["news-test"].find({})
    count = 0
    for news in cursor:
        count += 1
        print (count)
        if 'class' in news:
            print ('Populating classes...')
            title = news['title']
            text = news['text']
            data = title + text
            topic = news_topic_modeling_service_client.classify(data)
            news['class'] = topic
            db['news'].replace_one({'digest': news['digest']}, news, upsert=True)