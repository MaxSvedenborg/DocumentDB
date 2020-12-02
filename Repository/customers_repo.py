from Data.Models.customers import Customer
from DB import session

def get_all_customers():
    return session.query(Customer).all()


def get_customer_by_id(id):
    return session.query(Customer).filter(Customer.CustomerId == id).first()


def get_customer_by_name(pattern):
    return session.query(Customer).filter(Customer.CustomerName.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_name(customer, new_value):
    try:
        customer.CustomerName = new_value
        session.commit()
    except:
        session.rollback()


def store_new_address(customer, new_value):
    try:
        customer.CustomerAddress = new_value
        session.commit()
    except:
        session.rollback()


def store_new_phone(customer, new_value):
    try:
        customer.CustomerPhone = new_value
        session.commit()
    except:
        session.rollback()

def store_new_email(customer, new_value):
    try:
        customer.CustomerEmail = new_value
        session.commit()
    except:
        session.rollback()


def store_new_customertype(customer, new_value):
    try:
        customer.CustomerTypeId = new_value
        session.commit()
    except:
        session.rollback()

def store_new_customer(customer):
    try:
        session.add(customer)
        session.commit()
    except:
        session.rollback()

def delete_customer(customer):
    try:
        session.delete(customer)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

