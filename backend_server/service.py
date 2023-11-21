# import pyjsonrpc
import json
import os
import sys
import operations
#import mongodb_client
from pymongo import MongoClient
from bson.json_util import dumps
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

sys.path.append(os.path.join(os.path.dirname(__file__),'..','common'))

import mongodb_client

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

# test function
def add(a, b):
	print ("add is called with %d and %d" % (a, b))
	return a + b

# test function
def getNews():
	#mongodb_client = MongoClient()
	#db = mongodb_client['test']
	db = mongodb_client.get_db('test')
	news = list(db['demo'].find()).limit(5)
	# return [{'name': "testing getNews", 'ans': "here"}]
	return json.loads(dumps(news))

# test function
def getOneNews():
    """Get one news"""
    print("getOneNews is called")
    return operations.getOneNews()

def getNewsSummariesForUser(user_id, page_num):
    print("getNewsSummariesForUser is called with %s and %s" % (user_id, page_num))
    return operations.getNewsSummariesForUser(user_id, page_num)

def logNewsClickForUser(user_id, news_id):
    print("logNewsClickForUser is called with %s and %s" % (user_id, news_id))
    operations.logNewsClickForUser(user_id, news_id)

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(getNews, 'getNews')
RPC_SERVER.register_function(getOneNews, 'getOneNews')
RPC_SERVER.register_function(getNewsSummariesForUser, 'getNewsSummariesForUser')
RPC_SERVER.register_function(logNewsClickForUser, 'logNewsClickForUser')


print ("start Http server on %s:%d" % (SERVER_HOST, SERVER_PORT))

RPC_SERVER.serve_forever()
