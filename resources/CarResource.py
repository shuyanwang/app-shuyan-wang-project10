from flask_restful import Resource
from flask import jsonify, request
from utils.AuthenticationUtils import *
from services.CarService import *
from services.HelperService import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class CarResource(Resource):
    @jwt_required
    def get(self, helper_id=None, car_id=None):
        jwt_identity = get_jwt_identity()
        the_helper = get_helper_by_id(helper_id)
        if user_has_permission(jwt_identity, the_helper):
            if car_id:
                the_car = get_car_by_car_id(car_id)
                if the_car:
                    if helper_id == the_car.helper_id or jwt_identity['role'] == 'admin':
                        return jsonify(the_car)
                    else:
                        return "you are not authorized", 403
                else:
                    return "car not found", 404
            elif helper_id:
                return jsonify(get_all_cars_for_the_helper(helper_id))
            else:
                return "car id or helper id is missing", 400
        else:
            return "you are not authorized", 403

    @jwt_required
    def post(self, helper_id=None):
        if helper_id:
            jwt_identity = get_jwt_identity()
            the_helper = get_helper_by_id(helper_id)
            if user_has_permission(jwt_identity, the_helper):
                return jsonify(create_car_in_db(helper_id, request.json))
            else:
                return "you are not authorized", 403
        else:
            return "missing helper_id", 400

    @jwt_required
    def delete(self, helper_id=None, car_id=None):
        jwt_identity = get_jwt_identity()
        the_car = get_car_by_car_id(car_id)
        if the_car:
            the_helper = get_helper_by_id(the_car.helper_id)
            if user_has_permission(jwt_identity, the_helper):
                delete_car_by_car_id(car_id)
                return jsonify({"message": "delete success"})
            else:
                return "you are not authorized", 403
        else:
            return "car not found", 404
