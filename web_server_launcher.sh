#!/bin/bash
# remember to `chmod +x filename.sh` first
# conda activate tapNews

# start server
cd web_server/server
nodemon start

echo "=================================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)