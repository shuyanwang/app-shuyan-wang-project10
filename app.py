from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.HelperResource import HelperResource
from resources.BankAccountResource import BankAccountResource
from resources.CarResource import CarResource
from resources.ResetResource import ResetResource
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
                 '/helpers',
                 '/helpers/<string:helper_id>')

api.add_resource(ResetResource,
                 '/reset')

api.add_resource(BankAccountResource,
                 '/helpers/<string:helper_id>/bankaccounts',
                 '/helpers/<string:helper_id>/bankaccounts/<string:bank_account_id>')

api.add_resource(CarResource,
                 '/helpers/<string:helper_id>/cars',
                 '/helpers/<string:helper_id>/cars/<string:car_id>')



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
