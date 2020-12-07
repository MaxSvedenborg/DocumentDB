from Mongo.Mongo_models import Sparepart


def get_all_spareparts():
    return Sparepart.all()


def get_sparepart_by_id(id):
    return Sparepart.find(SparepartId=int(id))


def get_sparepart_by_name(pattern):
    return Sparepart.find(SparepartName={"$regex":pattern, "$options":"i"})


def store_changes(spareparts):
   spareparts.save()


def store_new_sparepart_name(sparepart, new_value):
    sparepart.SparepartName = new_value
    sparepart.save()


def store_new_sparepart_description(sparepart, new_value):
    sparepart.SparepartDescription = new_value
    sparepart.save()


def store_new_sparepart(sparepart):
    sparepart.save()


def delete_sparepart(sparepart):
    sparepart.delete(_id=sparepart._id)