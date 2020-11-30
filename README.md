# Honey and Bee

### Description
Honey and Bee is an application that helps users to get their stuffs picked up. `Needers` can post their `requests` which have information like when and where to pick up the stuff. `Helpers` can get rewards by fishing the `requests`.

### Prerequisites
1. If you don't have python, [install python](https://www.python.org/downloads/)
2. If you don't have mongod, [install mongod](https://www.mongodb.com/try/download/community)
3. install python dependencies
    1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    2. [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
    3. [flask-mongoengine](https://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

### Run the server
1. Start a mongodb server locally: `mongod --dppath=~/data/db/`
2. Start the server: `flask run`




