from Data.Models.stores import Store
from DB import session


def get_all_stores():
    return session.query(Store).all()


def get_store_by_id(id):
    return session.query(Store).filter(Store.StoreId == id).first()


def get_store_by_name(pattern):
    return session.query(Store).filter(Store.StoreName.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_store_name(store, new_value):
    try:
        store.StoreName = new_value
        session.commit()
    except:
        session.rollback()


def store_new_store_address(store, new_value):
    try:
        store.StoreAddress = new_value
        session.commit()
    except:
        session.rollback()


def store_new_store_phone(store, new_value):
    try:
        store.StorePhone = new_value
        session.commit()
    except:
        session.rollback()


def store_new_store_email(store, new_value):
    try:
        store.StoreEmail = new_value
        session.commit()
    except:
        session.rollback()


def store_new_store(store):
    try:
        session.add(store)
        session.commit()
    except:
        session.rollback()


def delete_store(store):
    try:
        session.delete(store)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()