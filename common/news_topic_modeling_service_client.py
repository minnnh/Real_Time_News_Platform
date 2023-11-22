import jsonrpclib
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from common_config import *

# TOPIC_URL = "http://localhost:6060/"

client = jsonrpclib.ServerProxy(TOPIC_URL)

def classify(text):
    topic = client.classify(text)
    print("Topic: %s" % str(topic))
    return topic
