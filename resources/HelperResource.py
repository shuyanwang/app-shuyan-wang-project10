from flask_restful import Resource
from flask import jsonify, request
from services.HelperService import *
from utils.HashHelper import get_hash_from_str
from flask_jwt_extended import create_access_token


class HelperResource(Resource):

    """
    path param: helper_id
    query param: sortBy, sortOrder (sort by the property `score`, sortOrder could be either desc and asc)
    query param: filterBy, filterValue (e.g. filterBy=cities, filterValue=San Francisco)
    query param: pageSize, page (pageSize: num helpers in the same page, page, which page, starting from 1)
    """
    def get(self, helper_id=None):
        if helper_id:
            return jsonify(get_helper_by_id(helper_id))
        else:
            all_helpers = get_all_helpers(
                request.args.get('filterBy'),
                request.args.get('filterValue'),
                request.args.get('sortBy'),
                request.args.get('sortOrder'),
                request.args.get('pageSize'),
                request.args.get('page')
            )
            return jsonify(all_helpers)

    def patch(self, helper_id=None):
        if helper_id:
            return jsonify(update_helper(helper_id, request.json))
        else:
            return 'helper_id is needed for updating a helper'

    def post(self):
        json = request.json
        if json.get('email') and json.get('password'):
            email = json.get('email')
            found_helper = get_helper_by_email(email)
            if found_helper:
                return "Helper with this email already exists", 400

            password_hash = get_hash_from_str(json.get('password'))
            json['password_hash'] = password_hash
            del json['password']
            created_helper = create_helper_in_db(json)
            access_token = create_access_token(identity={
                "email": email,
                "role": "helper"
            })
            return jsonify(id=str(created_helper.id), access_token=access_token)
        else:
            return "email or password is missing in request body", 400

    def delete(self, helper_id=None):
        return jsonify(delete_helper(helper_id))
