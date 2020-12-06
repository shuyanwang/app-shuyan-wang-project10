from flask_restful import Resource
from flask import jsonify, request
from services.SupportRequestService import *
from utils.AuthenticationUtils import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class SupportRequestResource(Resource):

    """
    query param: sortBy, sortOrder (sort by the property `score`, sortOrder could be either desc and asc)
    query param: filterBy, filterValue (e.g. filterBy=cities, filterValue=San Francisco)
    query param: pageSize, page (pageSize: num helpers in the same page, page, which page, starting from 1)
    """
    @jwt_required
    def get(self, support_request_id=None):
        jwt_identity = get_jwt_identity()
        if user_is_admin(jwt_identity):
            if support_request_id:
                return jsonify((get_support_request_by_id(support_request_id)))
            else:
                all_requests = get_all_support_requests(
                    request.args.get('filterBy'),
                    request.args.get('filterValue'),
                    request.args.get('sortBy'),
                    request.args.get('sortOrder'),
                    request.args.get('pageSize'),
                    request.args.get('page')
                )
                return jsonify(all_requests)
        else:
            return 'only admin can get support requests', 403

    @jwt_required
    def patch(self, support_request_id=None):
        if support_request_id:
            jwt_identity = get_jwt_identity()
            if user_is_admin(jwt_identity):
                the_support_request = get_support_request_by_id(support_request_id)
                if the_support_request:
                    return jsonify(update_support_request(support_request_id, request.json))
                else:
                    return 'support request not found', 404
            else:
                return 'only admin can update support requests', 403
        else:
            return 'support_request_id is needed for updating a request'

    @jwt_required
    def post(self):
        the_created_support_request = create_support_request_in_db(request.json)
        return jsonify(the_created_support_request)

    @jwt_required
    def delete(self, support_request_id=None):
        jwt_identity = get_jwt_identity()
        if user_is_admin(jwt_identity):
            the_support_request = get_support_request_by_id(support_request_id)
            if the_support_request:
                delete_support_request(support_request_id)
                return jsonify({"message": "delete success"})
            else:
                return 'support request not found', 404
        else:
            return 'only admin can delete support requests', 403
