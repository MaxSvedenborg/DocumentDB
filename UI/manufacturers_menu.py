from BL.manufacturers_controller import get_all_manufacturers, get_manufacturer_by_id, get_manufacturer_by_name, \
    store_new_manufacturer_address, store_new_manufacturer_phone, store_new_manufacturer, delete_manufacturer, store_new_manufacturer_name
from BL.personaldata_controller import store_new_personaldata
from Data.Models.manufacturers import Manufacturer
from Data.Models.personaldata import Personaldata


def manufacturers_menu():
    while True:
        print("===========================")
        print("Manufacturer Menu")
        print("===========================")
        print("1. View All Manufacturer")
        print("2. View Manufacturer by Id")
        print("3. Find and Update Manufacturers")
        print("4. Create new Manufacturer into the system")
        print("5. Delete Manufacturer from the system")
        print("6. Exit Manufacturer Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            manufacturers = get_all_manufacturers()
            for manufacturer in manufacturers:
                print(manufacturer)

        elif selection == "2":
            id = input("Enter Manufacturer Id: ")
            manufacturer = get_manufacturer_by_id(id)
            if manufacturer:
                print(manufacturer)
            else:
                print("Could not find manufacturer with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial name of the manufacturer: ")
            manufacturers = get_manufacturer_by_name(pattern)
            if len(manufacturers) > 0:
                for key, manufacturer in manufacturers.items():
                    print(f'{key}. {manufacturer}')

                edit_choice = input("Would you like to edit manufacturer information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for manufacturer to edit: ")
                    edit_selection = int(edit_selection)

                    manufacturer = manufacturers[edit_selection]
                    print(f'1. Manufacturer Name: {manufacturer.ManufacturerName}')
                    print(f'2. Manufacturer Address: {manufacturer.ManufacturerAddressHQ}')
                    print(f'3. Manufacturer Phone: {manufacturer.ManufacturerPhoneHQ}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Manufacturer Name: ")
                        store_new_manufacturer_name(manufacturer, new_value)
                        print("Sucessfully updated new Manufacturer Name")
                    elif line == "2":
                        new_value = input("Enter new Manufacturer Address: ")
                        store_new_manufacturer_address(manufacturer, new_value)
                        print("Sucessfully updated new Manufacturer Address")
                    elif line == "3":
                        new_value = input("Enter new Manufacturer Phone: ")
                        store_new_manufacturer_phone(manufacturer, new_value)
                        print("Sucessfully updated new Manufacturer Phone")

            else:
                print("No manufacturer found")

        elif selection == "4":
            manufacturer = Manufacturer()
            manufacturer.ManufacturerName = input("Enter Manufacturer Name: ")
            manufacturer.ManufacturerAddressHQ = input("Enter Manufacturer Address: ")
            manufacturer.ManufacturerPhoneHQ = input("Enter Manufacturer Phone Number: ")

            contact_person = Personaldata()
            contact_person.PersonalDataName = input("Manufacturer contact person name: ")
            contact_person.PersonalDataPhone = input("Manufacturer contact person phone: ")
            contact_person.PersonalDataEmail = input("Manufacturer contact person email: ")

            store_new_personaldata(contact_person)
            manufacturer.PersonalData = contact_person

            store_new_manufacturer(manufacturer)
            print("Sucessfully created new Manufacturer")

        elif selection == "5":
            pattern = input("Enter full or partial manufacturer name: ")
            manufacturers = get_manufacturer_by_name(pattern)
            if len(manufacturers) > 0:
                for key, manufacturer in manufacturers.items():
                    print(f'{key}. {manufacturer}')

                delete_selection = input("Enter number for manufacturer to delete: ")
                delete_selection = int(delete_selection)

                manufacturer = manufacturers[delete_selection]
                delete_manufacturer(manufacturer)
                print("Sucessfully deleted Manufacturer")

        else:
            break