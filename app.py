from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.HelperResource import HelperResource
from utils.JSONEncoder import MongoEngineJSONEncoder

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-shuyanwa',
    'host': 'mongodb://localhost:27017/app-shuyanwa'
}

initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)

api.add_resource(HelperResource,
                 '/helpers')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
