from flask_restful import Resource
from flask import jsonify, request, abort
from services.RatingService import *


class RatingResource(Resource):
    def get(self, needer_id=None, helper_id=None, rating_id=None):
        if needer_id:
            return jsonify(get_ratings_for_the_needer(needer_id))
        elif helper_id:
            return jsonify(get_ratings_for_the_helper(helper_id))
        elif rating_id:
            return jsonify(get_rating_by_id(rating_id))
        else:
            all_ratings = get_all_ratings(
                request.args.get('filterBy'),
                request.args.get('filterValue'),
                request.args.get('sortBy'),
                request.args.get('sortOrder'),
                request.args.get('pageSize'),
                request.args.get('page')
            )
            return jsonify(all_ratings)

    def patch(self, rating_id=None):
        if rating_id:
            return jsonify(update_rating(rating_id, request.json))
        else:
            return 'rating id is needed for updating a rating'

    def post(self, request_id=None):
        if request_id:
            if 'from_needer_to_helper' in request.json:
                the_created_rating = create_rating_in_db(request_id, request.json['from_needer_to_helper'], request.json)
                return jsonify(the_created_rating)
            else:
                abort(400, 'from_needer_to_helper is missing')
        else:
            abort(400, 'request_id is missing')

    def delete(self, rating_id=None):
        delete_rating(rating_id)
        return jsonify({"message": "delete success"})
