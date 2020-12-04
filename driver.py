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

def fix_inventory():
    inventories = session.query(Inventory).all()
    for inventory in inventories:
        as_dict = inventory.__dict__

        mongo_inventory = mm.Inventory(as_dict)
        mongo_inventory.save()

        print()


def fix_stores():
    stores = session.query(Store).all()
    for store in stores:
        as_dict = store.__dict__
        as_dict['Storeemployees'] = [storeemployee.__dict__ for storeemployee in stores.storeemplyee]

        del as_dict['storeemployee']
        for storeemployee_dict in as_dict['StoreEmployee']:
            del storeemployee_dict['_sa_instance_state']
            print()
        del as_dict['_sa_instance_state']

        mongo_store = mm.Store(as_dict)
        mongo_store.save()


        print()
# def fix_offises():
#     offices = session.query(Office).all()
#     for office in offices:
#         as_dict = office.__dict__
#         as_dict = {key: value for key, value in as_dict.items() if value is not None}
#         del as_dict['_sa_instance_state']
#         mongo_office = mm.Office(as_dict)
#         mongo_office.save()
#
#
# def fix_employees():
#     employees = session.query(Employee).all()
#     for employee in employees:
#         as_dict = employee.__dict__
#         as_dict['officeId'] = mm.Office.find(officeCode=employee.officeCode).first_or_none()._id
#         del as_dict['officeCode']
#         del as_dict['_sa_instance_state']
#         if as_dict['reportsTo'] is None:
#             del as_dict['reportsTo']
#         mongo_employee = mm.Employee(as_dict)
#
#         mongo_employee.save()
#
#     employees = mm.Employee.all()
#     for employee in employees:
#         if hasattr(employee, 'reportsTo'):
#             employee.reportsTo = mm.Employee.find(employeeNumber=employee.reportsTo).first_or_none()._id
#             employee.save()
#
#
# def fix_customers():
#     customers = session.query(Customer).all()
#     for customer in customers:
#         as_dict = customer.__dict__
#         as_dict = {key:value for key, value in as_dict.items() if value is not None}
#         if 'salesRepEmployeeNumber' in as_dict:
#             as_dict['salesRepEmployeeNumber'] = mm.Employee.find(employeeNumber=as_dict['salesRepEmployeeNumber']).first_or_none()._id
#         if 'creditLimit' in as_dict:
#             as_dict['creditLimit'] = float(as_dict['creditLimit'])
#         del as_dict['_sa_instance_state']
#         payments = []
#         for payment in customer.payments:
#             payments.append({
#                 'amount': float(payment.amount),
#                 'checkNumber': payment.checkNumber,
#                 'paymentDate': datetime.datetime(payment.paymentDate.year, payment.paymentDate.month, payment.paymentDate.day)
#             })
#         as_dict['payments'] = payments
#
#         mongo_customer = mm.Customer(as_dict)
#         mongo_customer.save()
#
#
# def fix_orders():
#     orders = session.query(Order).all()
#     for order in orders:
#         as_dict = order.__dict__
#         as_dict['orderDate'] = datetime.datetime(order.orderDate.year, order.orderDate.month, order.orderDate.day)
#         as_dict['requiredDate'] = datetime.datetime(order.requiredDate.year, order.requiredDate.month, order.requiredDate.day)
#         if order.shippedDate is not None:
#             as_dict['shippedDate'] = datetime.datetime(order.shippedDate.year, order.shippedDate.month, order.shippedDate.day)
#         else:
#             del as_dict['shippedDate']
#         if order.comments is None:
#             del as_dict['comments']
#         as_dict['customerId'] = mm.Customer.find(customerNumber=order.customerNumber).first_or_none()._id
#         orderdetails = []
#         for orderdetail in order.orderdetail:
#             order_detail_dict = orderdetail.__dict__
#             orderdetails.append({
#                 'productId': mm.Product.find(productCode=orderdetail.productCode).first_or_none()._id,
#                 'orderLineNumber': orderdetail.orderLineNumber,
#                 'quantityOrdered': orderdetail.quantityOrdered,
#                 'priceEach': float(orderdetail.priceEach)
#             })
#         as_dict['orderdetail'] = orderdetails
#
#         del as_dict['_sa_instance_state']
#         mongo_order = mm.Order(as_dict)
#         mongo_order.save()
#
#
# def clean_orders():
#     orders = mm.Order.all()
#     for order in orders:
#         order.delete_field('customerNumber')
#


def fix_personal_data():
    personal_data = session.query(Personaldata).all()
    for personal in personal_data:
        as_dict = personal.__dict__
        print()


def main():
    #fix_customers()
    fix_personal_data()
    #fix_employees()
    #fix_customers()
    #fix_orders()
    #clean_orders()

if __name__ == '__main__':
    main()