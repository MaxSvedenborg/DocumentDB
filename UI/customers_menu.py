from BL.customers_controller import get_all_customers, get_customer_by_id, get_customer_by_name, store_new_phone, \
    store_new_customertype, store_new_email, store_new_name, delete_customer, store_new_customer

#As a user, I want to be able to view all customers in the system.
# As a user, I want to be able to add/create customers list into the system.
    #As a user, I want to be able to choose which customers type it is when adding into the system.
#As a user, as I am done with adding customers into the system, I want to be able to choose whether to exit the program or to make an order for this particular customer.
#As a user, I want to be able to update information of the customers in the system.
#As a user, I want to be able to delete a particular customers from the database system i needed.

#As a user, I want to be able to see how many cars did this particular customer own, by searching for name or ID (not sure - wait with it).
#As a user, I want to be able to see how many orders history of this customers (Not sure -wait with it).
from Data.Models.customers import Customer


def customers_menu():
    while True:
        print("===========================")
        print("Customers Menu")
        print("===========================")
        print("1. View All Customers")
        print("2. View Customer by Id")
        print("3. Find and Update Customers")
        print("4. Create new Customer into the system")
        print("5. Delete Customer from the system")
        print("6. Exit Customers Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            customers = get_all_customers()
            for customer in customers:
                print(customer)

        elif selection == "2":
            id = input("Enter customer Id: ")
            customer = get_customer_by_id(id)
            if customer:
                print(customer)
            else:
                print("Could not find customer with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial customer name: ")
            customers = get_customer_by_name(pattern)
            if len(customers) > 0:
                for key, customer in customers.items():
                   print(f'{key}. {customer}')

                edit_choice = input("Would you like to edit customer information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for customer to edit: ")
                    edit_selection = int(edit_selection)

                    customer = customers[edit_selection]
                    print(f'1. Customer Name: {customer.CustomerName}')
                    print(f'2. Customer Address: {customer.CustomerAddress}')
                    print(f'3. Customer Phone: {customer.CustomerPhone}')
                    print(f'4. Customer Email: {customer.CustomerEmail}')
                    print(f'5. Customer Type: {customer.CustomerType.CustomerType}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Name: ")
                        store_new_name(customer, new_value)
                        print("Sucessfully updated customer name")
                    elif line == "2":
                        new_value = input("Enter new Address: ")
                        store_new_phone(customer, new_value)
                        print("Sucessfully updated customer address")
                    elif line == "3":
                        new_value = input("Enter new Phone: ")
                        store_new_phone(customer, new_value)
                        print("Sucessfully updated customer phone")
                    elif line == "4":
                        new_value = input("Enter new Email: ")
                        store_new_email(customer, new_value)
                        print("Sucessfully updated customer email")
                    elif line == "5":

                        print('Please select the following customer type:')
                        print('1. Company')
                        print('2. Private')
                        new_value = input("Enter new Customer Type: ")
                        store_new_customertype(customer, new_value)
                        print("Sucessfully updated customer type")
            else:
                print("No customer found")

        elif selection == "4":
            print('Please select the following customer type:')
            print('1. Company')
            print('2. Private')
            customer_type = input("Enter new Customer Type: ")

            customer = Customer()
            customer.CustomerTypeId = customer_type
            customer.CustomerName = input("Enter Customer Name: ")
            customer.CustomerAddress = input("Enter Customer Address: ")
            customer.CustomerPhone = input("Enter Customer Phone: ")
            customer.CustomerEmail = input("Enter new Email: ")

            store_new_customer(customer)
            print("Sucessfully created new customer")

        elif selection == "5":
            pattern = input("Enter full or partial customer name: ")
            customers = get_customer_by_name(pattern)
            if len(customers) > 0:
                for key, customer in customers.items():
                    print(f'{key}. {customer}')

                delete_selection = input("Enter number for customer to delete: ")
                delete_selection = int(delete_selection)

                customer = customers[delete_selection]
                delete_customer(customer)
                print("Sucessfully deleted customer")
        else:
            break