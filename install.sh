#!/usr/bin/env bash

#insall dependencies
apt-get update
apt-get install -y python3-pip
apt-get install -y python3-setuptools
apt-get install -y mysql-server
apt-get install -y mysql-client
apt-get install -y libmysqlclient15-dev
apt-get install -y python-mysqldb
apt-get install -y python-dev
apt-get install -y python3-dev
pip3 install flask
pip3 install requests
pip3 install flask_restful
pip3 install flask-jsonpify
pip3 install MySQL-python
pip3 install SQLAlchemy


#create database
python3 draft_create_db.py

#populate database
python3 draft_insert_db.py


#start API
FLASK_APP=draft_api.py python3 -m flask run --host=0.0.0.0 --port=5000