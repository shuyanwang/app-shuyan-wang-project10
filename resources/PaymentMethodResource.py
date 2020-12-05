from flask_restful import Resource
from flask import jsonify, request
from services.PaymentMethodService import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class PaymentMethodResource(Resource):

    @jwt_required
    def get(self, needer_id=None, payment_method_id=None):
        jwt_identity = get_jwt_identity()
        the_needer = get_needer_by_id(needer_id)
        if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
            if payment_method_id:
                the_method = get_payment_method_by_payment_method_id(payment_method_id)
                if the_method:
                    if needer_id == the_method.needer_id or jwt_identity['role'] == 'admin':
                        return jsonify(the_method)
                    else:
                        return "you are not authorized", 403
                else:
                    return "payment method not found", 404
            elif needer_id:
                return jsonify(get_all_payment_methods_for_the_needer(needer_id))
            else:
                return "needer id or payment method is missing", 400
        else:
            return "you are not authorized", 403

    @jwt_required
    def post(self, needer_id=None):
        if needer_id:
            jwt_identity = get_jwt_identity()
            the_needer = get_needer_by_id(needer_id)
            if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                return jsonify(create_payment_method_in_db(needer_id, request.json))
            else:
                return "you are not authorized", 403
        else:
            return "needer id is missing", 400

    @jwt_required
    def patch(self, needer_id=None, payment_method_id=None):
        jwt_identity = get_jwt_identity()
        the_method = get_payment_method_by_payment_method_id(payment_method_id)
        if the_method:
            the_needer = get_needer_by_id(the_method.needer_id)
            if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                return jsonify(update_payment_method_by_payment_method_id(payment_method_id, request.json))
            else:
                return "you are not authorized", 403
        else:
            return "payment method not found", 404

    @jwt_required
    def delete(self, needer_id=None, payment_method_id=None):
        jwt_identity = get_jwt_identity()
        the_method = get_payment_method_by_payment_method_id(payment_method_id)
        if the_method:
            the_needer = get_needer_by_id(the_method.needer_id)
            if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                delete_payment_method_by_payment_method_id(payment_method_id)
                return jsonify({"message": "delete success"})
            else:
                return "you are not authorized", 403
        else:
            return "payment method not found", 404
