from flask_restful import Resource
from flask import jsonify, request, abort
from services.PaymentMethodService import *


class PaymentMethodResource(Resource):

    def get(self, needer_id=None, payment_method_id=None):
        if payment_method_id:
            return jsonify(get_payment_method_by_payment_method_id(payment_method_id))
        elif needer_id:
            return jsonify(get_all_payment_methods_for_the_needer(needer_id))
        else:
            abort(400)

    def post(self, needer_id=None):
        if needer_id:
            return jsonify(create_payment_method_in_db(needer_id, request.json))
        else:
            abort(400)

    def patch(self, needer_id=None, payment_method_id=None):
        if payment_method_id:
            return jsonify(update_payment_method_by_payment_method_id(payment_method_id, request.json))
        else:
            abort(400)

    def delete(self, needer_id=None, payment_method_id=None):
        if payment_method_id:
            delete_payment_method_by_payment_method_id(payment_method_id)
            return jsonify({"message": "delete success"})
        else:
            abort(400)
