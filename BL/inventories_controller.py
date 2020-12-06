import Data.Repository.inventories_repo as ir


def get_all_inventories():
    return ir.get_all_inventories()


def get_inventory_by_id(id):
    return ir.get_inventory_by_id(id)


def get_inventory_by_location(pattern):
    inventories = ir.get_inventory_by_location(pattern)
    return {i+1: inventory for i, inventory in enumerate(inventories)}


def inventory_changes():
    ir.inventory_changes()


def store_new_inventory_location(inventory, new_value):
    ir.store_new_inventory_location(inventory, new_value)


def store_new_inventory_QTY(inventory, new_value):
    ir.store_new_inventory_QTY(inventory, new_value)


def store_new_inventory_automatic_order(inventory, new_value):
    ir.store_new_inventory_automatic_order(inventory, new_value)


def store_new_inventory(Inventory):
    ir.store_new_inventory(Inventory)


def delete_inventory(Inventory):
    ir.delete_inventory(Inventory)