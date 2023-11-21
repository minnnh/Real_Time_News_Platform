- monitor -> fetcher -> dedupe

### monitor news
- use newsapi to get the top news
- send the news to the host
- use redis to chache the news 

### fetch news (scrape news)
- fetch the news from monitor host
- SCRAPE_NEWS_URL to scrape news. (monitor -> scrape)
- DEDUPE_NEWS_URL to dedupe news. (scrape -> dedupe)

### dedupe news
- use TF-IDF to dedupe the news
- use news_topic_modeling_service server to classify the data and get the topic of each news
- store the deduped news to mongodb 

### monitor -> fetcher -> deduper
- monitor -> redis & fetcher amqp
- fetch from fetcher amqp -> send to deduper amqp
- deduper recieve data from deduper amqp -> send to mongodb