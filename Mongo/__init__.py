from Mongo.Base_documents import Document, db


class Customer(Document):
    collection = db.customers


class Order(Document):
    collection = db.Orders


class Personaldata(Document):
    collection = db.personalata

class Store(Document):
    collection = db.stores


class Supplier(Document):
    collection = db.suppliers