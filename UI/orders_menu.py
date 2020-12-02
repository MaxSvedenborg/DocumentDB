from BL.orders_controller import get_all_orders, get_order_by_id, get_order_by_date, store_new_date, store_new_time, \
    store_new_storeId, store_new_customerId, delete_order, store_new_order
from Data.Models.orders import Order


def orders_menu():
    while True:
        print("===========================")
        print("Orders Menu")
        print("===========================")
        print("1. View All Orders")
        print("2. View Order by Id")
        print("3. Find and Update Orders")
        print("4. Create new Order into the system")
        print("5. Delete Order from the system")
        print("7. Exit Order Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            orders = get_all_orders()
            for order in orders:
                print(order)

        elif selection == "2":
            id = input("Enter Order Id: ")
            order = get_order_by_id(id)
            if order:
                print(order)
            else:
                print("Could not find order with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial date: ")
            orders = get_order_by_date(pattern)
            if len(orders) > 0:
                for key, order in orders.items():
                   print(f'{key}. {order}')

                edit_choice = input("Would you like to edit order information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for order to edit: ")
                    edit_selection = int(edit_selection)

                    order = orders[edit_selection]
                    print(f'1. Order Date: {order.OrderDate}')
                    print(f'2. Order Time: {order.OrderTime}')
                    print(f'3. Order Store Id: {order.StoreId}')
                    print(f'4. Order Customer Id: {order.CustomerId}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Order Date: ")
                        store_new_date(order, new_value)
                        print("Sucessfully updated order date")
                    elif line == "2":
                        new_value = input("Enter new Order Time: ")
                        store_new_time(order, new_value)
                        print("Sucessfully updated order time")
                    elif line == "3":
                        new_value = input("Enter new Store Id: ")
                        store_new_storeId(order, new_value)
                        print("Sucessfully updated Store Id")
                    elif line == "4":
                        new_value = input("Enter new Customer Id: ")
                        store_new_customerId(order, new_value)
                        print("Sucessfully updated customer Id")
            else:
                print("No order found")

        elif selection == "4":

            edit_choice = input("Opps! StoreId and CustomerId information needed, do you have them? [y/n]: ")
            if (edit_choice.lower() == "y"):
                order = Order()
                order.OrderDate = input("Enter Order Date: ")
                order.OrderTime = input("Enter Order Time: ")
                order.StoreId = input("Enter Store Id: ")
                order.CustomerId = input("Enter Customer Id: ")
                store_new_order(order)
                print("Sucessfully created new order")

        elif selection == "5":
            pattern = input("Enter full or partial order date: ")
            orders =  get_order_by_date(pattern)
            if len(orders) > 0:
                for key, order in orders.items():
                    print(f'{key}. {order}')
                delete_selection = input("Enter number for order to delete: ")
                delete_selection = int(delete_selection)
                order = orders[delete_selection]
                delete_order(order)
                print("Sucessfully deleted order")

        else:
            break