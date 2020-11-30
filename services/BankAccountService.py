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


def reset_bank_accounts():
    BankAccountDocument.drop_collection()
    all_helpers = get_all_helpers(None, None, None, None, None, None)
    the_helper_id = str(all_helpers.first().id)
    doc1 = BankAccountDocument(
        helper_id=the_helper_id,
        bank_name="Bank of America",
        account_type="Saving",
        account_number="12345",
        routing_number="122043291"
    )
    doc2 = BankAccountDocument(
        helper_id=the_helper_id,
        bank_name="Chase",
        account_type="Checking",
        account_number="23455",
        routing_number="122043294"
    )
    doc1.save()
    doc2.save()
    return BankAccountDocument.objects
