from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.BankAccountResource import BankAccountResource
from resources.CarResource import CarResource
from resources.HelperResource import HelperResource
from resources.NeederResource import NeederResource
from resources.PaymentMethodResource import PaymentMethodResource
from resources.RatingResource import RatingResource
from resources.RequestResouce import RequestResource
from resources.SupportRequestResource import SupportRequestResource
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

api.add_resource(NeederResource,
                 '/needers',
                 '/needers/<string:needer_id>')

api.add_resource(RatingResource,
                 '/ratings',
                 '/ratings/<string:rating_id>',
                 '/requests/<string:request_id>/ratings',
                 '/helpers/<string:helper_id>/ratings',
                 '/needers/<string:needer_id>/ratings')

api.add_resource(RequestResource,
                 '/requests',
                 '/requests/<string:request_id>',
                 '/needers/<string:needer_id>/requests',
                 '/needers/<string:needer_id>/requests/<string:request_id>',
                 '/helpers/<string:helper_id>/requests/<string:request_id>')

api.add_resource(SupportRequestResource,
                 '/supportrequests',
                 '/supportrequests/<string:support_request_id>')

api.add_resource(BankAccountResource,
                 '/helpers/<string:helper_id>/bankaccounts',
                 '/helpers/<string:helper_id>/bankaccounts/<string:bank_account_id>')

api.add_resource(CarResource,
                 '/helpers/<string:helper_id>/cars',
                 '/helpers/<string:helper_id>/cars/<string:car_id>')

api.add_resource(PaymentMethodResource,
                 '/needers/<string:needer_id>/paymentmethods',
                 '/needers/<string:needer_id>/paymentmethods/<string:payment_method_id>')

api.add_resource(ResetResource,
                 '/reset')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
