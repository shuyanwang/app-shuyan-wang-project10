from flask_restful import Resource
from flask import jsonify, request, abort
from services.BankAccountService import *


class BankAccountResource(Resource):

    def get(self, helper_id=None, bank_account_id=None):
        if bank_account_id:
            return jsonify(get_bank_account_by_account_id(bank_account_id))
        elif helper_id:
            return jsonify(get_all_bank_accounts_for_the_helper(helper_id))
        else:
            abort(400)

    def post(self, helper_id=None):
        if helper_id:
            return jsonify(create_bank_account_in_db(helper_id, request.json))
        else:
            abort(400)
