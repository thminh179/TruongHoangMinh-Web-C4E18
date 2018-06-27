import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds217131.mlab.com:17131/muadongkhonglanhc4e

host = "ds217131.mlab.com"
port = 17131
db_name = "muadongkhonglanhc4e"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())