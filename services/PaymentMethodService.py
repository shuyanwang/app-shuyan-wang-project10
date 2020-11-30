from models.PaymentMehtod import PaymentMethodDocument
from services.NeederService import *


def create_payment_method_in_db(needer_id, json):
    the_needer = get_needer_by_id(needer_id)
    if the_needer:
        json['needer_id'] = needer_id
        created_doc = PaymentMethodDocument(**json)
        created_doc.save()
        return created_doc
    else:
        raise Exception("needer does not exist in db")


def get_all_payment_methods_for_the_needer(needer_id):
    return PaymentMethodDocument.objects.filter(needer_id=needer_id)


def get_payment_method_by_payment_method_id(payment_method_id):
    return PaymentMethodDocument.objects.filter(id=payment_method_id).first()


def delete_payment_method_by_payment_method_id(payment_method_id):
    return PaymentMethodDocument.objects.filter(id=payment_method_id).first().delete()


def update_payment_method_by_payment_method_id(payment_method_id, json):
    the_doc = PaymentMethodDocument.objects.filter(id=payment_method_id).first()
    the_doc.update(**json)
    the_doc.reload()
    return the_doc


def reset_payment_methods():
    PaymentMethodDocument.drop_collection()
    all_needers = get_all_needers(None, None, None, None, None, None)
    the_needer_id = str(all_needers.first().id)
    doc1 = PaymentMethodDocument(
        needer_id=the_needer_id,
        bank_name="Wells Fargo",
        card_type="Credit",
        card_number="1234123412341234",
        expired_at="09/23",
        security_code="123",
    )
    doc2 = PaymentMethodDocument(
        needer_id=the_needer_id,
        bank_name="Wells Fargo",
        card_type="Debit",
        card_number="2234223422342234",
        expired_at="11/25",
        security_code="111",
    )
    doc1.save()
    doc2.save()
    return PaymentMethodDocument.objects
