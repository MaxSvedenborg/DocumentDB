from Data.Models.cars import Car
from DB import session


def get_all_cars():
    return session.query(Car).all()


def get_car_by_id(id):
    return session.query(Car).filter(Car.CarsId == id).first()


def get_car_by_manufacturer(pattern):
    return session.query(Car).filter(Car.CarsManufacturer.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_regno(car, new_value):
    try:
        car.CarsRegNo = new_value
        session.commit()
    except:
        session.rollback()


def store_new_manufacturer(car, new_value):
    try:
        car.CarsManufacturer = new_value
        session.commit()
    except:
        session.rollback()


def store_new_model(car, new_value):
    try:
        car.CarsModel = new_value
        session.commit()
    except:
        session.rollback()


def store_new_color(car, new_value):
    try:
        car.CarsColor = new_value
        session.commit()
    except:
        session.rollback()


def store_new_owner(car, new_value):
    try:
        car.CustomerId = new_value
        session.commit()
    except:
        session.rollback()


def store_new_car(car):
    try:
        session.add(car)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def delete_car(car):
    try:
        session.delete(car)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
