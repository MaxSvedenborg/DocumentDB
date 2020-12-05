import Repository.customers_repo as cr
from Mongo.Base_documents import NestedDocument


def get_all_customers():
    return cr.get_all_customers()


def get_customer_by_id(id):
    return cr.get_customer_by_id(id)


def get_customer_by_name(pattern):
    customers = cr.get_customer_by_name(pattern)
    return {i+1: customer for i, customer in enumerate(customers)}


def store_new_name(customer, new_value):
    cr.store_new_name(customer, new_value)


def store_new_address(customer, new_value):
    cr.store_new_address(customer, new_value)


def store_new_phone(customer, new_value):
    cr.store_new_phone(customer, new_value)


def store_new_email(customer, new_value):
    cr.store_new_email(customer, new_value)


def store_new_customertype(customer, new_value):
    if int(new_value) == 1:
        cr.store_new_customertype(customer, _get_customer_type(new_value))
    elif int(new_value) == 2:
        cr.store_new_customertype(customer, _get_customer_type())


def store_new_customer(customer):
    customer.CustomerType = _get_customer_type(customer.CustomerTypeId)
    del customer.__dict__["CustomerTypeId"]
    cr.store_new_customer(customer)


def delete_customer(customer):
    cr.delete_customer(customer)


def _get_customer_type(CustomerTypeId):
    if int(CustomerTypeId) == 1:
        return NestedDocument({"CustomerTypeId": 1, "CustomerType": "Company"})
    elif int(CustomerTypeId) == 2:
        return NestedDocument({"CustomerTypeId": 2, "CustomerType": "Private"})

