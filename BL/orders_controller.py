import Data.Repository.orders_repo as o


def get_all_orders():
    return o.get_all_orders()


def get_order_by_id(id):
    return o.get_order_by_id(id)


def get_order_by_date(pattern):
    orders = o.get_order_by_date(pattern)
    return {i+1: order for i, order in enumerate(orders)}


def store_changes():
    o.store_changes()


def store_new_date(order, new_value):
    o.store_new_date(order, new_value)


def store_new_time(order, new_value):
    o.store_new_time(order, new_value)


def store_new_storeId(order, new_value):
    o.store_new_storeId(order, new_value)


def store_new_customerId(order, new_value):
    o.store_new_customerId(order, new_value)


def store_new_order(order):
    o.store_new_order(order)


def delete_order(order):
    o.delete_order(order)
