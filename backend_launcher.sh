#!/bin/bash
# remember to `chmod +x filename.sh` first
# conda activate tapNews

cd backend_server
python service.py

# cd ../news_topic_modeling_service/server
# python server.py

# cd ../../recommendation_service
# python recommendation_service.py

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)