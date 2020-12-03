from models.Helper import HelperDocument, AvailableTimeDocument, HiveInfoDocument
from utils.HashHelper import get_hash_from_str


def create_helper_in_db(json) -> HelperDocument:
    helper_doc = HelperDocument(**json)
    helper_doc.save()
    return helper_doc


def update_helper(helper_id: str, json):
    the_helper = HelperDocument.objects.filter(id=helper_id).first()
    the_helper.update(**json)
    the_helper.reload()
    return the_helper


# soft delete, mark the helper as not activate use
def delete_helper(helper_id: str):
    the_helper = HelperDocument.objects.filter(id=helper_id).first()
    the_helper.update(is_activate=False)
    the_helper.reload()
    return the_helper


def get_helper_by_id(helper_id):
    return HelperDocument.objects.filter(id=helper_id).filter(is_activate=True).first()


def get_helper_by_email(email):
    return HelperDocument.objects.filter(email=email).first()


# return all active helpers
def get_all_helpers(filter_by, filter_value, sort_by, sort_order, page_size, page):
    objects = HelperDocument.objects.filter(is_activate=True)

    if filter_by and filter_value:
        objects = objects.filter(**{filter_by: filter_value})

    if sort_by:
        order = '+' if sort_order == 'asc' else '-'
        objects = objects.order_by(order + sort_by)

    if page_size and page:
        start_index = (int(page) - 1) * int(page_size)
        objects = objects[start_index: start_index + int(page_size)]

    return objects


def reset_helpers():
    HelperDocument.drop_collection()
    password_hash1 = get_hash_from_str('johnsmith')
    password_hash2 = get_hash_from_str('marysmith')
    password_hash3 = get_hash_from_str('selinasmith')
    password_hash_root = get_hash_from_str('0825')
    admin_doc = HelperDocument(
        **({
            "email": "root@honeyandbee.com",
            "password_hash": password_hash_root,
            "first_name": "Shuyan",
            "last_name": "Wang",
            "social_security_number": "1",
            "address": "",
            "phone_number": "6501231234",
            "is_valid": True
        })
    )
    helper_doc1 = HelperDocument(
        **({
            "email": "john@yahoo.com",
            "password_hash": password_hash1,
            "first_name": "John",
            "last_name": "Smith",
            "cities": ["Mountain View", "Sunnyvale"],
            "available_times": [
                {
                    "start_hour": 9,
                    "start_minute": 10,
                    "end_hour": 16,
                    "end_minute": 0
                },
                {
                    "start_hour": 16,
                    "start_minute": 10,
                    "end_hour": 20,
                    "end_minute": 0
                }
            ],
            "hive_info": {
                "home_latitude": 30.006,
                "home_longitude": 120.123,
                "office_latitude": 30.012,
                "office_longitude": 119.33,
                "go_to_work_hour": 8,
                "go_to_work_minute": 0,
                "go_home_hour": 15,
                "go_home_minute": 30
            },
            "transportations": ["car", "bike"],
            "driver_license_number": "Y123456",
            "social_security_number": "42144123",
            "address": "100 Street 1, Sunnyvale, CA, 94183",
            "phone_number": "6501231234",
            "is_valid": True,
            "score": 4.95
        })
    )
    helper_doc2 = HelperDocument(
        **({
            "email": "mary@gmail.com",
            "password_hash": password_hash2,
            "first_name": "Mary",
            "last_name": "Smith",
            "cities": ["San Francisco", "Sunnyvale"],
            "available_times": [
                {
                    "start_hour": 6,
                    "start_minute": 10,
                    "end_hour": 18,
                    "end_minute": 0
                }
            ],
            "hive_info": {
                "home_latitude": 33.1,
                "home_longitude": 121.3,
                "office_latitude": 32.7,
                "office_longitude": 123.33,
                "go_to_work_hour": 6,
                "go_to_work_minute": 0,
                "go_home_hour": 18,
                "go_home_minute": 0
            },
            "transportations": ["bike"],
            "driver_license_number": "Y222222",
            "social_security_number": "123222222",
            "address": "200 Street 3, Sunnyvale, CA, 94183",
            "phone_number": "6502222222",
            "is_valid": True,
            "score": 4.5
        })
    )
    helper_doc3 = HelperDocument(
        **({
            "email": "selina@gmail.com",
            "password_hash": password_hash3,
            "first_name": "Selina",
            "last_name": "Smith",
            "cities": ["San Jose"],
            "available_times": [
                {
                    "start_hour": 6,
                    "start_minute": 10,
                    "end_hour": 18,
                    "end_minute": 0
                }
            ],
            "hive_info": {
                "home_latitude": 33.1,
                "home_longitude": 121.3,
                "office_latitude": 32.7,
                "office_longitude": 123.33,
                "go_to_work_hour": 6,
                "go_to_work_minute": 0,
                "go_home_hour": 18,
                "go_home_minute": 0
            },
            "transportations": ["car"],
            "driver_license_number": "Y3333333",
            "social_security_number": "123333333",
            "address": "300 Street 3, Sunnyvale, CA, 94183",
            "phone_number": "6503333333",
            "is_valid": True,
            "score": 5
        })
    )

    helper_doc1.save()
    helper_doc2.save()
    helper_doc3.save()
    admin_doc.save()
    return HelperDocument.objects
