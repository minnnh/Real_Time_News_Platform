from cloudAMQP_client import CloudAMQPClient
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from common_config import *

# TEST_QUEUE_NAME = "test"

def test_basic():
	client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

	sentMsg = {"test":"demo"}
	client.sendMessage(sentMsg)
	client.sleep(10)
	receivedMsg = client.getMessage()
	assert receivedMsg == sentMsg
	print ("CloudAMQP test passed!")

if __name__ == '__main__':
	test_basic()