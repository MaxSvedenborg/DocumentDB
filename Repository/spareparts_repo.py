from Data.Models.spareparts import Sparepart
from DB import session


def get_all_spareparts():
    return session.query(Sparepart).all()


def get_sparepart_by_id(id):
    return session.query(Sparepart).filter(Sparepart.SparepartId == id).first()


def get_sparepart_by_name(pattern):
    return session.query(Sparepart).filter(Sparepart.SparepartName.like(f'%{pattern}%')).all()


def sparepart_changes():
   session.commit()


def store_new_sparepart_name(Sparepart, new_value):
    try:
        Sparepart.SparepartName = new_value
        session.commit()
    except:
        session.rollback()


def store_new_sparepart_description(Sparepart, new_value):
    try:
        Sparepart.SparepartDescription = new_value
        session.commit()
    except:
        session.rollback()


def store_new_sparepart(Sparepart):
    try:
        session.add(Sparepart)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def delete_sparepart(Sparepart):
    try:
        session.delete(Sparepart)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()