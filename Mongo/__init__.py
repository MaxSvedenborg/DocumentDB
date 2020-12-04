from Mongo.Base_documents import Document, db


class Customer(Document):
    collection = db.customers


class Personaldata(Document):
    collection = db.personaldata


class Order(Document):
    collection = db.Orders


class Store(Document):
    collection = db.stores


class Supplier(Document):
    collection = db.suppliers

class Manufactorer(Document):
    collection = db.manufactorers