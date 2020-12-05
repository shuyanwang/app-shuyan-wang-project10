from flask_restful import Resource
from flask import jsonify, request, abort
from services.RequestService import *
from services.HelperService import *
from services.NeederService import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class RequestResource(Resource):

    """
    path param: needer_id
    query param: sortBy, sortOrder (sort by the property `score`, sortOrder could be either desc and asc)
    query param: filterBy, filterValue (e.g. filterBy=cities, filterValue=San Francisco)
    query param: pageSize, page (pageSize: num helpers in the same page, page, which page, starting from 1)
    """
    @jwt_required
    def get(self, helper_id=None, needer_id=None, request_id=None):
        jwt_identity = get_jwt_identity()
        if request_id:
            the_request = get_request_by_id(request_id)
            the_needer = get_needer_by_id(the_request.needer_id)
            if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                return jsonify(the_request)
            elif the_request.helper_id:
                the_helper = get_helper_by_id(the_request.helper_id)
                if jwt_identity['email'] == str(the_helper.email):
                    return jsonify(the_request)
                else:
                    return 'you are not authorized', 403
            else:
                return 'you are not authorized', 403
        elif needer_id:
            the_needer = get_needer_by_id(needer_id)
            if the_needer:
                if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                    return jsonify(get_all_requests_for_the_needer(needer_id))
                else:
                    return 'you are not authorized', 403
            else:
                return 'needer not found', 404
        elif helper_id:
            the_helper = get_helper_by_id(helper_id)
            if the_helper:
                if jwt_identity['email'] == str(the_helper.email) or jwt_identity['role'] == 'admin':
                    return jsonify(get_all_requests_for_the_helper(helper_id))
                else:
                    return 'you are not authorized', 403
            else:
                return 'helpers not found', 404
        else:
            if jwt_identity['role'] == 'admin':
                all_requests = get_all_requests(
                    request.args.get('filterBy'),
                    request.args.get('filterValue'),
                    request.args.get('sortBy'),
                    request.args.get('sortOrder'),
                    request.args.get('pageSize'),
                    request.args.get('page')
                )
                return jsonify(all_requests)
            else:
                return 'only admin can get all requests', 403

    @jwt_required
    def patch(self, needer_id=None, helper_id=None, request_id=None):
        jwt_identity = get_jwt_identity()
        if request_id:
            the_request = get_request_by_id(request_id)
            if the_request:
                if helper_id:
                    # helper can only change helper_id and status for a request
                    the_helper = get_helper_by_id(helper_id)
                    if the_helper:
                        if jwt_identity['email'] == str(the_helper.email) or jwt_identity['role'] == 'admin' and\
                                (not the_request.helper_id or str(the_request.helper_id) == helper_id):
                            json = {"helper_id": helper_id, "status": request.json['status']}
                            return jsonify(update_request(request_id, json))
                        else:
                            return 'you are not authorized', 403
                    else:
                        return 'helper not found', 404
                else:
                    the_needer = get_needer_by_id(the_request.needer_id)
                    if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                        return jsonify(update_request(request_id, request.json))
                    else:
                        return 'you are not authorized', 403
            else:
                return 'request not found', 404
        else:
            return 'request_id is needed for updating a request', 400

    @jwt_required
    def post(self, needer_id=None):
        if needer_id:
            jwt_identity = get_jwt_identity()
            the_needer = get_needer_by_id(needer_id)
            if the_needer:
                if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                    the_created_request = create_request_in_db(needer_id, request.json)
                    return jsonify(the_created_request)
                return 'you are not authorized', 403
            else:
                return 'needer not found', 404
        else:
            return 'needer id is needed for creating a request', 400

    @jwt_required
    def delete(self, request_id=None):
        the_request = get_request_by_id(request_id)
        if the_request:
            jwt_identity = get_jwt_identity()
            the_needer = get_needer_by_id(the_request.needer_id)
            if jwt_identity['email'] == str(the_needer.email) or jwt_identity['role'] == 'admin':
                delete_request(request_id)
                return jsonify({"message": "delete success"})
            else:
                return 'you are not authorized', 403
        else:
            return 'request not found', 404
