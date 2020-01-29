from mongoengine import Document, StringField


class Allowed(Document):

    mac_dir = StringField(required=True)
