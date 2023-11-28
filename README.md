# Monitoring API

API para monitoramento de Servidor

## Atenção

*TESTADO APENAS EM DEBIAN*

## Requisitos

* [Minecraft Management Server](https://msmhq.com/docs/installation.html)
* [Python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)

### Opcional

* [Supervisor](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps)

## Instalação

### Instalar pacote virtualenv

`pip install virtualenv`

### Criar ambiente virtual

`python -m virtualenv venv`

### Utilizar o ambiente virtual

#### Linux

`source venv/bin/activate`

### Instalar dependências

`pip install -r requirements.txt`

## Iniciar Servidor

`python main.py`

## Documentação

[localhost](http://localhost:8000/docs)

## Configurações Adicionais

### Supervisor

Configurar Automaticamente o supervisor

` . configure-supervisor.sh`

Iniciar instância do supervisor

`sudo supervisorctl start monitoring-api`
