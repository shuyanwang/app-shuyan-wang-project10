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
