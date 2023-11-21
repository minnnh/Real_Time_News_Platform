#!/bin/bash
# remember to `chmod +x filename.sh` fiest
"""
Web-server:3000
Web-client:3001

Backend:4040
news_topic_modeling:6060
news_recommendation:5050
"""

# List all processes using specified ports
PORTS=(3000 3001 4040 6060 5050)  # Add your ports here
for port in "${PORTS[@]}"; do
    echo "Processes using port $port:"
    lsof -i :$port
done

# Kill all processes using specified ports
for port in "${PORTS[@]}"; do
    echo "Killing processes using port $port:"
    lsof -ti :$port | xargs kill -9
done



