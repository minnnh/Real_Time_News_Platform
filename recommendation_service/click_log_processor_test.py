import click_log_processor
import os
import sys

from datetime import datetime
# from sets import Set

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))

from recommendation_service_config import *
import mongodb_client

# PREFERENCE_MODEL_TABLE_NAME = "user_preference_model"
# NEWS_TABLE_NAME = "news-test"

# NUM_OF_CLASSES = 17

# Start MongoDB before running following tests.
def test_basic():
    db = mongodb_client.get_db()
    db[PREFERENCE_MODEL_TABLE_NAME].delete_many({"userId": "test_user"})

    msg = {"userId": "test_user",
           "newsId": '11ddbf495275e52bb63ef554d4f48f0d',
           "timestamp": str(datetime.utcnow())}

    click_log_processor.handle_message(msg)

    model = db[PREFERENCE_MODEL_TABLE_NAME].find_one({'userId':'test_user'})
    assert model is not None
    assert len(model['preference']) == NUM_OF_CLASSES

    print ('test_basic passed!')


if __name__ == "__main__":
    test_basic()