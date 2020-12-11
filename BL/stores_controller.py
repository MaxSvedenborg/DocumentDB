import Repository.stores_repo as sr

from Mongo.Base_documents import NestedDocument


def get_all_stores():
    return sr.get_all_stores()


def get_store_by_id(id):
    return sr.get_store_by_id(id)


def get_store_by_name(pattern):
    stores = sr.get_store_by_name(pattern)
    return {i+1: store for i, store in enumerate(stores)}


def store_new_store_name(store, new_value):
    sr.store_new_store_name(store, new_value)


def store_new_store_address(store, new_value):
    sr.store_new_store_address(store, new_value)


def store_new_store_phone(store, new_value):
    sr.store_new_store_phone(store, new_value)


def store_new_store_email(store, new_value):
    sr.store_new_store_email(store, new_value)


def store_new_store(store):
#     _update_store_storeemployee(store, store.StoreEmployeeId)
    sr.store_new_store(store)


# def store_new_storeemployeeId(store, new_value):
#     _update_store_storeemployee(store, new_value)
#     sr.store_new_storeemployeeId(store, new_value)


def delete_store(store):
    sr.delete_store(store)


# def _update_store_storeemployee(store, storeemployeeId):
#     storeemployee = sr.get_storeemployee_by_id(storeemployeeId).first_or_none()
#     if storeemployee is not None:
#         store.StoreEmployee = NestedDocument({})
#         store.StoreEmployee.StoreEmployeeId = storeemployee.StoreEmployeeId


