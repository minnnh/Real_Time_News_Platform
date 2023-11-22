import jsonrpclib
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from common_config import *
# RECOMMEND_URL = "http://localhost:5050/"

client = jsonrpclib.ServerProxy(RECOMMEND_URL)

def getPreferenceForUser(userId):
    preference = client.getPreferenceForUser(userId)
    print("Preference list: %s" % str(preference))
    return preference
    