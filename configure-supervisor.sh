#!/bin/bash
export MONITORING_API_PATH=$(pwd)

if ! [ -f /etc/supervisor/conf.d/monitoring-api.conf ]; then
    sudo cp supervisor/monitoring-api.conf /etc/supervisor/conf.d/
fi

sudo chmod +x supervisor.sh

sudo supervisorctl reread

sudo supervisorctl update
