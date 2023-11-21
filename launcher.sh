#!/bin/bash

sudo ./news_pipeline_launcher.sh 
sudo ./dashboard_launcher.sh
sudo ./visualization_launcher

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)