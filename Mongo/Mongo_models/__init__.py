from Mongo.Base_documents import Document, db


class Product(Document):
    collection = db.products


class Office(Document):
    collection = db.offices


class Employee(Document):
    collection = db.employees

class Customer(Document):
    collection = db.customers


class Order(Document):
    collection = db.orders


class Inventory(Document):
    collection = db.inventory


class Store(Document):
    collection = db.stores


class Personaldata(Document):
    collection = db.personalata