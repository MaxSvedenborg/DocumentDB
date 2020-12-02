#view number of cars in customers
from BL.cars_controller import get_all_cars, get_car_by_id, store_new_regno, store_new_manufacturer, store_new_model, \
    store_new_color, store_new_owner, store_new_car, delete_car, get_car_by_manufacturer
from Data.Models.cars import Car


def cars_menu():
    while True:
        print("===========================")
        print("Cars Menu")
        print("===========================")
        print("1. View All Cars")
        print("2. View Cars by Id")
        print("3. Find and Update Cars")
        print("4. Create new Car into the system")
        print("5. Delete Car from the system")
        print("6. Exit Car Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            cars = get_all_cars()
            for car in cars:
                print(car)

        elif selection == "2":
            id = input("Enter Car Id: ")
            car = get_car_by_id(id)
            if car:
                print(car)
            else:
                print("Could not find car with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial car manufacturer: ")
            cars = get_car_by_manufacturer(pattern)
            if len(cars) > 0:
                for key, car in cars.items():
                    print(f'{key}. {car}')

                edit_choice = input("Would you like to edit car information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for car to edit: ")
                    edit_selection = int(edit_selection)

                    car = cars[edit_selection]
                    print(f'1. Car Registration Number: {car.CarsRegNo}')
                    print(f'2. Car Manufacturer: {car.CarsManufacturer}')
                    print(f'3. Car Model: {car.CarsModel}')
                    print(f'4. Car Color: {car.CarsColor}')
                    print(f'5. Customer Id: {car.CustomerId}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new car Registration Number: ")
                        store_new_regno(car, new_value)
                        print("Sucessfully updated new car Registration Number")
                    elif line == "2":
                        new_value = input("Enter new Car Manufacturer: ")
                        store_new_manufacturer(car, new_value)
                        print("Sucessfully updated new car manufacturer")
                    elif line == "3":
                        new_value = input("Enter new Car Model: ")
                        store_new_model(car, new_value)
                        print("Sucessfully updated new car model")
                    elif line == "4":
                        new_value = input("Enter new Car Color: ")
                        store_new_color(car, new_value)
                        print("Sucessfully updated new car color")
                    elif line == "5":
                        new_value = input("Enter new Owner: Customer Id: ")
                        store_new_owner(car, new_value)
                        print("Sucessfully updated new owner with customer Id")
            else:
                print("No car found")


        elif selection == "4":
            edit_choice = input("Opps! CustomerId information needed, do you have them? [y/n]: ")
            if (edit_choice.lower() == "y"):
                car = Car()
                car.CarsRegNo = input("Enter Car Registration Number: ")
                car.CarsManufacturer = input("Enter Car Manufacturer: ")
                car.CarsModel = input("Enter Car Model: ")
                car.CarsColor = input("Enter Car Color: ")
                car.CustomerId = input("Enter Customer Id: ")
                store_new_car(car)
                print("Sucessfully created new car")

        elif selection == "5":
            pattern = input("Enter full or partial car manufacturer: ")
            cars = get_car_by_manufacturer(pattern)
            if len(cars) > 0:
                for key, car in cars.items():
                    print(f'{key}. {car}')

                delete_selection = input("Enter number for car to delete: ")
                delete_selection = int(delete_selection)

                car = cars[delete_selection]
                delete_car(car)
                print("Sucessfully deleted car")

        else:
            break