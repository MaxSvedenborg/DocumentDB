from BL.personaldata_controller import store_new_personaldata
from BL.suppliers_controller import get_all_suppliers, get_supplier_by_id, get_supplier_by_name, store_new_name, \
    store_new_phone, store_new_address, store_new_email, store_new_supplier, delete_supplier
from Data.Models.personaldata import Personaldata
from Data.Models.suppliers import Supplier


def suppliers_menu():
    while True:
        print("===========================")
        print("Suppliers Menu")
        print("===========================")
        print("1. View All Suppliers")
        print("2. View Supplier by Id")
        print("3. Find and Update Supplier")
        print("4. Create new Supplier into the system")
        print("5. Delete Supplier from the system")
        print("6. Exit Supplier Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)

        elif selection == "2":
            id = input("Enter Supplier Id: ")
            supplier = get_supplier_by_id(id)
            if supplier:
                print(supplier)
            else:
                print("Could not find Supplier with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial Supplier name: ")
            suppliers = get_supplier_by_name(pattern)
            if len(suppliers) > 0:
                for key, supplier in suppliers.items():
                    print(f'{key}. {supplier}')

                edit_choice = input("Do you want to edit Supplier information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for Supplier to edit: ")
                    edit_selection = int(edit_selection)

                    supplier = suppliers[edit_selection]
                    print(f'1. Supplier Name: {supplier.SupplierName}')
                    print(f'2. Supplier Address: {supplier.SupplierAddress}')
                    print(f'3. Supplier Phone: {supplier.SupplierPhone}')
                    print(f'4. Supplier Email: {supplier.SupplierEmail}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Name: ")
                        store_new_name(supplier, new_value)
                        print("Sucessfully updated Supplier name")
                    elif line == "2":
                        new_value = input("Enter new Address: ")
                        store_new_address(supplier, new_value)
                        print("Sucessfully updated Supplier address")
                    elif line == "3":
                        new_value = input("Enter new Phone: ")
                        store_new_phone(supplier, new_value)
                        print("Sucessfully updated Supplier phone")
                    elif line == "4":
                        new_value = input("Enter new Email: ")
                        store_new_email(supplier, new_value)
                        print("Sucessfully updated Supplier email")
            else:
                print("No Supplier found")

        elif selection == "4":

            supplier = Supplier()
            supplier.SupplierName = input("Enter Supplier Name: ")
            supplier.SupplierAddress = input("Enter Supplier Address: ")
            supplier.SupplierPhone = input("Enter Supplier Phone: ")
            supplier.SupplierEmail = input("Enter Supplier Email: ")

            contact_person = Personaldata()
            contact_person.PersonalDataName = input("Supplier contact person name: ")
            contact_person.PersonalDataPhone = input("Supplier contact person phone: ")
            contact_person.PersonalDataEmail = input("Supplier contact person email: ")

            store_new_personaldata(contact_person)
            supplier.PersonalData = contact_person
            store_new_supplier(supplier)
            print("Sucessfully created new supplier")

        elif selection == "5":
            pattern = input("Enter full or partial Supplier name: ")
            suppliers = get_supplier_by_name(pattern)
            if len(suppliers) > 0:
                for key, supplier in suppliers.items():
                    print(f'{key}. {supplier}')

                delete_selection = input("Enter number for supplier to delete: ")
                delete_selection = int(delete_selection)

                supplier = suppliers[delete_selection]
                delete_supplier(supplier)
                print("Sucessfully deleted supplier")
        else:
            break
