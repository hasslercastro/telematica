from mongoengine import Document, StringField, BinaryField


class User(Document):
    username = StringField(unique=True, required=True)
    password = BinaryField(required=True)
