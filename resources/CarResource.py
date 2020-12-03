from flask_restful import Resource
from flask import jsonify, request, abort
from services.CarService import *
from services.HelperService import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class CarResource(Resource):

    @jwt_required
    def get(self, helper_id=None, car_id=None):
        jwt_identity = get_jwt_identity()  # { "email": "1231@af.com, "role": "helper"}
        the_helper = get_helper_by_id(helper_id)
        if jwt_identity['email'] == str(the_helper.email) or jwt_identity['role'] == 'admin':
            if car_id:
                if helper_id == get_car_by_car_id(car_id).helper_id:
                    return jsonify(get_car_by_car_id(car_id))
                else:
                    return "you are not authorized", 403
            elif helper_id:
                return jsonify(get_all_cars_for_the_helper(helper_id))
            else:
                return "bad request", 400
        else:
            return "you are not authorized", 403

    def post(self, helper_id=None):
        if helper_id:
            return jsonify(create_car_in_db(helper_id, request.json))
        else:
            abort(400)

    def delete(self, helper_id=None, car_id=None):
        delete_car_by_car_id(car_id)
        return jsonify({"message": "delete success"})
