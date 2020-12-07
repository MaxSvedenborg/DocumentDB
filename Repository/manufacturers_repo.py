from Mongo.Mongo_models import Manufactor


def get_all_manufacturers():
    return Manufactor.all()


def get_manufacturer_by_id(id):
    return Manufactor.find(ManufactorerId=int(id))


def get_manufacturer_by_name(pattern):
    return Manufactor.find(ManufactorerName={"$regex":pattern, "$options":"i"})


def store_changes(manufactor):
    manufactor.save()


def store_new_manufacturer_name(manufacturer, new_value):
    manufacturer.ManufactorerName = new_value
    manufacturer.save()


def store_new_manufacturer_address(manufacturer, new_value):
    manufacturer.ManufacturerAddressHQ = new_value
    manufacturer.save()


def store_new_manufacturer_phone(manufacturer, new_value):
    manufacturer.ManufacturerPhoneHQ = new_value
    manufacturer.save()


def store_new_manufacturer(manufacturer):
    manufacturer.save()


def delete_manufacturer(manufacturer):
    manufacturer.delete(_id=manufacturer._id)
