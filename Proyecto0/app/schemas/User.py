from mongoengine import Document , StringField, FloatField, ListField, BinaryField

class User(Document):

    username = StringField(unique=True, required= True)
    password = BinaryField(required=True)
    weather_data = ListField(ListField(FloatField()))

