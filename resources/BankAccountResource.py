from flask_restful import Resource
from flask import jsonify, request


class BankAccountResource(Resource):

    def get(self):
        return 'hello bank account'


