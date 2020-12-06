import Data.Repository.stores_repo as sr


def get_all_stores():
    return sr.get_all_stores()


def get_store_by_id(id):
    return sr.get_store_by_id(id)


def get_store_by_name(pattern):
    stores = sr.get_store_by_name(pattern)
    return {i+1: store for i, store in enumerate(stores)}


def store_changes():
    sr.store_changes()


def store_new_store_name(store, new_value):
    sr.store_new_store_name(store, new_value)


def store_new_store_address(store, new_value):
    sr.store_new_store_address(store, new_value)


def store_new_store_phone(store, new_value):
    sr.store_new_store_phone(store, new_value)


def store_new_store_email(store, new_value):
    sr.store_new_store_email(store, new_value)


def store_new_store(store):
    sr.store_new_store(store)


def delete_store(store):
    sr.delete_store(store)

