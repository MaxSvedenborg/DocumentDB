import Data.Repository.customertypes_repo as ct

def get_all_customertypes():
    return ct.get_all_customertypes()


def get_customertype_by_id(id):
    return ct.get_customertype_by_id(id)


def get_customertype_by_name(pattern):
    customertypes = ct.get_customertype_by_name(pattern)
    return {i+1: customertype for i, customertype in enumerate(customertypes)}


def store_changes():
    ct.store_changes()


def store_new_name(customertype, new_value):
    ct.store_new_name(customertype, new_value)

