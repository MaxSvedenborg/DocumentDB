import Data.Repository.manufacturers_repo as mr
import Data.Repository.personaldata_repo as pr

def get_all_manufacturers():
    return mr.get_all_manufacturers()


def get_manufacturer_by_id(id):
    return mr.get_manufacturer_by_id(id)


def get_manufacturer_by_name(pattern):
    manufacturers = mr.get_manufacturer_by_name(pattern)
    return {i+1: manufacturer for i, manufacturer in enumerate(manufacturers)}


def store_changes():
    mr.store_changes()


def store_new_manufacturer_name(manufacturer, new_value):
    mr.store_new_manufacturer_name(manufacturer, new_value)


def store_new_manufacturer_address(manufacturer, new_value):
    mr.store_new_manufacturer_address(manufacturer, new_value)


def store_new_manufacturer_phone(manufacturer, new_value):
    mr.store_new_manufacturer_phone(manufacturer, new_value)


def store_new_personaldata(personaldata):
    pr.store_new_personaldata(personaldata)


def store_new_manufacturer(manufacturer):
    mr.store_new_manufacturer(manufacturer)


def delete_manufacturer(manufacturer):
    mr.delete_manufacturer(manufacturer)
