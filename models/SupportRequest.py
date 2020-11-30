from mongoengine import Document, DateTimeField, StringField, EmbeddedDocument, EmbeddedDocumentListField
import datetime


class StatusDocument(EmbeddedDocument):
    status = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now)


class SupportRequestDocument(Document):
    type = StringField(required=True)
    contact_number = StringField(required=True)
    city = StringField()
    note = StringField()
    progress = EmbeddedDocumentListField(StatusDocument)
    created_at = DateTimeField(default=datetime.datetime.now)
