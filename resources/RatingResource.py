from flask_restful import Resource
from flask import jsonify, request, abort
from services.RatingService import *
from services.HelperService import *
from services.NeederService import *
from utils.AuthenticationUtils import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class RatingResource(Resource):
    @jwt_required
    def get(self, needer_id=None, helper_id=None, rating_id=None):
        jwt_identity = get_jwt_identity()
        if needer_id:
            the_needer = get_needer_by_id(needer_id)
            if the_needer:
                if user_has_permission(jwt_identity, the_needer):
                    return jsonify(get_ratings_to_the_needer(needer_id))
                else:
                    return "you are not authorized", 403
            else:
                return 'needer not found', 404
        elif helper_id:
            the_helper = get_helper_by_id(helper_id)
            if the_helper:
                if user_has_permission(jwt_identity, the_helper):
                    return jsonify(get_ratings_to_the_helper(helper_id))
                else:
                    return "you are not authorized", 403
            else:
                return 'helper not found', 404
        elif rating_id:
            # both rating from and rating to users can see the rating
            the_rating = get_rating_by_id(rating_id)
            if the_rating:
                the_needer = None
                the_helper = None
                if the_rating.from_needer_to_helper:
                    the_needer = get_needer_by_id(the_rating.rating_from)
                    the_helper = get_helper_by_id(the_rating.rating_to)
                else:
                    the_needer = get_needer_by_id(the_rating.rating_to)
                    the_helper = get_helper_by_id(the_rating.rating_from)
                if user_has_permission(jwt_identity, the_helper) or user_has_permission(jwt_identity, the_needer):
                    return jsonify(the_rating)
                else:
                    return 'you are not authorized', 403
            else:
                return 'rating not found', 404
        else:
            if user_is_admin(jwt_identity):
                all_ratings = get_all_ratings(
                    request.args.get('filterBy'),
                    request.args.get('filterValue'),
                    request.args.get('sortBy'),
                    request.args.get('sortOrder'),
                    request.args.get('pageSize'),
                    request.args.get('page')
                )
                return jsonify(all_ratings)
            else:
                return 'only admin can get all ratings', 403

    @jwt_required
    def patch(self, rating_id=None):
        if rating_id:
            jwt_identity = get_jwt_identity()
            the_rating = get_rating_by_id(rating_id)
            if the_rating:
                the_rating_from_user = get_needer_by_id(the_rating.rating_from) \
                    if the_rating.from_needer_to_helper else get_helper_by_id(the_rating.rating_from)
                if user_has_permission(jwt_identity, the_rating_from_user):
                    return jsonify(update_rating(rating_id, request.json))
                else:
                    return 'you are not authorized', 403
            else:
                return 'rating not found', 404
        else:
            return 'rating id is needed for updating a rating', 400

    @jwt_required
    def post(self, request_id=None):
        if request_id:
            jwt_identity = get_jwt_identity()
            the_request = get_request_by_id(request_id)
            if the_request:
                if the_request.helper_id:
                    if 'from_needer_to_helper' in request.json:
                        the_rating_from_user = get_needer_by_id(the_request.needer_id) \
                            if request.json.get('from_needer_to_helper') else get_helper_by_id(the_request.helper_id)
                        if user_has_permission(jwt_identity, the_rating_from_user):
                            the_created_rating = create_rating_in_db(request_id, request.json['from_needer_to_helper'], request.json)
                            return jsonify(the_created_rating)
                        else:
                            return 'you are not authorized', 403
                    else:
                        return 'from_needer_to_helper is missing in request body', 400
                else:
                    return 'the request does not have helper_id', 400
            else:
                return 'request not found', 404
        else:
            return 'request_id is missing', 400

    @jwt_required
    def delete(self, rating_id=None):
        the_rating = get_rating_by_id(rating_id)
        if the_rating:
            jwt_identity = get_jwt_identity()
            the_rating_from_user = get_needer_by_id(the_rating.rating_from) \
                if the_rating.from_needer_to_helper else get_helper_by_id(the_rating.rating_from)
            if user_has_permission(jwt_identity, the_rating_from_user):
                delete_rating(rating_id)
                return jsonify({"message": "delete success"})
            else:
                return 'you are not authorized', 403
        else:
            return 'rating not found', 404
