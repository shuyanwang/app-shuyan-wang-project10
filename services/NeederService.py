from models.Needer import NeederDocument
import datetime


def create_needer_in_db(json) -> NeederDocument:
    needer_doc = NeederDocument(**json)
    needer_doc.save()
    return needer_doc


def update_needer(needer_id: str, json):
    the_needer = NeederDocument.objects.filter(id=needer_id).first()
    the_needer.update(**json)
    the_needer.reload()
    return the_needer


# soft delete, mark the needer as not activate use
def delete_needer(needer_id: str):
    the_needer = NeederDocument.objects.filter(id=needer_id).first()
    the_needer.update(is_activate=False)
    the_needer.reload()
    return the_needer


def get_needer_by_id(needer_id):
    return NeederDocument.objects.filter(id=needer_id).filter(is_activate=True).first()


# return all active helpers
def get_all_needers(filter_by, filter_value, sort_by, sort_order, page_size, page):
    objects = NeederDocument.objects.filter(is_activate=True)

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

