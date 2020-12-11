import Repository.orders_repo as o
import Repository.customers_repo as c
from Mongo.Base_documents import NestedDocument


def get_all_orders():
    return o.get_all_orders()


def get_order_by_id(id):
    return o.get_order_by_id(id)


def get_order_by_date(pattern):
    orders = o.get_order_by_date(pattern)
    return {i+1: order for i, order in enumerate(orders)}


def store_new_date(order, new_value):
    o.store_new_date(order, new_value)


def store_new_time(order, new_value):
    o.store_new_time(order, new_value)


def store_new_storeId(order, new_value):
    o.store_new_storeId(order, new_value)


def store_new_customerId(order, new_value):
    _update_order_customer(order, new_value)
    o.store_new_customerId(order, new_value)


def store_new_order(order):
    _update_order_customer(order, order.CustomerId)
    o.store_new_order(order)


def delete_order(order):
    o.delete_order(order)


def _update_order_customer(order, customerId):
    customer = c.get_customer_by_id(customerId).first_or_none()
    if customer is not None:
        order.Customer = NestedDocument({})
        order.Customer.CustomerEmail = customer.CustomerEmail
        order.Customer.CustomerAddress = customer.CustomerAddress
        order.Customer.CustomerName = customer.CustomerName
        order.Customer.CustomerTypeId = customer.CustomerType.CustomerTypeId
        order.Customer.CustomerPhone = customer.CustomerPhone
        order.Customer.CustomerId = customer.CustomerId
