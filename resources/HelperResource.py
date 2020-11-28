from flask_restful import Resource
from flask import jsonify, request
from services.HelperService import *


class HelperResource(Resource):

    def get(self):
        return jsonify(get_all_helpers())

    def post(self):
        the_created_helper = create_helper_in_db(
            request.json.get('first_name'),
            request.json.get('last_name'),
            request.json.get('cities'),
            request.json.get('transportations'),
            request.json.get('available_times'),
            request.json.get('hive_info'),
            request.json.get('driver_license_number'),
            request.json.get('social_security_number'),
            request.json.get('address'),
            request.json.get('phone_number'),
            request.json.get('score'),
            # default is_active is true
            True,
            # default is_valid is false
            False
        )
        return jsonify(the_created_helper)


