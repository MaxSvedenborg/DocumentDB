from Mongo.Base_documents import Document, db, NestedDocument


class Personaldata(Document):
    collection = db.personaldata


class Customer(Document):
    collection = db.customers


    def __init__(self, data):
        super().__init__(data)

        if "CustomerCars" in self.__dict__:
            self.CustomerCars = [NestedDocument(car) for car in self.CustomerCars]

        if "CustomerType" in self.__dict__:
            self.CustomerType = NestedDocument(self.CustomerType)

    def save(self):
        if "CustomerCars" in self.__dict__:
            self.CustomerCars = [car.__dict__ for car in self.CustomerCars]

        if "CustomerType" in self.__dict__:
            self.CustomerType = self.CustomerType.__dict__

        super().save()


    def __str__(self):
        return f"{self.CustomerName}"


class Order(Document):
    collection = db.orders


class Inventory(Document):
    collection = db.inventory


class Store(Document):
    collection = db.stores

    # def __init__(self, data):
    #     super().__init__(data)
    #
    #     if "StoreEmployees" in self.__dict__:
    #         self.StoreEmployees = [NestedDocument(storeemployee) for storeemployee in self.StoreEmployees]
    #
    # def save(self):
    #     if "StoreEmployees" in self.__dict__:
    #         self.StoreEmployees = [storeemployee.__dict__ for storeemployee in self.StoreEmployees]
    #
    #     super().save()

    def __str__(self):
        return f'{self.StoreName}'


