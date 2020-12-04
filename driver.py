import datetime

from Mysql_db.DB import session
from Mysql_db.Models import Customertype, Personaldata, Store, Customer, Manufactor, Storeemployee, Supplier, Car, Order, Sparepart, Inventory, Orderssparepart
import Mongo.Mongo_models as mm

def fix_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        as_dict = customer.__dict__
        as_dict['CustomerType'] = customer.customertype.__dict__
        as_dict['CustomerCars'] = [car.__dict__ for car in customer.cars]

        del as_dict['customertype']
        del as_dict['cars']
        del as_dict['CustomerType']['_sa_instance_state']
        for car_dict in as_dict['CustomerCars']:
            del car_dict['_sa_instance_state']
            print()
        del as_dict['_sa_instance_state']

        mongo_customer = mm.Customer(as_dict)
        mongo_customer.save()


        print()

def fix_personal_data():
    personal_data = session.query(Personaldata).all()
    for personal in personal_data:
        as_dict = personal.__dict__

        del as_dict['_sa_instance_state']

        mongo_personaldata = mm.Personaldata(as_dict)
        mongo_personaldata.save()
        print()

def fix_manufactorer():
    manufactorers = session.query(Manufactor).all()
    for manufactorer in manufactorers:
        as_dict = manufactorer.__dict__
        as_dict['PersonalData'] = [personal.__dict__ for personal in manufactorer.personaldata]


        del as_dict['personaldata']

        for personaldata_dict in as_dict['ManufactorerPersonaldata']:
            del personaldata_dict['_sa_instance_state']
            print()
        del as_dict['_sa_instance_state']

        mongo_manufactorer = mm.Manufactorer(as_dict)
        mongo_manufactorer.save()


        print()


def main():
    fix_customers()
    fix_personal_data()
    fix_manufactorer()

if __name__ == '__main__':
    main()