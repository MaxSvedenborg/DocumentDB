from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customertype(Base):
    __tablename__ = 'customertype'

    CustomerTypeId = Column(Integer, primary_key=True)
    CustomerType = Column(String(100), nullable=False)


class Personaldata(Base):
    __tablename__ = 'personaldata'

    PersonalDataId = Column(Integer, primary_key=True)
    PersonaDataName = Column(String(100), nullable=False)
    PersonalDataPhone = Column(String(100), nullable=False)
    PersonalDataEmail = Column(String(100), nullable=False)


class Store(Base):
    __tablename__ = 'store'

    StoreId = Column(Integer, primary_key=True)
    StoreName = Column(String(100), nullable=False)
    StoreAddress = Column(String(100), nullable=False)
    StorePhone = Column(String(100), nullable=False)
    StoreEmail = Column(String(100), nullable=False)


class Customer(Base):
    __tablename__ = 'customer'

    CustomerId = Column(Integer, primary_key=True)
    CustomerName = Column(String(100), nullable=False)
    CustomerAddress = Column(String(100), nullable=False)
    CustomerPhone = Column(String(100), nullable=False)
    CustomerEmail = Column(String(100), nullable=False)
    CustomerTypeId = Column(ForeignKey('customertype.CustomerTypeId'), nullable=False, index=True)

    customertype = relationship('Customertype')
    cars = relationship('Car')

class Manufactor(Base):
    __tablename__ = 'manufactor'

    ManufactorerId = Column(Integer, primary_key=True)
    ManufactorerName = Column(String(100), nullable=False)
    ManufactorerAddressHQ = Column(String(100), nullable=False)
    ManufactoerPhoneHQ = Column(String(100), nullable=False)
    PersonalDataId = Column(ForeignKey('personaldata.PersonalDataId'), nullable=False, index=True)

    personaldata = relationship('Personaldata')


class Storeemployee(Base):
    __tablename__ = 'storeemployee'

    StoreEmployeeId = Column(Integer, primary_key=True)
    StoreId = Column(ForeignKey('store.StoreId'), nullable=False, index=True)
    PersonalDataId = Column(ForeignKey('personaldata.PersonalDataId'), nullable=False, index=True)

    personaldata = relationship('Personaldata')
    store = relationship('Store')


class Supplier(Base):
    __tablename__ = 'supplier'

    SupplierId = Column(Integer, primary_key=True)
    SupplierName = Column(String(100), nullable=False)
    SupplierAddress = Column(String(100), nullable=False)
    SupplierPhone = Column(String(100), nullable=False)
    SupplierEmail = Column(String(100), nullable=False)
    PersonalDataId = Column(ForeignKey('personaldata.PersonalDataId'), nullable=False, index=True)

    personaldata = relationship('Personaldata')


class Car(Base):
    __tablename__ = 'cars'

    CarsId = Column(Integer, primary_key=True)
    CarsRegNo = Column(String(100), nullable=False)
    CarsManufactor = Column(String(100), nullable=False)
    CarsModel = Column(String(100), nullable=False)
    CarsColor = Column(String(100), nullable=False)
    CustomerId = Column(ForeignKey('customer.CustomerId'), nullable=False, index=True)

    customer = relationship('Customer')
    sparepart = relationship('Sparepart', secondary='carssparepart')


class Order(Base):
    __tablename__ = 'orders'

    OrderId = Column(Integer, primary_key=True)
    OrderDate = Column(Date, nullable=False)
    OrderTime = Column(Time, nullable=False)
    StoreId = Column(ForeignKey('store.StoreId'), nullable=False, index=True)
    CustomerId = Column(ForeignKey('customer.CustomerId'), nullable=False, index=True)

    Customer = relationship('Customer')
    Store = relationship('Store')
    Orderssparepart = relationship('Orderssparepart')


class Sparepart(Base):
    __tablename__ = 'sparepart'

    SparepartId = Column(Integer, primary_key=True)
    SparepartName = Column(String(45), nullable=False)
    ManufactorId = Column(ForeignKey('manufactor.ManufactorerId'), nullable=False, index=True)
    SupplierId = Column(ForeignKey('supplier.SupplierId'), nullable=False, index=True)
    SparepartDescription = Column(String(10000), nullable=False)

    manufactor = relationship('Manufactor')
    supplier = relationship('Supplier')


t_carssparepart = Table(
    'carssparepart', metadata,
    Column('CarsID', ForeignKey('cars.CarsId'), primary_key=True, nullable=False, index=True),
    Column('SparepartId', ForeignKey('sparepart.SparepartId'), primary_key=True, nullable=False, index=True)
)


class Inventory(Base):
    __tablename__ = 'inventory'

    InventoryId = Column(Integer, primary_key=True)
    StoreId = Column(ForeignKey('store.StoreId'), nullable=False, index=True)
    InventoryLocation = Column(String(100), nullable=False)
    InventoryQTY = Column(Integer, nullable=False)
    InventoryCriticalLevel = Column(Integer, nullable=False)
    InventoryQTYAutomaticOrder = Column(Integer, nullable=False)
    InventoryETA = Column(String(100), nullable=False)
    SparepartId = Column(ForeignKey('sparepart.SparepartId'), nullable=False, index=True)

    sparepart = relationship('Sparepart')
    store = relationship('Store')


class Orderssparepart(Base):
    __tablename__ = 'orderssparepart'

    OrderId = Column(ForeignKey('orders.OrderId'), primary_key=True, nullable=False, index=True)
    SparepartId = Column(ForeignKey('sparepart.SparepartId'), primary_key=True, nullable=False, index=True)
    OrdersAmount = Column(Integer, nullable=False)

    Order = relationship('Order')
    Sparepart = relationship('Sparepart')
