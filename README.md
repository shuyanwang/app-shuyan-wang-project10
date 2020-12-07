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




Test report
https://docs.google.com/document/d/1_z-gezVF8IkMVSsviyXuhF27spfMoKiq2rU-R7GKkFs/edit?usp=sharing

Important notes:
1.Users can only access their own data except for admin.
2.Admin is treated as a special helper.
3. Token will not expire for testing purposes.
4. It’s recommended to reset if your data gets messy.
5.As every API is protected now, you have to login as admin("email": "root@honeyandbee.com", "password": "0825") to reset. 
6. It’s recommended to test as admin unless you are testing relative features deliberately.
7.All id will change when you reset the database
8.admin account: 
 "email": "root@honeyandbee.com",
 "password": "0825"
