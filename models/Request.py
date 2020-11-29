from mongoengine import Document, StringField, DateTimeField, PointField, FloatField, EmbeddedDocument, EmbeddedDocumentListField
import datetime


class ItemDocument(EmbeddedDocument):
    item_name = StringField(required=True)
    item_type = StringField()
    size = StringField()


class RequestDocument(Document):
    items = EmbeddedDocumentListField(ItemDocument)
    request_priority = StringField()
    needer_id = StringField(required=True)
    pick_up_time = DateTimeField(required=True)
    pick_up_location = PointField(required=True)
    drop_off_time = DateTimeField(required=True)
    drop_off_location = PointField(required=True)
    reward = FloatField(required=True)
    helper_id = StringField()
    status = StringField()
    note = StringField()
    correspondence_number = StringField()
    tip = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)
