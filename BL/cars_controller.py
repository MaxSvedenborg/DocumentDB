import Repository.cars_repo as c


def get_all_cars():
    return c.get_all_cars()


def get_car_by_id(id):
    return c.get_car_by_id(id)


def get_car_by_manufacturer(pattern):
    cars = c.get_car_by_manufacturer(pattern)
    return {i+1: car for i, car in enumerate(cars)}


def store_changes():
    c.store_changes()


def store_new_regno(car, new_value):
    c.store_new_regno(car, new_value)


def store_new_manufacturer(car, new_value):
    c.store_new_manufacturer(car, new_value)


def store_new_model(car, new_value):
    c.store_new_model(car, new_value)


def store_new_color(car, new_value):
    c.store_new_color(car, new_value)


def store_new_owner(car, new_value):
    c.store_new_owner(car, new_value)

def store_new_car(car):
    c.store_new_car(car)

def delete_car(car):
    c.delete_car(car)

