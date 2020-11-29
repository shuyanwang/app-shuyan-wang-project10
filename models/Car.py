from mongoengine import Document, StringField


class CarDocument(Document):
    helper_id = StringField(required=True)
    plate = StringField(required=True)
    state = StringField()
