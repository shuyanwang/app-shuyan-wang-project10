from models.Helper import HelperDocument, AvailableTimeDocument, HiveInfoDocument
import datetime


def create_helper_in_db(
    first_name: str,
    last_name: str,
    cities: list,
    transportations: list,
    available_times: list,
    hive_info: dict,
    driver_license_number: str,
    social_security_number: str,
    address: str,
    phone_number: str,
    score: float,
    is_activate: bool,
    is_valid: bool,
) -> HelperDocument:
    available_times_docs = []
    for available_time in available_times:
        available_time_doc = AvailableTimeDocument(
            start_hour=available_time['start_hour'],
            end_hour=available_time['end_hour'],
            start_minute=available_time['start_minute'],
            end_minute=available_time['end_minute'],
        )
        available_times_docs.append(available_time_doc)

    hive_info_doc = HiveInfoDocument(
        home_latitude=hive_info['home_latitude'],
        home_longitude=hive_info['home_longitude'],
        office_latitude=hive_info['office_latitude'],
        office_longitude=hive_info['office_longitude'],
        go_to_work_hour=hive_info['go_to_work_hour'],
        go_to_work_minute=hive_info['go_to_work_minute'],
        go_home_hour=hive_info['go_home_hour'],
        go_home_minute=hive_info['go_home_minute']
    )

    helper_doc = HelperDocument(
        first_name=first_name,
        last_name=last_name,
        cities=cities,
        transportations=transportations,
        available_times=available_times_docs,
        hive_info=hive_info_doc,
        driver_license_number=driver_license_number,
        social_security_number=social_security_number,
        address=address,
        phone_number=phone_number,
        score=score,
        is_activate=is_activate,
        is_valid=is_valid,
        created_at=datetime.datetime.now()
    )
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
    helper_doc1 = HelperDocument(
        **({
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
    return HelperDocument.objects

