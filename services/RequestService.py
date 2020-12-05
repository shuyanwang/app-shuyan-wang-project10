from models.Request import RequestDocument
from services.NeederService import *
from services.HelperService import *
import datetime


def create_request_in_db(needer_id, json) -> RequestDocument:
    the_needer = get_needer_by_id(needer_id)
    if the_needer:
        json['needer_id'] = needer_id
        if 'pick_up_time' in json:
            json['pick_up_time'] = datetime.datetime.fromtimestamp(json['pick_up_time'] / 1e3)
        if 'drop_off_time' in json:
            json['drop_off_time'] = datetime.datetime.fromtimestamp(json['drop_off_time'] / 1e3)
        created_doc = RequestDocument(**json)
        created_doc.save()
        return created_doc
    else:
        raise Exception("needer does not exist in db")


def update_request(request_id: str, json):
    the_request = RequestDocument.objects.filter(id=request_id).first()
    if 'pick_up_time' in json:
        json['pick_up_time'] = datetime.datetime.fromtimestamp(json['pick_up_time'] / 1e3)
    if 'drop_off_time' in json:
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


def get_all_requests_for_the_helper(helper_id):
    return RequestDocument.objects.filter(helper_id=helper_id)


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


def reset_requests():
    RequestDocument.drop_collection()
    all_needers = get_all_needers(None, None, None, None, None, None)
    the_needer_id1 = str(all_needers.first().id)
    the_needer_id2 = str(all_needers[1].id)
    all_helpers = get_all_helpers(None, None, None, None, None, None)
    the_helper_id1 = str(all_helpers.first().id)
    the_helper_id2 = str(all_helpers[1].id)
    doc1 = create_request_in_db(
        the_needer_id1,
        {
            "items": [
                {
                    "item_name": "fish",
                    "item_type": "food",
                    "size": "big"
                },
                {
                    "item_name": "mac book",
                    "item_type": "electronics",
                    "size": "medium"
                }
            ],
            "request_priority": "urgent",
            "pick_up_time": 1606603129447,
            "pick_up_location": [120.1, 30.003],
            "drop_off_time": 1606603139447,
            "drop_off_location": [120.34, 30.1],
            "reward": 10.3,
            "note": "please be careful",
            "status": "delivered",
            "helper_id": the_helper_id1,
            "correspondence_number": "650-111-1111",
            "tip": None
        }
    )
    doc2 = create_request_in_db(
        the_needer_id2,
        {
            "items": [
                {
                    "item_name": "fruit",
                    "item_type": "food",
                    "size": "small"
                },
                {
                    "item_name": "shirt",
                    "item_type": "clothing",
                    "size": "small"
                }
            ],
            "request_priority": "urgent",
            "pick_up_time": 1606603329447,
            "pick_up_location": [110.1, 20.003],
            "drop_off_time": 1606604239447,
            "drop_off_location": [110.34, 20.1],
            "reward": 12,
            "note": "please be careful",
            "helper_id": the_helper_id1,
            "status": "delivered",
            "correspondence_number": "650-111-1111",
            "tip": None
        }
    )
    doc3 = create_request_in_db(
        the_needer_id1,
        {
            "items": [
                {
                    "item_name": "fruit",
                    "item_type": "food",
                    "size": "big"
                }
            ],
            "request_priority": "urgent",
            "pick_up_time": 1606603329447,
            "pick_up_location": [110.1, 40.003],
            "drop_off_time": 1606604239447,
            "drop_off_location": [110.34, 40.1],
            "reward": 20,
            "note": "please be careful",
            "status": "delivered",
            "helper_id": the_helper_id2,
            "correspondence_number": "650-111-1111",
            "tip": None
        }
    )
    doc4 = create_request_in_db(
        the_needer_id1,
        {
            "items": [
                {
                    "item_name": "snacks",
                    "item_type": "food",
                    "size": "medium"
                }
            ],
            "request_priority": "low",
            "pick_up_time": 1606603329447,
            "pick_up_location": [110.1, 40.003],
            "drop_off_time": 1606604239447,
            "drop_off_location": [110.34, 40.1],
            "reward": 8.3,
            "note": "please be careful",
            "status": "waiting for pick up",
            "correspondence_number": "650-111-1111",
            "tip": None
        }
    )
    doc1.save()
    doc2.save()
    doc3.save()
    doc4.save()
    return RequestDocument.objects
