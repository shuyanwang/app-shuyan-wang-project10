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


# return all active needers
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


def reset_needers():
    NeederDocument.drop_collection()
    doc1 = NeederDocument(
        **({
            "first_name": "Matt",
            "last_name": "Smith",
            "cities": ["San Francisco", "Sunnyvale", "Mountain View"],
            "social_security_number": "123121234",
            "phone_number": "4081111111",
            "score": 4.8,
            "is_activate": True
        })
    )
    doc2 = NeederDocument(
        **({
            "first_name": "Jessica",
            "last_name": "Smith",
            "cities": ["San Jose"],
            "social_security_number": "223232223",
            "phone_number": "4082222222",
            "score": 4,
            "is_activate": True
        })
    )
    doc3 = NeederDocument(
        **({
            "first_name": "Tim",
            "last_name": "Smith",
            "cities": ["Sunnyvale", "Mountain View"],
            "social_security_number": "334343334",
            "phone_number": "4083333333",
            "score": 4.5,
            "is_activate": True
        })
    )
    doc1.save()
    doc2.save()
    doc3.save()
    return NeederDocument.objects
