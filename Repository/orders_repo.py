from Data.Models.orders import Order
from DB import session


def get_all_orders():
    return session.query(Order).all()


def get_order_by_id(id):
    return session.query(Order).filter(Order.CustomerId == id).first()


def get_order_by_date(pattern):
    return session.query(Order).filter(Order.OrderDate.like(f'%{pattern}%')).all()


def store_changes():
    session.commit()


def store_new_date(order, new_value):
    try:
        order.OrderDate = new_value
        session.commit()
    except:
        session.rollback()


def store_new_time(order, new_value):
    try:
        order.OrderTime = new_value
        session.commit()
    except:
        session.rollback()


def store_new_storeId(order, new_value):
    try:
        order.StoreId = new_value
        session.commit()
    except:
        session.rollback()


def store_new_customerId(order, new_value):
    try:
        order.CustomerId = new_value
        session.commit()
    except:
        session.rollback()


def store_new_order(order):
    try:
        session.add(order)
        session.commit()
    except:
        session.rollback()


def delete_order(order):
    try:
        session.delete(order)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
