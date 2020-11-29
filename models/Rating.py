from mongoengine import Document, StringField, FloatField


class RatingDocument(Document):
    rating_from = StringField(required=True)
    rating_to = StringField(required=True)
    request_id = StringField(required=True)
    score = FloatField(required=True)
    comment = StringField()
