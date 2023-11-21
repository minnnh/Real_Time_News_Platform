import cnn_news_scraper as scraper
from bs4 import BeautifulSoup

EXPECTED_NEWS = "A former employee at a Florida gym opened fire on former co-workers"
CNN_NEWS_URL = "https://www.cnn.com/2017/04/08/us/florida-mall-shooting/index.html"

def test_basic():
	news = scraper.extract_news(CNN_NEWS_URL)

	print (news)
	assert EXPECTED_NEWS in news, "didn't find the content"
	print ('test_basic passed!')

if __name__ == "__main__":
	test_basic()