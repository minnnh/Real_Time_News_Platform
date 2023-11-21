### news_topic_modeling_service
- use tensorflow and nltk to build the model and train the data
- to find the topic of each news

### ./trainer/news_cnn_model.py
- build the model to apply the data to trainer
- use tensorflow and cnn

### ./trainer/news_class_trainer.py 
- use the model to train the data
- use nltk and tensorflow

### ./server/server.py
- use the model to classify the cluster of news 
- news_fetcher in news_pipeline will connect to this server to classify the news

