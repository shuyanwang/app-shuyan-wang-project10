from flask_restful import Resource
from flask import jsonify, request, abort
from services.RequestService import *


class RequestResource(Resource):

    """
    path param: needer_id
    query param: sortBy, sortOrder (sort by the property `score`, sortOrder could be either desc and asc)
    query param: filterBy, filterValue (e.g. filterBy=cities, filterValue=San Francisco)
    query param: pageSize, page (pageSize: num helpers in the same page, page, which page, starting from 1)
    """
    def get(self, needer_id=None, request_id=None):
        if request_id:
            return jsonify((get_request_by_id(request_id)))
        elif needer_id:
            return jsonify(get_all_requests_for_the_needer(needer_id))
        else:
            all_requests = get_all_requests(
                request.args.get('filterBy'),
                request.args.get('filterValue'),
                request.args.get('sortBy'),
                request.args.get('sortOrder'),
                request.args.get('pageSize'),
                request.args.get('page')
            )
            return jsonify(all_requests)

    def patch(self, needer_id=None, helper_id=None, request_id=None):
        if helper_id:
            request.json['helper_id'] = helper_id
        if request_id:
            return jsonify(update_request(request_id, request.json))
        else:
            return 'request_id is needed for updating a request'

    def post(self, needer_id=None):
        if needer_id:
            the_created_request = create_request_in_db(needer_id, request.json)
            return jsonify(the_created_request)
        else:
            abort(400)

    def delete(self, request_id=None):
        delete_request(request_id)
        return jsonify({"message": "delete success"})
