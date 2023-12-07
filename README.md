# Real Time News Scraping and Recommendation System
Real Time News Scraping and Recommendation System is a web application that provides users with the latest news from various sources such as CNN, BBC, and The New York Times. This system utilizes a robust news pipeline to scrape the most recent updates from different news outlets and tailors the news feed to each user's preferences.

## Demo
![show](./img/show2.gif)
## Environment
- Python 3.8.18
- npm 10.1
- Node.js v20.9
- Nodemon 3.0.1
- Conda env -- tapNews

## Built with
- __News Pipeline__: MongoDB, Redis, RabbitMQ, TF-IDF
- __News Topic Modeling__: TensorFlow, CNN, NLP
- __News Recommendation__: NLP
- __Web Server__: React, Node.js, RPC, SOA, JWT

## How It Works
- __News Pipeline__: The system continually monitors, fetches, deduplicates, and updates the database with the latest news, ensuring real-time information.
- __News Topic Modeling__: Utilizing TensorFlow, CNN, and NLP, the system trains a pipeline to model news topics, enhancing the relevance of recommended news articles.
- __News Recommendations__: Users receive personalized news recommendations based on their interests and preferences.
- __Web Application__: The ReactJS frontend offers a user-friendly interface, while the Node.js backend processes data, facilitates JSON-RPC communication.
- __Backend Service__: The server monitors, fetches, and updates the database with real-time news. It manages data from the frontend, TensorFlow serving, and training processes, connecting seamlessly with the database for efficient data processing.

## Connections
- __backend-server <-> web-server server__
    - JSON-RPC
    - Jayson
- __web-server: server <-> client__
    - React
    - Express

## Getting Started
To get started with the Real Time News Scraping and Recommendation System, follow these steps:

### Prerequisites
- install npm  
```sh
npm install -g npm@10.1
```
- install node.js  
```sh
npm install -g node
```
```sh
node -v 20.9.0
```
- install nodemon  
```sh
npm install -g nodemon@3.0.1
```

### Installation
1. clone the repo  
```sh
git clone https://github.com/minnnh/Real_Time_News_Platform
```
2. install the requirements  
```sh
pip install -r requirements.txt
```
3. run the system  
```sh
sudo ./backend_launcher.sh
```
```sh
sudo ./news_pipeline_launcher.sh
```
```sh
sudo ./news_recommendation_launcher.sh
```
```sh
sudo ./news_topic_modeling_launcher.sh
```
```sh
sudo ./click_log_processor.sh  
```
```sh
sudo ./web_client_launcher.sh
```
```sh
sudo ./web_server_launcher.sh
```

## Todo List
### coding
- [x] backend-server
- [x] common
- [x] pipeline
- [x] topic modeling
- [x] recommendation
    - [x] recommendation service
    - [x] conmmon
    - [x] backend-server
    - [x] web-client
    - [x] web-server 
- [x] web-server server
	- [x] middleware 
    - [x] models (mongoose)
    - [x] config
	- [x] passport
	- [x] routes
    - [x] app
- [x] web-server client
	- [x] auth
	- [x] base
	- [x] signup
	- [x] login

### testing
- [x] backend-server
- [x] common
- [x] pipeline
- [x] topic modeling
- [x] recommendation
- [x] web-server server
    - [x] login
    - [x] signup
    - [x] news
- [x] web-server client
    - [x] login
    - [x] signup
    - [x] logout
    - [x] news panel
