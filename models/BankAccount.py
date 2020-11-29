from mongoengine import Document, StringField


class BankAccountDocument(Document):
    helper_id = StringField(required=True)
    bank_name = StringField()
    account_type = StringField()
    account_number = StringField(required=True, unique=True)
    routing_number = StringField(required=True)
