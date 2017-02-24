# Euler's Cookbook

A django site with solutions to some of the problems posed on the Project Euler website.

## Setup

* git clone git@github.com:zachcalvert/eulers_cookbook.git
* cd eulers_cookbook
* mkvirtualenv euler
* pip install -r requirements.txt
* echo "create database eulerdb CHARACTER SET utf8 COLLATE utf8_bin;" | mysql -u root -p  (empty password)
* cd eulers_cookbook
* ./manage.py migrate
* ./manage.py load_problems
* ./manage.py collectstatic
* ./manage.py runserver
* navigate to 'http://localhost:8000/' in a web browser