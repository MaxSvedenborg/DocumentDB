from Mongo.Mongo_models import Customer


def get_all_customers():
    return Customer.all()


def get_customer_by_id(id):
    return Customer.find(CustomerId=int(id))


def get_customer_by_name(pattern):
    return Customer.find(CustomerName={"$regex":pattern, "$options":"i"})


def store_new_name(customer, new_value):
    customer.CustomerName = new_value
    customer.save()


def store_new_address(customer, new_value):
    customer.CustomerAddress = new_value
    customer.save()


def store_new_phone(customer, new_value):
    customer.CustomerPhone = new_value
    customer.save()


def store_new_email(customer, new_value):
    customer.CustomerEmail = new_value
    customer.save()


def store_new_customertype(customer, new_value):
    customer.CustomerType = new_value
    customer.save()


def store_new_customer(customer):
    customer.save()


def delete_customer(customer):
    Customer.delete(_id=customer._id)


def get_storeemployee_by_id(storeemployeeId):
    return None