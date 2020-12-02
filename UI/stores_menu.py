from BL.stores_controller import get_all_stores, get_store_by_id, get_store_by_name, store_new_store_name, store_new_store_address, store_new_store_phone, \
    store_new_store_email, store_new_store, delete_store
from Data.Models.stores import Store


def stores_menu():
    while True:
        print("===========================")
        print("Stores Menu")
        print("===========================")
        print("1. View All Stores")
        print("2. View Stores by Id")
        print("3. Find and Update Stores")
        print("4. Create new Store into the system")
        print("5. Delete Store from the system")
        print("6. Exit Store Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            stores = get_all_stores()
            for store in stores:
                print(store)

        elif selection == "2":
            id = input("Enter Store Id: ")
            store = get_store_by_id(id)
            if store:
                print(store)
            else:
                print("Could not find store with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial store name: ")
            stores = get_store_by_name(pattern)
            if len(stores) > 0:
                for key, store in stores.items():
                    print(f'{key}. {store}')

                edit_choice = input("Would you like to edit store information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for store to edit: ")
                    edit_selection = int(edit_selection)

                    store = stores[edit_selection]
                    print(f'1. Store Name: {store.StoreName}')
                    print(f'2. Store Address: {store.StoreAddress}')
                    print(f'3. Store Phone: {store.StorePhone}')
                    print(f'4. Store Email: {store.StoreEmail}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Store Name: ")
                        store_new_store_name(store, new_value)
                        print("Sucessfully updated new Store Name")
                    elif line == "2":
                        new_value = input("Enter new Store Address: ")
                        store_new_store_address(store, new_value)
                        print("Sucessfully updated new Store Address")
                    elif line == "3":
                        new_value = input("Enter new Store Phone: ")
                        store_new_store_phone(store, new_value)
                        print("Sucessfully updated new Store Phone")
                    elif line == "4":
                        new_value = input("Enter new Store Email: ")
                        store_new_store_email(store, new_value)
                        print("Sucessfully updated new Store Phone")

            else:
                print("No store found")

        elif selection == "4":
            store = Store()
            store.StoreName = input("Enter Store Name: ")
            store.StoreAddress = input("Enter Store Address: ")
            store.StorePhone = input("Enter Store Phone Number: ")
            store.StoreEmail = input("Enter store email: ")
            store_new_store(store)
            print("Sucessfully created new store")

        elif selection == "5":
            pattern = input("Enter full or partial store name: ")
            stores = get_store_by_name(pattern)
            if len(stores) > 0:
                for key, store in stores.items():
                    print(f'{key}. {store}')

                delete_selection = input("Enter number for store to delete: ")
                delete_selection = int(delete_selection)

                store = stores[delete_selection]
                delete_store(store)
                print("Sucessfully deleted store")

        else:
            break