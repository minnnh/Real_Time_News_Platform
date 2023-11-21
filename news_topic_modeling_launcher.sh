#!/bin/bash
# remember to `chmod +x filename.sh` first
# conda activate tapNews
# sudo pip install -r requirements.txt

#brew services start redis
#brew services start mongodb-community

cd ./news_topic_modeling_service/server
python server.py

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)