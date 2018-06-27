from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]
# print(first_service.name)

id_to_find = "5b2f402d69691c068c4650a6"

service = Service.objects().with_id(id_to_find)

if service is not None:
    # hera.delete() 
    # print("Deleted")
    service.update(set__yob=1995) #update(set__<field>=value) (*)2 gạch dưới
    service.reload()
    print(service.yob)
else:
    print("Service not found")