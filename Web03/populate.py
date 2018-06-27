from models.service import Service
import mlab
from random import choice
mlab.connect()


new_service = Service(
    name= "Tú Linh",
    yob= 1994,
    gender= 0,
    height=163,
    phone= "0934231124",
    address="Hà Nội",
    status=choice([True,False]),
    image = "static/image/tulinh.jpg",
    description = "ngoan hiền, dễ thương",
    measurements = [90, 60, 90]
)
new_service.save()   

# name = StringField()
# yob = IntField()
# gender = IntField()
# height = IntField()
# phone = StringField()
# address = StringField()
# status = BooleanField()
# image = ImageField()
# description = StringField()
# measurements = ListField()
