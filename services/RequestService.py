from models.Request import RequestDocument
from services.NeederService import *
import datetime


def create_request_in_db(needer_id, json) -> RequestDocument:
    the_needer = get_needer_by_id(needer_id)
    if the_needer:
        json['needer_id'] = needer_id
        json['pick_up_time'] = datetime.datetime.fromtimestamp(json['pick_up_time'] / 1e3)
        json['drop_off_time'] = datetime.datetime.fromtimestamp(json['drop_off_time'] / 1e3)
        created_doc = RequestDocument(**json)
        created_doc.save()
        return created_doc
    else:
        raise Exception("needer does not exist in db")


def update_request(request_id: str, json):
    the_request = RequestDocument.objects.filter(id=request_id).first()
    json['pick_up_time'] = datetime.datetime.fromtimestamp(json['pick_up_time'] / 1e3)
    json['drop_off_time'] = datetime.datetime.fromtimestamp(json['drop_off_time'] / 1e3)
    the_request.update(**json)
    the_request.reload()
    return the_request


def delete_request(request_id: str):
    the_request = RequestDocument.objects.filter(id=request_id).first().delete()
    return the_request


def get_request_by_id(request_id):
    return RequestDocument.objects.filter(id=request_id).first()


def get_all_requests_for_the_needer(needer_id):
    return RequestDocument.objects.filter(needer_id=needer_id)


# return all requests
def get_all_requests(filter_by, filter_value, sort_by, sort_order, page_size, page):
    objects = RequestDocument.objects

    if filter_by and filter_value:
        objects = objects.filter(**{filter_by: filter_value})

    if sort_by:
        order = '+' if sort_order == 'asc' else '-'
        objects = objects.order_by(order + sort_by)

    if page_size and page:
        start_index = (int(page) - 1) * int(page_size)
        objects = objects[start_index: start_index + int(page_size)]

    return objects

# def reset_helpers():
#     HelperDocument.drop_collection()
#     helper_doc1 = HelperDocument(
#         **({
#             "first_name": "John",
#             "last_name": "Smith",
#             "cities": ["Mountain View", "Sunnyvale"],
#             "available_times": [
#                 {
#                     "start_hour": 9,
#                     "start_minute": 10,
#                     "end_hour": 16,
#                     "end_minute": 0
#                 },
#                 {
#                     "start_hour": 16,
#                     "start_minute": 10,
#                     "end_hour": 20,
#                     "end_minute": 0
#                 }
#             ],
#             "hive_info": {
#                 "home_latitude": 30.006,
#                 "home_longitude": 120.123,
#                 "office_latitude": 30.012,
#                 "office_longitude": 119.33,
#                 "go_to_work_hour": 8,
#                 "go_to_work_minute": 0,
#                 "go_home_hour": 15,
#                 "go_home_minute": 30
#             },
#             "transportations": ["car", "bike"],
#             "driver_license_number": "Y123456",
#             "social_security_number": "42144123",
#             "address": "100 Street 1, Sunnyvale, CA, 94183",
#             "phone_number": "6501231234",
#             "is_valid": True,
#             "score": 4.95
#         })
#     )
#     helper_doc2 = HelperDocument(
#         **({
#             "first_name": "Mary",
#             "last_name": "Smith",
#             "cities": ["San Francisco", "Sunnyvale"],
#             "available_times": [
#                 {
#                     "start_hour": 6,
#                     "start_minute": 10,
#                     "end_hour": 18,
#                     "end_minute": 0
#                 }
#             ],
#             "hive_info": {
#                 "home_latitude": 33.1,
#                 "home_longitude": 121.3,
#                 "office_latitude": 32.7,
#                 "office_longitude": 123.33,
#                 "go_to_work_hour": 6,
#                 "go_to_work_minute": 0,
#                 "go_home_hour": 18,
#                 "go_home_minute": 0
#             },
#             "transportations": ["bike"],
#             "driver_license_number": "Y222222",
#             "social_security_number": "123222222",
#             "address": "200 Street 3, Sunnyvale, CA, 94183",
#             "phone_number": "6502222222",
#             "is_valid": True,
#             "score": 4.5
#         })
#     )
#     helper_doc3 = HelperDocument(
#         **({
#             "first_name": "Selina",
#             "last_name": "Smith",
#             "cities": ["San Jose"],
#             "available_times": [
#                 {
#                     "start_hour": 6,
#                     "start_minute": 10,
#                     "end_hour": 18,
#                     "end_minute": 0
#                 }
#             ],
#             "hive_info": {
#                 "home_latitude": 33.1,
#                 "home_longitude": 121.3,
#                 "office_latitude": 32.7,
#                 "office_longitude": 123.33,
#                 "go_to_work_hour": 6,
#                 "go_to_work_minute": 0,
#                 "go_home_hour": 18,
#                 "go_home_minute": 0
#             },
#             "transportations": ["car"],
#             "driver_license_number": "Y3333333",
#             "social_security_number": "123333333",
#             "address": "300 Street 3, Sunnyvale, CA, 94183",
#             "phone_number": "6503333333",
#             "is_valid": True,
#             "score": 5
#         })
#     )
#     helper_doc1.save()
#     helper_doc2.save()
#     helper_doc3.save()
#     return HelperDocument.objects

