from DB import session
from Data.Models.suppliers import Supplier


def get_all_suppliers():
    return session.query(Supplier).all()


def get_supplier_by_id(id):
    return session.query(Supplier).filter(Supplier.SupplierId == id).first()


def get_supplier_by_name(pattern):
    return session.query(Supplier).filter(Supplier.SupplierName.like(f'%{pattern}%')).all()


def store_changes():
    session.commit()


def store_new_name(supplier, new_value):
    try:
        supplier.SupplierName = new_value
        session.commit()
    except:
        session.rollback()


def store_new_address(supplier, new_value):
    try:
        supplier.SupplierAddress = new_value
        session.commit()
    except:
        session.rollback()


def store_new_phone(supplier, new_value):
    try:
        supplier.SupplierPhone = new_value
        session.commit()
    except:
        session.rollback()


def store_new_email(supplier, new_value):
    try:
        supplier.SupplierEmail = new_value
        session.commit()
    except:
        session.rollback()


def store_new_supplier(supplier):
    try:
        session.add(supplier)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def delete_supplier(supplier):
    try:
        session.delete(supplier)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()