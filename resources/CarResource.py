from flask_restful import Resource
from flask import jsonify, request, abort
from services.CarService import *


class CarResource(Resource):

    def get(self, helper_id=None, car_id=None):
        if car_id:
            return jsonify(get_car_by_car_id(car_id))
        elif helper_id:
            return jsonify(get_all_cars_for_the_helper(helper_id))
        else:
            abort(400)

    def post(self, helper_id=None):
        if helper_id:
            return jsonify(create_car_in_db(helper_id, request.json))
        else:
            abort(400)

    def delete(self, helper_id=None, car_id=None):
        return jsonify(delete_car_by_car_id(car_id))
