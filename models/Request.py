from mongoengine import Document, StringField, DateTimeField, PointField, FloatField, EmbeddedDocumentListField


class ItemDocument(Document):
    item_name = StringField(required=True)
    item_type = StringField()
    size = StringField()


class RequestDocument(Document):
    items = EmbeddedDocumentListField(ItemDocument)
    request_priority = StringField()
    pick_up_time = DateTimeField(required=True)
    pick_up_location = PointField(required=True)
    drop_off_time = DateTimeField(required=True)
    drop_off_location = PointField(required=True)
    reward = FloatField(required=True)
    note = StringField()
    status = StringField()
    need_id = StringField(required=True)
    helper_id = StringField()
    correspondence_number = StringField()
    tip = FloatField()
