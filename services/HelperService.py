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


def get_all_helpers():
    return HelperDocument.objects
