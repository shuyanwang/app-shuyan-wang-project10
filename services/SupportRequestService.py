from models.SupportRequest import SupportRequestDocument
import datetime


def create_support_request_in_db(json):
    created_doc = SupportRequestDocument(**json)
    created_doc.save()
    return created_doc


def update_support_request(request_id: str, json):
    the_request = SupportRequestDocument.objects.filter(id=request_id).first()
    the_request.update(**json)
    the_request.reload()
    return the_request


def delete_support_request(request_id: str):
    SupportRequestDocument.objects.filter(id=request_id).first().delete()


def get_support_request_by_id(request_id):
    return SupportRequestDocument.objects.filter(id=request_id).first()


def get_all_support_requests(filter_by, filter_value, sort_by, sort_order, page_size, page):
    objects = SupportRequestDocument.objects

    if filter_by and filter_value:
        objects = objects.filter(**{filter_by: filter_value})

    if sort_by:
        order = '+' if sort_order == 'asc' else '-'
        objects = objects.order_by(order + sort_by)

    if page_size and page:
        start_index = (int(page) - 1) * int(page_size)
        objects = objects[start_index: start_index + int(page_size)]

    return objects


def reset_support_requests():
    SupportRequestDocument.drop_collection()
    doc1 = SupportRequestDocument(
        **({
            "type": "IT Support",
            "city": "Sunnyvale",
            "contact_number": "6501111111",
            "note": "cannot accept request",
            "progress": [
                {
                    "status": "pending",
                    "created_at": datetime.datetime.fromtimestamp(1606593299246 / 1e3)
                },
                {
                    "status": "in progress",
                    "created_at": datetime.datetime.fromtimestamp(1606593399246 / 1e3)
                },
                {
                    "status": "done",
                    "created_at": datetime.datetime.fromtimestamp(1606593499246 / 1e3)
                }
            ]
        })
    )
    doc1.save()
    return SupportRequestDocument.objects
