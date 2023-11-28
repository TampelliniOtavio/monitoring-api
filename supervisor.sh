#!/bin/bash

if [[ -z "${MONITORING_API_PATH}" ]]; then
    echo "Caminho da API não configurado, por favor executar configure-supervisor.sh"
    exit
fi

cd $MONITORING_API_PATH

if ! [ -f venv ]; then
    python3 -m venv venv
    echo "*" > venv/.gitignore
fi

source venv/bin/activate

pip install -r requirements.txt
python main.py