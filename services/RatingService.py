from models.Rating import RatingDocument
from services.NeederService import *
from services.RequestService import *
from services.HelperService import *

from statistics import mean


def create_rating_in_db(request_id, from_needer_to_helper, json):
    the_request = get_request_by_id(request_id)
    if the_request:
        if the_request.helper_id:
            return create_rating_in_db_helper(
                the_request.helper_id, the_request.needer_id, request_id, from_needer_to_helper, json)
        else:
            raise Exception('the request does not have helper_id')
    else:
        raise Exception('the request does not exist')


def create_rating_in_db_helper(helper_id, needer_id, request_id, from_needer_to_helper, json):
    the_helper = get_helper_by_id(helper_id)
    if the_helper:
        the_needer = get_needer_by_id(needer_id)
        if the_needer:
            json['rating_from'] = needer_id if from_needer_to_helper else helper_id
            json['rating_to'] = helper_id if from_needer_to_helper else needer_id
            json['request_id'] = request_id
            created_doc = RatingDocument(**json)
            created_doc.save()
            if from_needer_to_helper:
                update_score_for_the_helper(helper_id)
            else:
                update_score_for_the_needer(needer_id)
            return created_doc
        else:
            raise Exception('the needer does not exit')
    else:
        raise Exception('the helper does not exit')


def update_score_for_the_helper(helper_id):
    all_ratings = RatingDocument.objects.filter(rating_to=helper_id)
    avg_score = None if len(all_ratings) == 0 else mean([rating['score'] for rating in all_ratings])
    the_helper = get_helper_by_id(helper_id)
    the_helper.update(score=avg_score)


def update_score_for_the_needer(needer_id):
    all_ratings = RatingDocument.objects.filter(rating_to=needer_id)
    avg_score = None if len(all_ratings) == 0 else mean([rating['score'] for rating in all_ratings])
    the_needer = get_needer_by_id(needer_id)
    the_needer.update(score=avg_score)


def get_all_ratings(filter_by, filter_value, sort_by, sort_order, page_size, page):
    objects = RatingDocument.objects

    if filter_by and filter_value:
        objects = objects.filter(**{filter_by: filter_value})

    if sort_by:
        order = '+' if sort_order == 'asc' else '-'
        objects = objects.order_by(order + sort_by)

    if page_size and page:
        start_index = (int(page) - 1) * int(page_size)
        objects = objects[start_index: start_index + int(page_size)]

    return objects


def get_ratings_to_the_helper(helper_id):
    return RatingDocument.objects(rating_to=helper_id)


def get_ratings_to_the_needer(needer_id):
    return RatingDocument.objects(rating_to=needer_id)


def get_rating_by_id(rating_id):
    return RatingDocument.objects(id=rating_id).first()


def update_rating(rating_id: str, json):
    the_rating = RatingDocument.objects.filter(id=rating_id).first()
    the_rating.update(**json)
    if the_rating.from_needer_to_helper:
        update_score_for_the_helper(the_rating.rating_to)
    else:
        update_score_for_the_needer(the_rating.rating_to)
    the_rating.reload()
    return the_rating


def delete_rating(rating_id: str):
    the_rating = RatingDocument.objects.filter(id=rating_id).first()
    from_needer_to_helper = the_rating.from_needer_to_helper
    rating_to = the_rating.rating_to
    the_rating.delete()
    if from_needer_to_helper:
        update_score_for_the_helper(rating_to)
    else:
        update_score_for_the_needer(rating_to)


def reset_ratings():
    RatingDocument.drop_collection()
    all_requests = get_all_requests('status', 'delivered', None, None, None, None)
    the_request_id1 = str(all_requests.first().id)
    the_request_id2 = str(all_requests[1].id)
    the_request_id3 = str(all_requests[2].id)
    doc1 = create_rating_in_db(
        the_request_id1,
        True,
        {
            "score": 5,
            "comment": "The helper is very good!",
            "from_needer_to_helper": True
        }
    )
    doc2 = create_rating_in_db(
        the_request_id2,
        True,
        {
            "score": 4,
            "comment": "The helper is good!",
            "from_needer_to_helper": True
        }
    )
    doc3 = create_rating_in_db(
        the_request_id3,
        True,
        {
            "score": 4.75,
            "comment": "The helper is on time!",
            "from_needer_to_helper": True
        }
    )
    doc1.save()
    doc2.save()
    doc3.save()
    return RatingDocument.objects
