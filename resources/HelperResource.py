from flask_restful import Resource
from flask import jsonify, request
from services.HelperService import *


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

    def delete(self, helper_id=None):
        return jsonify(delete_helper(helper_id))
