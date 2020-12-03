from flask_restful import Resource
from flask import jsonify, request, abort
from services.HelperService import *
from utils.HashHelper import get_hash_from_str
from flask_jwt_extended import create_access_token


class HelperLoginResource(Resource):

    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        if email and password:
            the_helper = get_helper_by_email(email)
            if the_helper:
                password_hash = get_hash_from_str(password)
                if password_hash == the_helper['password_hash']:
                    role = 'admin' if email == 'root@honeyandbee.com' else 'helper'
                    access_token = create_access_token(identity={
                        "email": email,
                        "role": role
                    })
                    return jsonify(id=str(the_helper.id), access_token=access_token)
                else:
                    return 'login failed either email or password is invalid', 401
            else:
                return 'login failed either email or password is invalid', 401
        else:
            return 'query parameter email or password is missing', 400
