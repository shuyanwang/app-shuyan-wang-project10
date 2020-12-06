from flask_restful import Resource
from flask import jsonify, request
from services.NeederService import *
from utils.HashUtils import get_hash_from_str
from flask_jwt_extended import create_access_token


class NeederLoginResource(Resource):

    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        if email and password:
            the_needer = get_needer_by_email(email)
            if the_needer and the_needer.is_activate:
                password_hash = get_hash_from_str(password)
                if password_hash == the_needer['password_hash']:
                    access_token = create_access_token(identity={
                        "email": email,
                        "role": "needer"
                    })
                    return jsonify(id=str(the_needer.id), access_token=access_token)
                else:
                    return 'login failed either email or password is invalid', 401
            else:
                return 'login failed either email or password is invalid', 401
        else:
            return 'email or password is missing in request body', 400
