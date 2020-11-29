from models.BankAccount import BankAccountDocument
from services.HelperService import *


def create_bank_account_in_db(helper_id, json):
    the_helper = get_helper_by_id(helper_id)
    if the_helper:
        json['helper_id'] = helper_id
        created_doc = BankAccountDocument(**json)
        created_doc.save()
        return created_doc
    else:
        raise Exception("helper does not exist in db")


def get_all_bank_accounts_for_the_helper(helper_id):
    return BankAccountDocument.objects.filter(helper_id=helper_id)


def get_bank_account_by_account_id(bank_account_id):
    return BankAccountDocument.objects.filter(id=bank_account_id).first()


def delete_bank_account_by_account_id(bank_account_id):
    return BankAccountDocument.objects.filter(id=bank_account_id).first().delete()
