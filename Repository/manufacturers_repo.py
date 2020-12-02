from Data.Models.manufacturers import Manufacturer
from DB import session

def get_all_manufacturers():
    return session.query(Manufacturer).all()

def get_manufacturer_by_id(id):
    return session.query(Manufacturer).filter(Manufacturer.ManufacturerId == id).first()

def get_manufacturer_by_name(pattern):
    return session.query(Manufacturer).filter(Manufacturer.ManufacturerName.like(f'%{pattern}%')).all()

def store_changes():
   session.commit()

def store_new_manufacturer_name(manufacturer, new_value):
    try:
        manufacturer.ManufacturerName = new_value
        session.commit()
    except:
        session.rollback()

def store_new_manufacturer_address(manufacturer, new_value):
    try:
        manufacturer.ManufacturerAddressHQ = new_value
        session.commit()
    except:
        session.rollback()


def store_new_manufacturer_phone(manufacturer, new_value):
    try:
        manufacturer.ManufacturerPhoneHQ = new_value
        session.commit()
    except:
        session.rollback()


def store_new_manufacturer(manufacturer):
    try:
        session.add(manufacturer)
        session.commit()
    except:
        session.rollback()


def delete_manufacturer(manufacturer):
    try:
        session.delete(manufacturer)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

