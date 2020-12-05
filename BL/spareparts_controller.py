import Data.Repository.spareparts_repo as spr


def get_all_spareparts():
    return spr.get_all_spareparts()


def get_sparepart_by_id(id):
    return spr.get_sparepart_by_id(id)


def get_sparepart_by_name(pattern):
    spareparts = spr.get_sparepart_by_name(pattern)
    return {i+1: Sparepart for i, Sparepart in enumerate(spareparts)}


def sparepart_changes():
    spr.sparepart_changes()


def store_new_sparepart_name(Sparepart, new_value):
    spr.store_new_sparepart_name(Sparepart, new_value)


def store_new_sparepart_description(Sparepart, new_value):
    spr.store_new_sparepart_description(Sparepart, new_value)


def store_new_sparepart(Sparepart):
    spr.store_new_sparepart(Sparepart)


def delete_sparepart(Sparepart):
    spr.delete_sparepart(Sparepart)

