from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqps://ahkufdzq:AVcDKu5oRlZd0bohjcB2wnIAiiR_E_XY@fish.rmq.cloudamqp.com/ahkufdzq"

TEST_QUEUE_NAME = "test"

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