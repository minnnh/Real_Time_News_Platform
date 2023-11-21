import news_topic_modeling_service_client as client

def test_basic():
    newsTitle = "China grants Trump a trademark he's been seeking for a decade,China moves quickly "
    topic = client.classify(newsTitle)
    print(topic)
    assert topic == "World"
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()