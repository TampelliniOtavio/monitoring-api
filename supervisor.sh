#!bin/bash

cd /home/otavio/monitoring-api

git restore --staged .
git restore .
git switch main
git pull

if ! [ -f /home/otavio/monitoring-api/venv ]; then
    python3 -m virtualenv venv
    echo "*" > venv/.gitignore
fi

source venv/bin/activate

pip install -r requirements.txt
python main.py