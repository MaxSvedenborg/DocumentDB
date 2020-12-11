from Mongo.Mongo_models import Store


def get_all_stores():
    return Store.all()


def get_store_by_id(id):
    return Store.find(StoreId=int(id))


# def get_storeemployee_by_id(id):
#     return Store.find(StoreEmployeeId=int(id))


def get_store_by_name(pattern):
    # return session.query(Store).filter(Store.StoreName.like(f'%{pattern}%')).all()
    return Store.find(StoreName={"$regex": pattern, "$options": "i"})

# def store_changes():
#    session.commit()


def store_new_store_name(store, new_value):
    store.StoreName = new_value
    store.save()


def store_new_store_address(store, new_value):
    store.StoreAddress = new_value
    store.save()


def store_new_store_phone(store, new_value):
    store.StorePhone = new_value
    store.save()


def store_new_store_email(store, new_value):
    store.StoreEmail = new_value
    store.save()


def store_new_store(store):
    store.save()


def delete_store(store):
    Store.delete(_id=store._id)


# def store_new_storeemployeeId(store, new_value):
#     store.StoreEmployeeId = new_value
#     store.save()



