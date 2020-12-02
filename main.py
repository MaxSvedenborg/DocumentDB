from Data.Repository.customertypes_repo import get_all_customer_types
from Data.Repository.customers_repo import get_all_customers
from Data.Repository.cars_repo import get_all_cars
from Data.Repository.personaldata_repo import get_all_personaldata
from Data.Models.carspareparts import CarSparepart
from Data.Models.spareparts import Sparepart
from Data.Models.manufacturers import Manufacturer
from Data.Models.suppliers import Supplier
from Data.Models.personaldata import Personaldata
from Data.Models.inventories import Inventory
from Data.Models.orders import Order
from Data.Models.storeemployees import StoreEmployee
from Data.Models.stores import Store
from Data.Models.orderspareparts import OrderSparepart
from App.UI.main_menu import main_menu


def main():

    main_menu()


if __name__ == '__main__':
    main()
