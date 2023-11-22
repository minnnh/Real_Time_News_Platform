DEDUPE_NEWS_TASK_QUEUE_URL = 'amqps://eviywzfr:Eu1cq8176zK4dfANwzaQVp57XIakXaT_@fish.rmq.cloudamqp.com/eviywzfr'
DEDUPE_NEWS_TASK_QUEUE_NAME = 'tap-news-dedupe-news-task-queue'

SLEEP_TIME_IN_SECONDS = 1

NEWS_TABLE_NAME = "news-test"

SAME_NEWS_SIMILARITY_THRESHOLD = 0.8

SCRAPE_NEWS_TASK_QUEUE_URL = 'amqps://ahkufdzq:AVcDKu5oRlZd0bohjcB2wnIAiiR_E_XY@fish.rmq.cloudamqp.com/ahkufdzq'
SCRAPE_NEWS_TASK_QUEUE_NAME = 'tap-news-scrape-news-task-queue'

SLEEP_TIME_IN_SECONDS = 5

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24

NEWS_SOURCES = [
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]


