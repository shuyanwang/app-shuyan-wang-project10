from mongoengine import Document, StringField, FloatField, BooleanField


class RatingDocument(Document):
    rating_from = StringField(required=True)
    rating_to = StringField(required=True)
    request_id = StringField(required=True)
    from_needer_to_helper = BooleanField(required=True)
    score = FloatField(required=True)
    comment = StringField()
