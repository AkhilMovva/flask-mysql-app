# flask-mysql-app

## Update the db.yaml respectively 

- mysql_host: 'localhost'
- mysql_user: 'root'
- mysql_password: 'password'
- mysql_db: 'flaskapp'

## Useful Commands
```
sudo apt update -y
sudo apt install python3-pip -y
sudo apt-get install python3.8

pip3 install flask
sudo apt-get install libmysqlclient-dev -y
pip3 install flask-mysqldb

sudo mysql -u root -p
mysql> create database flaskapp;
mysql> use flaskapp;
mysql> create table users(name varchar(20), email varchar(40));
```
