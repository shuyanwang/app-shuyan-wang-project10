from flask_restful import Resource
from flask import jsonify, request
from services.SupportRequestService import *


class SupportRequestResource(Resource):

    """
    query param: sortBy, sortOrder (sort by the property `score`, sortOrder could be either desc and asc)
    query param: filterBy, filterValue (e.g. filterBy=cities, filterValue=San Francisco)
    query param: pageSize, page (pageSize: num helpers in the same page, page, which page, starting from 1)
    """
    def get(self, support_request_id=None):
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

    def patch(self, support_request_id=None):
        if support_request_id:
            return jsonify(update_support_request(support_request_id, request.json))
        else:
            return 'support_request_id is needed for updating a request'

    def post(self):
        the_created_support_request = create_support_request_in_db(request.json)
        return jsonify(the_created_support_request)

    def delete(self, support_request_id=None):
        delete_support_request(support_request_id)
        return jsonify({"message": "delete success"})
