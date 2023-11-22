#!/bin/bash
# remember to `chmod +x filename.sh` first
# conda activate tapNews
# sudo pip install -r requirements.txt

#brew services start redis
#brew services start mongodb-community

cd ./recommendation_service
python click_log_processor.py

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)