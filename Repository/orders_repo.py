from Mongo.Mongo_models import Order


def get_all_orders():
    return Order.all()


def get_order_by_id(id):
    return Order.find(OrderId=int(id))


def get_order_by_date(pattern):
    return Order.find(OrderDate={"$regex":pattern, "$options":"i"})


def store_new_date(order, new_value):
    order.OrderDate = new_value
    order.save()


def store_new_time(order, new_value):
    order.OrderTime = new_value
    order.save()


def store_new_storeId(order, new_value):
    order.StoreId = new_value
    order.save()


def store_new_customerId(order, new_value):
    order.CustomerId = new_value
    order.save()


def store_new_order(order):
    order.save()


def delete_order(order):
    Order.delete(_id=order._id)
