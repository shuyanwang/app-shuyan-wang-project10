from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, EmbeddedDocumentListField, StringField, ListField,\
    IntField, DateTimeField, FloatField, BooleanField
import datetime


class AvailableTimeDocument(EmbeddedDocument):
    start_hour = IntField()
    start_minute = IntField()
    end_hour = IntField()
    end_minute = IntField()


class HiveInfoDocument(EmbeddedDocument):
    home_latitude = FloatField()
    home_longitude = FloatField()
    office_latitude = FloatField()
    office_longitude = FloatField()
    go_to_work_hour = IntField()
    go_to_work_minute = IntField()
    go_home_hour = IntField()
    go_home_minute = IntField()


class HelperDocument(Document):
    email = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    cities = ListField(field=StringField())
    transportations = ListField(field=StringField())
    available_times = EmbeddedDocumentListField(AvailableTimeDocument)
    hive_info = EmbeddedDocumentField(HiveInfoDocument)
    driver_license_number = StringField()
    social_security_number = StringField(required=True)
    address = StringField(required=True)
    phone_number = StringField(required=True)
    score = FloatField()
    is_activate = BooleanField(default=True)
    is_valid = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
