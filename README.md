# draft_code
code challenge


Files:
install.sh - Bash script that installs and runs code
sports.json - file containing the urls for the download
draft_create_db - creates the sql database
draft_insert_db - populates database
draft_api - quieries database and returns json data


Python Modules:
The following modules are installed via the pip3 install command in the install script
flask
equests
flask_restful
flask-jsonpify
MySQL-python
SQLAlchemy

Other Dependencies:
The following are installed via a an apt-get install command in the install script
python3-pip
python3-setuptools
mysql-server
mysql-client
libmysqlclient15-dev
python-mysqldb
python-dev
python3-dev


Instructions:
Recommended to do in virtual environment
#download the files via the terminal line with
git clone --depth=1 https://github.com/GeneralTstohs/draft_code.git
#move into draft_code directory
cd draft_code
#run instal script
sudo sh script.sh

The API can be accessed at localhost:5000/draft/players 
for the players query and at localhost:5000/draft/sport
for the sport query



















