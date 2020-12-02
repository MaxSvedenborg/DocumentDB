from Data.Models.customertypes import CustomerType
from DB import session


def get_all_customer_types():
    return session.query(CustomerType).all()


def get_customertype_by_id(id):
    return session.query(CustomerType).filter(CustomerType.CustomerTypeId == id).first()


def get_customertype_by_name(pattern):
    return session.query(CustomerType).filter(CustomerType.CustomerType.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_name(customertype, new_value):
    try:
        customertype.CustomerType = new_value
        session.commit()
    except:
        session.rollback()