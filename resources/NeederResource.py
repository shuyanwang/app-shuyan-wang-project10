from flask_restful import Resource
from flask import jsonify, request
from services.NeederService import *
from utils.HashHelper import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token
)


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
        json = request.json
        if json.get('email') and json.get('password'):
            email = json.get('email')
            found_needer = get_needer_by_email(email)
            if found_needer:
                return "needer with this email already exists", 400

            password_hash = get_hash_from_str(json.get('password'))
            json['password_hash'] = password_hash
            del json['password']
            the_created_needer = create_needer_in_db(json)
            access_token = create_access_token(identity={
                "email": email,
                "role": "needer"
            })
            return jsonify(id=str(the_created_needer.id), access_token=access_token)
        else:
            return "email or password is missing in request body", 400

    def delete(self, needer_id=None):
        return jsonify(delete_needer(needer_id))
