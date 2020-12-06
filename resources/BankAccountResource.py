from flask_restful import Resource
from flask import jsonify, request, abort
from utils.AuthenticationUtils import *
from services.BankAccountService import *
from services.HelperService import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class BankAccountResource(Resource):
    @jwt_required
    def get(self, helper_id=None, bank_account_id=None):
        jwt_identity = get_jwt_identity()
        the_helper = get_helper_by_id(helper_id)
        if user_has_permission(jwt_identity, the_helper):
            if bank_account_id:
                the_account = get_bank_account_by_account_id(bank_account_id)
                if the_account:
                    if helper_id == the_account.helper_id or user_is_admin(jwt_identity):
                        return jsonify(the_account)
                    else:
                        return "you are not authorized", 403
                else:
                    return "bank account not found", 404
            elif helper_id:
                return jsonify(get_all_bank_accounts_for_the_helper(helper_id))
            else:
                return "bank account id or helper id is missing", 400
        else:
            return "you are not authorized", 403

    @jwt_required
    def post(self, helper_id=None):
        if helper_id:
            jwt_identity = get_jwt_identity()
            the_helper = get_helper_by_id(helper_id)
            if user_has_permission(jwt_identity, the_helper):
                return jsonify(create_bank_account_in_db(helper_id, request.json))
            else:
                return "you are not authorized", 403
        else:
            abort(400)

    @jwt_required
    def delete(self, helper_id=None, bank_account_id=None):
        jwt_identity = get_jwt_identity()
        the_account = get_bank_account_by_account_id(bank_account_id)
        if the_account:
            the_helper = get_helper_by_id(the_account.helper_id)
            if user_has_permission(jwt_identity, the_helper):
                delete_bank_account_by_account_id(bank_account_id)
                return jsonify({"message": "delete success"})
            else:
                return 'you are not authorized', 403
        else:
            return 'bank account not found', 404
