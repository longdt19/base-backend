from datetime import datetime, timedelta

# methods helpler
def get_constant_by_name(constant_list, name):
    return list(filter(lambda item: item['name'] == name, constant_list))[0]['code']


def get_now_timestamp():
    return datetime.now().timestamp()
