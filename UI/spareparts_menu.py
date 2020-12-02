from BL.spareparts_controller import get_all_spareparts, get_sparepart_by_id, get_sparepart_by_name, \
    store_new_sparepart_name, store_new_sparepart_description, store_new_sparepart, delete_sparepart
from Data.Models.spareparts import Sparepart


def spareparts_menu():
    while True:
        print("===========================")
        print("Spareparts Menu")
        print("===========================")
        print("1. View All Spareparts")
        print("2. View Spareparts by Id")
        print("3. Find and Update Spareparts")
        print("4. Create new Sparepart into the system")
        print("5. Delete Sparepart from the system")
        print("6. Exit Sparepart Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            spareparts = get_all_spareparts()
            for sparepart in spareparts:
                print(sparepart)

        elif selection == "2":
            id = input("Enter Sparepart Id: ")
            sparepart = get_sparepart_by_id(id)
            if sparepart:
                print(sparepart)
            else:
                print("Could not find sparepart with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial name of the sparepart: ")
            spareparts = get_sparepart_by_name(pattern)
            if len(spareparts) > 0:
                for key, sparepart in spareparts.items():
                    print(f'{key}. {sparepart}')

                edit_choice = input("Would you like to edit sparepart information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for sparepart to edit: ")
                    edit_selection = int(edit_selection)

                    sparepart = spareparts[edit_selection]
                    print(f'1. Sparepart Name: {sparepart.SparepartName}')
                    print(f'2. Sparepart Description: {sparepart.SparepartDescription}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Sparepart Name: ")
                        store_new_sparepart_name(sparepart, new_value)
                        print("Sucessfully updated new Sparepart Name")
                    elif line == "2":
                        new_value = input("Enter new Sparepart description: ")
                        store_new_sparepart_description(sparepart, new_value)
                        print("Sucessfully updated new sparepart description")

            else:
                print("No sparepart found")


        elif selection == "4":
            edit_choice = input("Opps! SupplierId and ManufacturerId information needed, do you have them? [y/n]: ")
            if (edit_choice.lower() == "y"):
                sparepart = Sparepart()
                sparepart.SparepartName = input("Enter Sparepart Name: ")
                sparepart.SparepartDescription = input("Enter Sparepart description: ")
                sparepart.ManufacturerId = input("Enter Manufacturer Id: ")
                sparepart.SupplierId = input("Enter Supplier Id: ")
                store_new_sparepart(sparepart)
                print("Sucessfully created new sparepart")

        elif selection == "5":
            pattern = input("Enter full or partial sparepart name: ")
            spareparts = get_sparepart_by_name(pattern)
            if len(spareparts) > 0:
                for key, sparepart in spareparts.items():
                    print(f'{key}. {sparepart}')

                delete_selection = input("Enter number for spareparts to delete: ")
                delete_selection = int(delete_selection)

                sparepart = spareparts[delete_selection]
                delete_sparepart(sparepart)
                print("Sucessfully deleted sparepart")

        else:
            break