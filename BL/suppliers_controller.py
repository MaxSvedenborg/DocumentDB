import Data.Repository.suppliers_repo as sr


def get_all_suppliers():
    return sr.get_all_suppliers()


def get_supplier_by_id(id):
    return sr.get_supplier_by_id(id)


def get_supplier_by_name(pattern):
    suppliers = sr.get_supplier_by_name(pattern)
    return {i+1: supplier for i, supplier in enumerate(suppliers)}


def store_changes():
    sr.store_changes()


def store_new_name(supplier, new_value):
    sr.store_new_name(supplier, new_value)


def store_new_address(supplier, new_value):
    sr.store_new_address(supplier, new_value)


def store_new_phone(supplier, new_value):
    sr.store_new_phone(supplier, new_value)


def store_new_email(supplier, new_value):
    sr.store_new_email(supplier, new_value)


def store_new_supplier(supplier):
    sr.store_new_supplier(supplier)


def delete_supplier(supplier):
    sr.delete_supplier(supplier)
