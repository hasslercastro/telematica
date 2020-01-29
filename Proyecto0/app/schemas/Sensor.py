from mongoengine import Document, FloatField, ListField, DateTimeField
import datetime


class Sensor(Document):
    date = DateTimeField(required=True)
    weather_data = ListField(FloatField())
