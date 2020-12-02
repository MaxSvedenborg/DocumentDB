from DB import session
from Data.Models.personaldata import Personaldata


def get_all_personaldata():
    return session.query(Personaldata).all()


def get_personaldata_by_id(id):
    return session.query(Personaldata).filter(Personaldata.PersonalDataId == id).first()


def get_personaldata_by_name(pattern):
    return session.query(Personaldata).filter(Personaldata.PersonalDataName.like(f'%{pattern}%')).all()


def store_changes():
    session.commit()


def store_new_name(personaldata, new_value):
    try:
        personaldata.PersonalDataName = new_value
        session.commit()
    except:
        session.rollback()


def store_new_phone(personaldata, new_value):
    try:
        personaldata.PersonalDataPhone = new_value
        session.commit()
    except:
        session.rollback()


def store_new_email(personaldata, new_value):
    try:
        personaldata.PersonalDataEmail= new_value
        session.commit()
    except:
        session.rollback()


def store_new_personaldata(personaldata):
    try:
        session.add(personaldata)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def delete_personaldata(personaldata):
    try:
        session.delete(personaldata)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

