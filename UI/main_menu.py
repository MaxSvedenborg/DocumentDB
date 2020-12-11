from UI.customers_menu import customers_menu
from UI.orders_menu import orders_menu
from UI.manufacturers_menu import manufacturers_menu
from UI.personaldata_menu import personaldata_menu

def main_menu():
    while True:
        print("=====================")
        print("Main Menu")
        print("=====================")
        print("1. Customers") #tested - todo: create car for customer in menu
        print("2. Customer Types")
        print("3. Cars")
        print("4. Orders")  #tested - todo: create orderspareparts in menu
        print("5. Personal Data")
        print("6. Suppliers")
        print("7. Stores")
        print("8. Manufacturers")
        print("9. Spareparts")
        print("10. Inventories")
        print("11. Exit")

        print("=====================")
        selection = input("Please enter option above >> ")
        if selection == "1":
            customers_menu()
        # elif selection == "2":
        #     customers_type_menu()
        # elif selection == "3":
        #     cars_menu()
        # elif selection == "4":
        #     orders_menu()
        elif selection == "5":
            personaldata_menu()
        # elif selection == "6":
        #     suppliers_menu()
        # elif selection == "7":
        #     stores_menu()
        elif selection == "8":
            manufacturers_menu()
        # elif selection == "9":
        #     spareparts_menu()
        # elif selection == "10":
        #     inventories_menu()
        else:
            break
