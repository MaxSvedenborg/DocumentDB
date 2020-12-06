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
        del as_dict['CustomerTypeId']
        del as_dict['cars']
        del as_dict['CustomerType']['_sa_instance_state']
        for car_dict in as_dict['CustomerCars']:
            del car_dict['_sa_instance_state']

        del as_dict['_sa_instance_state']

        mongo_customer = mm.Customer(as_dict)
        mongo_customer.save()


def fix_personal_data():
    personal_data = session.query(Personaldata).all()
    for personal in personal_data:
        as_dict = personal.__dict__

        del as_dict['_sa_instance_state']

        mongo_personaldata = mm.Personaldata(as_dict)
        mongo_personaldata.save()
        print()


def fix_orders():
    orders = session.query(Order).all()
    for order in orders:
        as_dict = order.__dict__

        as_dict['OrderDate'] = str(order.OrderDate)
        as_dict['OrderTime'] = str(order.OrderTime)
        as_dict['Customer'] = order.Customer.__dict__
        as_dict['Orderssparepart'] = [orderssparepart.__dict__ for orderssparepart in order.Orderssparepart]

        del as_dict['_sa_instance_state']
        del as_dict['Customer']['_sa_instance_state']

        mongo_order = mm.Order(as_dict)
        mongo_order.save()


def fix_inventory():
    inventories = session.query(Inventory).all()
    for inventory in inventories:
        as_dict = inventory.__dict__
        del as_dict['_sa_instance_state']
        mongo_inventory = mm.Inventory(as_dict)
        mongo_inventory.save()


def fix_stores():
    stores = session.query(Store).all()
    for store in stores:
        as_dict = store.__dict__

        as_dict['storeemployee'] = [storeemployee.__dict__ for storeemployee in store.storeemployee]
        del as_dict['_sa_instance_state']
        for storeemployee_dict in as_dict['storeemployee']:
            del storeemployee_dict['_sa_instance_state']

        mongo_store = mm.Store(as_dict)
        mongo_store.save()


def main():
    fix_customers()
    fix_personal_data()
    fix_orders()
    fix_inventory()
    fix_stores()


if __name__ == '__main__':
    main()