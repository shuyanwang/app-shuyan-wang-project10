from flask_restful import Resource
from flask import jsonify, request
from services.NeederService import *


class NeederResource(Resource):

    """
    path param: needer_id
    query param: sortBy, sortOrder (sort by the property `score`, sortOrder could be either desc and asc)
    query param: filterBy, filterValue (e.g. filterBy=cities, filterValue=San Francisco)
    query param: pageSize, page (pageSize: num docs in the same page, page, which page, starting from 1)
    """
    def get(self, needer_id=None):
        if needer_id:
            return jsonify(get_needer_by_id(needer_id))
        else:
            all_needers = get_all_needers(
                request.args.get('filterBy'),
                request.args.get('filterValue'),
                request.args.get('sortBy'),
                request.args.get('sortOrder'),
                request.args.get('pageSize'),
                request.args.get('page')
            )
            return jsonify(all_needers)

    def patch(self, needer_id=None):
        if needer_id:
            return jsonify(update_needer(needer_id, request.json))
        else:
            return 'needer_id is needed for updating a needer'

    def post(self):
        the_created_needer = create_needer_in_db(request.json)
        return jsonify(the_created_needer)

    def delete(self, needer_id=None):
        return jsonify(delete_needer(needer_id))
