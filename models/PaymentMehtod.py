from mongoengine import Document, StringField, IntField


class PaymentMethodDocument(Document):
    needer_id = StringField(required=True)
    bank_name = StringField()
    card_type = StringField(required=True)
    card_number = StringField(required=True, unique=True)
    expired_at = StringField(required=True)
    security_code = IntField(required=True)
