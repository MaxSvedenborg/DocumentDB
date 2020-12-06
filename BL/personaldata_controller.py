import Data.Repository.personaldata_repo as pr


def get_all_personaldata():
    return pr.get_all_personaldata()


def get_personaldata_by_id(id):
    return pr.get_personaldata_by_id(id)


def get_personaldata_by_name(pattern):
    personaldata = pr.get_personaldata_by_name(pattern)
    return {i+1: customer for i, customer in enumerate(personaldata)}


def store_changes():
    pr.store_changes()


def store_new_name(personaldata, new_value):
    pr.store_new_name(personaldata, new_value)


def store_new_phone(personaldata, new_value):
    pr.store_new_phone(personaldata, new_value)


def store_new_email(personaldata, new_value):
    pr.store_new_email(personaldata, new_value)


def store_new_personaldata(personaldata):
    pr.store_new_personaldata(personaldata)


def delete_personaldata(personaldata):
    pr.delete_personaldata(personaldata)
