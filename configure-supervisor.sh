#!/bin/bash
if [[ ! -v MONITORING_API_PATH ]]; then
    export MONITORING_API_PATH=$(pwd)
fi

rm supervisor/monitoring-api.conf
sudo rm /etc/supervisor/conf.d/monitoring-api.conf

echo "[inet_http_server]" >> supervisor/monitoring-api.conf
echo "port=127.0.0.1:8001" >> supervisor/monitoring-api.conf
echo "" >> supervisor/monitoring-api.conf

echo "[rpcinterface:supervisor]" >> supervisor/monitoring-api.conf
echo "supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface" >> supervisor/monitoring-api.conf
echo "" >> supervisor/monitoring-api.conf
echo "[supervisorctl]" >> supervisor/monitoring-api.conf
echo "serverurl=http://127.0.0.1:8001" >> supervisor/monitoring-api.conf
echo "" >> supervisor/monitoring-api.conf
echo "[supervisord]" >> supervisor/monitoring-api.conf
echo "[program:monitoring-api]" >> supervisor/monitoring-api.conf
echo "environment = PYTHONUNBUFFERED=1,MONITORING_API_PATH=%(echo $MONITORING_API_PATH)s" >> supervisor/monitoring-api.conf
echo "process_name=%(program_name)s" >> supervisor/monitoring-api.conf
echo "user=root" >> supervisor/monitoring-api.conf
echo "command=/home/otavio/monitoring-api/supervisor.sh" >> supervisor/monitoring-api.conf
echo "stderr_logfile=/var/log/supervisor/monitoring-api.err.log" >> supervisor/monitoring-api.conf
echo "stdout_logfile=/var/log/supervisor/monitoring-api.out.log" >> supervisor/monitoring-api.conf

sudo cp supervisor/monitoring-api.conf /etc/supervisor/conf.d/

sudo chmod +x supervisor.sh

sudo supervisorctl reread

sudo supervisorctl update
