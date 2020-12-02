from BL.inventories_controller import get_all_inventories, get_inventory_by_id, store_new_inventory_location, \
    store_new_inventory_QTY, store_new_inventory_automatic_order, store_new_inventory, delete_inventory, \
    get_inventory_by_location

from Data.Models.inventories import Inventory


def inventories_menu():
    while True:
        print("===========================")
        print("Inventory Menu")
        print("===========================")
        print("1. View All Inventories")
        print("2. View Inventories by Id")
        print("3. Find and Update Inventories")
        print("4. Create new Inventories into the system")
        print("5. Delete Inventories from the system")
        print("6. Exit Inventories Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            inventories = get_all_inventories()
            for inventory in inventories:
                print(inventory)

        elif selection == "2":
            id = input("Enter Inventory Id: ")
            inventory = get_inventory_by_id(id)
            if inventory:
                print(inventory)
            else:
                print("Could not find inventory with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial name of the inventory: ")
            inventories = get_inventory_by_location(pattern)
            if len(inventories) > 0:
                for key, inventory in inventories.items():
                    print(f'{key}. {inventory}')

                edit_choice = input("Would you like to edit inventory information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for inventory to edit: ")
                    edit_selection = int(edit_selection)

                    inventory = inventories[edit_selection]
                    print(f'1. Inventory location: {inventory.InventoryLocation}')
                    print(f'2. Inventory Amount: {inventory.InventoryQTY}')
                    print(f'3. Inventory Automatic order amount: {inventory.InventoryQTYAutomaticOrder}')


                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Inventory Location: ")
                        store_new_inventory_location(inventory, new_value)
                        print("Sucessfully updated new inventory location")
                    elif line == "2":
                        new_value = input("Enter new inventory Amount: ")
                        store_new_inventory_QTY(inventory, new_value)
                        print("Sucessfully updated new inventory amount")
                    elif line == "3":
                        new_value = input("Enter new amount for automatic order: ")
                        store_new_inventory_automatic_order(inventory, new_value)
                        print("Sucessfully updated new amount for automatic orders")

            else:
                print("No Inventory found")

        elif selection == "4":
            edit_choice = input("Opps! SparepartId and StoreId information needed, do you have them? [y/n]: ")
            if (edit_choice.lower() == "y"):
                inventory = Inventory()
                inventory.InventoryLocation = input("Enter InventoryLocation: ")
                inventory.InventoryQTY = input("Enter Inventory Amount (number only): ")
                inventory.InventoryCriticalLevel = input("Enter Inventory Critical Level (number only): ")
                inventory.InventoryQTYAutomaticOrder = input("Enter Inventory automatic order amount (number only): ")
                inventory.InventoryETA = input("Enter Inventory Estimate Time of Arrival: ")
                inventory.StoreId = input("Enter StoreId: ")
                inventory.SparepartId = input("Enter SparepartId: ")
                store_new_inventory(inventory)
                print("Sucessfully created new inventory")

        elif selection == "5":
            pattern = input("Enter full or partial inventory location: ")
            inventories = get_inventory_by_location(pattern)
            if len(inventories) > 0:
                for key, inventory in inventories.items():
                    print(f'{key}. {inventory}')

                delete_selection = input("Enter number for inventory to delete: ")
                delete_selection = int(delete_selection)

                inventory = inventories[delete_selection]
                delete_inventory(inventory)
                print("Sucessfully deleted inventory")

        else:
            break