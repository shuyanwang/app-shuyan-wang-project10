from mongoengine import Document, StringField, ListField, DateTimeField, FloatField, BooleanField
import datetime


class NeederDocument(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    cities = ListField(field=StringField())
    social_security_number = StringField(required=True)
    phone_number = StringField(required=True)
    score = FloatField()
    is_activate = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)
