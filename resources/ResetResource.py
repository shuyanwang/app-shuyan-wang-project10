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
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class ResetResource(Resource):
    @jwt_required
    def get(self):
        jwt_identity = get_jwt_identity()
        if jwt_identity['role'] == 'admin':
            reset_helpers()
            reset_needers()
            reset_cars()
            reset_bank_accounts()
            reset_payment_methods()
            reset_requests()
            reset_ratings()
            reset_support_requests()
            return jsonify({"message": "reset succeeded"})
        else:
            return 'only admin can reset', 403
