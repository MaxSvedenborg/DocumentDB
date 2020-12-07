from Mongo.Mongo_models import Supplier


def get_all_suppliers():
    return Supplier.all()


def get_supplier_by_id(id):
    return Supplier.find(SupplierId=int(id))


def get_supplier_by_name(pattern):
    return Supplier.find(SupplierName={"$regex":pattern, "$options":"i"})


def store_changes(supplier):
    supplier.save()


def store_new_name(supplier, new_value):
    supplier.SupplierName = new_value
    supplier.save()


def store_new_address(supplier, new_value):
    supplier.SupplierAddress = new_value
    supplier.save()


def store_new_phone(supplier, new_value):
    supplier.SupplierPhone = new_value
    supplier.save()


def store_new_email(supplier, new_value):
    supplier.SupplierEmail = new_value
    supplier.save()


def store_new_supplier(supplier):
    supplier.save()


def delete_supplier(supplier):
    supplier.delete(_id=supplier._id)