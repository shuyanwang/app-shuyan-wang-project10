from flask_restful import Resource
from flask import jsonify, request
from services.HelperService import *
from services.NeederService import *
from services.CarService import *
from services.BankAccountService import *
from services.PaymentMethodService import *
from services.RequestService import *
from services.RatingService import *
from services.SupportRequestService import *


class ResetResource(Resource):
    def get(self):
        reset_helpers()
        reset_needers()
        reset_cars()
        reset_bank_accounts()
        reset_payment_methods()
        reset_requests()
        reset_ratings()
        reset_support_requests()
        return jsonify({"message": "reset succeeded"})
