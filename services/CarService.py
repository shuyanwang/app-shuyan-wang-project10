from models.Car import CarDocument
from services.HelperService import *


def create_car_in_db(helper_id, json):
    the_helper = get_helper_by_id(helper_id)
    if the_helper:
        json['helper_id'] = helper_id
        created_doc = CarDocument(**json)
        created_doc.save()
        return created_doc
    else:
        raise Exception("helper does not exist in db")


def get_all_cars_for_the_helper(helper_id):
    return CarDocument.objects.filter(helper_id=helper_id)


def get_car_by_car_id(car_id):
    return CarDocument.objects.filter(id=car_id).first()


def delete_car_by_car_id(car_id):
    return CarDocument.objects.filter(id=car_id).first().delete()


def reset_cars():
    CarDocument.drop_collection()
    all_helpers = get_all_helpers(None, None, None, None, None, None)
    the_helper_id = str(all_helpers.first().id)
    doc1 = CarDocument(helper_id=the_helper_id, plate="AB12345", state="CA")
    doc2 = CarDocument(helper_id=the_helper_id, plate="BB12345", state="NY")
    doc1.save()
    doc2.save()
    return CarDocument.objects
