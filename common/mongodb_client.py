from pymongo import MongoClient
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from common_config import *
# MONGO_DB_HOST = 'localhost'
# MONGO_DB_PORT = 27017
# DB_NAME = 'tap-news'

client = MongoClient("%s:%d" %(MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db = DB_NAME):
	db = client[db]
	return db