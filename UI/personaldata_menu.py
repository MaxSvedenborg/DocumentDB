from BL.personaldata_controller import get_all_personaldata, get_personaldata_by_id, get_personaldata_by_name, \
    store_new_name, store_new_phone, store_new_email, store_new_personaldata, delete_personaldata

from Data.Models.personaldata import Personaldata


def personaldata_menu():
    while True:
        print("===========================")
        print("Personaldata Menu")
        print("===========================")
        print("1. View All Personaldata")
        print("2. View Personaldata by Id")
        print("3. Find and Update PersonalData")
        print("4. Create new Personaldata into the system")
        print("5. Delete current Personaldata from the system")
        print("6. Exit Personaldata Menu")


        selection = input("Please select options:  ")

        if selection == "1":
            personaldata = get_all_personaldata()
            for p in personaldata:
                print(p)
        elif selection == "2":
            id = input("Enter Personaldata id: ")
            personaldata = get_personaldata_by_id(id)
            if personaldata:
                print(personaldata)
            else:
                print("Could not find Personaldata with id", id)
        elif selection == "3":
            pattern = input("Enter full or partial Personaldata name: ")
            personaldata = get_personaldata_by_name(pattern)
            if len(personaldata) > 0:
                for key, p in personaldata.items():
                    print(f'{key}. {personaldata}')

                edit_selection = input("Enter number for personaldata to edit: ")
                edit_selection = int(edit_selection)

                pd = personaldata[edit_selection]
                print(f'1. Personaldata Name: {pd.PersonalDataName}')
                print(f'2. Personaldata Phone: {pd.PersonalDataPhone}')
                print(f'3. Personaldata Email: {pd.PersonalDataEmail}')

                line = input("Enter number for what line to edit: ")
                if line == "1":
                    new_value = input("Enter new Personaldata Name: ")
                    store_new_name(personaldata, new_value)
                    print("Sucessfully updated personaldata name")
                elif line == "2":
                    new_value = input("Enter new Phone: ")
                    store_new_phone(personaldata, new_value)
                    print("Sucessfully updated personaldata Phone")
                elif line == "3":
                    new_value = input("Enter new Email: ")
                    store_new_email(personaldata, new_value)
                    print("Sucessfully updated personaldata email")
            else:
                print("No personaldata found")

        elif selection == "4":

            personaldata = Personaldata()
            personaldata.PersonalDataName = input("Enter Personaldata Name: ")
            personaldata.PersonalDataPhone = input("Enter Personaldata Phone: ")
            personaldata.PersonalDataEmail = input("Enter Personaldata Email: ")

            store_new_personaldata(personaldata)
            print("Sucessfully created new Personaldata")

        elif selection == "5":
            pattern = input("Enter full or partial Personaldata name: ")
            personaldata = get_personaldata_by_name(pattern)
            if len(personaldata) > 0:
                for key, p in personaldata.items():
                    print(f'{key}. {personaldata}')

                delete_selection = input("Enter number for customer to delete: ")
                delete_selection = int(delete_selection)

                personaldata = personaldata[delete_selection]
                delete_personaldata(personaldata)
                print("Sucessfully deleted Personaldata")

        else:
            break