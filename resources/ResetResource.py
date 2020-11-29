from flask_restful import Resource
from flask import jsonify, request
from services.HelperService import *


class ResetResource(Resource):
    def get(self):
        return jsonify(reset_helpers())
