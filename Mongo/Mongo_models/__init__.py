from Mongo.Base_documents import Document, db


class Personaldata(Document):
    collection = db.personaldata


class Office(Document):
    collection = db.offices


class Employee(Document):
    collection = db.employees

class Customer(Document):
    collection = db.customers


class Order(Document):
    collection = db.orders