from BL.customers_type_controller import get_customertype_by_id, get_customertype_by_name, store_new_name
from Data.Repository.customertypes_repo import get_all_customer_types


def customers_type_menu():
    while True:
        print("===========================")
        print("Customers Types Menu")
        print("===========================")
        print("1. View All Customer Types")
        print("2. View Customer Type by Id")
        print("3. Find and Update Customer Types")
        print("4. Exit Customer Types Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            customertypes = get_all_customer_types()
            for customertype in customertypes:
                print(customertype)

        elif selection == "2":
            print ("Currently, there are only Id '1', and Id '2'")
            id = input("Enter Customer Type Id: ")
            customertype = get_customertype_by_id(id)
            if customertype:
                print(customertype)
            else:
                print("Could not find customer with id ", id)

        elif selection == "3":
            print("Currently, there are only 'private', and 'company")
            pattern = input("Enter full or partial customer type name: ")
            customertypes = get_customertype_by_name(pattern)
            if len(customertypes) > 0:
                for key, customertype in customertypes.items():
                   print(f'{key}. {customertype}')

                edit_choice = input("Would you like to edit customer type information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for customer type to edit: ")
                    edit_selection = int(edit_selection)

                    customertype = customertypes[edit_selection]
                    print(f'1. Customer Type Name: {customertype.CustomerType}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Customer Type Name (Private? Or Company?): ")
                        store_new_name(customertype, new_value)
                        print("Sucessfully updated customer type")

            else:
                print("No customer type found")

        else:
            break


