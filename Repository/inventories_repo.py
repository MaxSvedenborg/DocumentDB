from Mongo.Mongo_models import Inventory


def get_all_inventories():
    return Inventory.all()


def get_inventory_by_id(id):
    return Inventory.find(InventoryId=int(id))


def get_inventory_by_location(pattern):
    return Inventory.find(InventoryLocation={"$regex": pattern, "$options": "i"})


# def inventory_changes():
#     session.commit()


def store_new_inventory_location(inventory, new_value):
    inventory.InventoryLocation = new_value
    inventory.save()



def store_new_inventory_QTY(inventory, new_value):
    inventory.InventoryQTY = new_value
    inventory.save()


def store_new_inventory_automatic_order(inventory, new_value):
    # try:
    #     Inventory.InventoryQTYAutomaticOrder = new_value
    #     session.commit()
    # except:
    #     session.rollback()
    inventory.InventoryQTYAutomaticOrder = new_value
    inventory.save()



def store_new_inventory(inventory):
    inventory.save()


def delete_inventory(inventory):
    Inventory.delete(_id=inventory._id)

