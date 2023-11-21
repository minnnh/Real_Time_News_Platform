#!/bin/bash
# remember to `chmod +x filename.sh` first
# conda activate tapNews
# sudo pip install -r requirements.txt

#brew services start redis
#brew services start mongodb-community

cd news_pipeline
python news_monitor.py &
python news_fetcher.py &
python news_deduper.py &

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)