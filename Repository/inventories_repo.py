from Data.Models.inventories import Inventory
from DB import session


def get_all_inventories():
    return session.query(Inventory).all()


def get_inventory_by_id(id):
    return session.query(Inventory).filter(Inventory.InventoryId == id).first()


def get_inventory_by_location(pattern):
    return session.query(Inventory).filter(Inventory.InventoryLocation.like(f'%{pattern}%')).all()


def inventory_changes():
    session.commit()


def store_new_inventory_location(Inventory, new_value):
    try:
        Inventory.InventoryLocation = new_value
        session.commit()
    except:
        session.rollback()


def store_new_inventory_QTY(Inventory, new_value):
    try:
        Inventory.InventoryQTY = new_value
        session.commit()
    except:
        session.rollback()


def store_new_inventory_automatic_order(Inventory, new_value):
    try:
        Inventory.InventoryQTYAutomaticOrder = new_value
        session.commit()
    except:
        session.rollback()


def store_new_inventory(Inventory):
    try:
        session.add(Inventory)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def delete_inventory(Inventory):
    try:
        session.delete(Inventory)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

