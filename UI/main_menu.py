from UI.cars_menu import cars_menu
from UI.customers_menu import customers_menu
from UI.customers_type_menu import customers_type_menu
from UI.inventories_menu import inventories_menu
from UI.manufacturers_menu import manufacturers_menu
from UI.orders_menu import orders_menu
from UI.personaldata_menu import personaldata_menu
from UI.spareparts_menu import spareparts_menu
from UI.stores_menu import stores_menu
from UI.suppliers_menu import suppliers_menu


def main_menu():
    while True:
        print("=====================")
        print("Main Menu")
        print("=====================")
        print("1. Customers") #tested
        print("2. Customer Types") #tested
        print("3. Cars") #tested
        print("4. Orders") #tested
        print("5. Personal Data") #tested
        print("6. Suppliers") #tested
        print("7. Stores") #tested
        print("8. Manufacturers") #tested
        print("9. Spareparts") #tested
        print("10. Inventories") #tested
        print("11. Exit")

        print("=====================")
        selection = input("Please enter option above >> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            customers_type_menu()
        elif selection == "3":
            cars_menu()
        elif selection == "4":
            orders_menu()
        elif selection == "5":
            personaldata_menu()
        elif selection == "6":
            suppliers_menu()
        elif selection == "7":
            stores_menu()
        elif selection == "8":
            manufacturers_menu()
        elif selection == "9":
            spareparts_menu()
        elif selection == "10":
            inventories_menu()
        else:
            break
