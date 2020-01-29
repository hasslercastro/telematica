from mongoengine import *
from app.schemas.Sensor import Sensor

connect("proyecto0")


res = Sensor.objects()

for i in res:
	print(i)
