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

    def __init__(self, data):
        super().__init__(data)

        if "Customer" in self.__dict__:
            self.Customer = NestedDocument(self.Customer)

        if "Orderssparepart" in self.__dict__:
            self.Orderssparepart = [NestedDocument(orderssparepart) for orderssparepart in self.Orderssparepart]

    def save(self):
        if "Customer" in self.__dict__:
            self.Customer = self.Customer.__dict__

        if "Orderssparepart" in self.__dict__:
            self.Orderssparepart = [orderssparepart.__dict__ for orderssparepart in self.Orderssparepart]

        super().save()



    def __str__(self):
        return f'{self.OrderDate} {self.OrderTime} ({self.Customer.CustomerName})'


class Inventory(Document):
    collection = db.inventory


class Store(Document):
    collection = db.stores

class Manufactor(Document):
    collection = db.manufactors

    def __init__(self, data):
        super().__init__(data)

        if "PersonalData" in self.__dict__:
            self.PersonalData = [NestedDocument(personaldata) for personaldata in self.PersonalData]

    def save(self):
        if "PersonalData" in self.__dict__:
            self.PersonalData = [personaldata.__dict__ for personaldata in self.PersonalData]

        super().save()

class Supplier(Document):
    collection = db.suppliers

    def __init__(self, data):
        super().__init__(data)

        if "PersonalData" in self.__dict__:
            self.PersonalData = [NestedDocument(personaldata) for personaldata in self.PersonalData]

    def save(self):
        if "PersonalData" in self.__dict__:
            self.PersonalData = [personaldata.__dict__ for personaldata in self.PersonalData]

        super().save()

class Sparepart(Document):
    collection = db.spareparts