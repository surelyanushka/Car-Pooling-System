from contract import SmartContract, BookingDetails


class Owner:
    def __init__(self, balance):
        self.contract = SmartContract
        self.balance = balance


    def add_car_to_rent(self, day_price, car_info):
        car = Car(car_info)
        self.contract.add_booking_details(BookingDetails(car, day_price))


    def deploy(self, ether, blockchain):
        self.balance -= ether
        self.contract = SmartContract()
        self.contract.owner_deposit(ether)
        blockchain.add_new_transaction(self.contract)


    def withdraw_earnings(self):
        self.balance += self.contract.withdraw_earnings()


    def allow_car_usage(self):
        self.contract.allow_car_usage()


    def encrypt_and_store_details(self, blockchain):
        blockchain.mine()


class Customer:
    def __init__(self, balance):
        self.balance = balance
        self.contract = SmartContract


    def request_book(self, ether, blockchain):
        self.contract = blockchain.get_unconfirmed_transactions()[0]
        self.contract.client_deposit(ether)
        self.balance -= ether


    def pass_number_of_days(self, days_no):
        self.contract.get_booking_details().request(days_no)


    def retrieve_balance(self):
        self.balance += self.contract.retrieve_balance()


    def end_car_rental(self):
        self.contract.end_car_rental()


    def access_car(self):
        self.contract.get_car().access()




class Car:
    def __init__(self, car_info, **kwargs):
        self.car_info = car_info
        self.additional = kwargs
        self.is_rented = False
        self.allowed_to_use = False


    def access(self):
        print("Car accessed")
        self.is_rented = True


    def end_rental(self):
        self.is_rented = False


    def allow_to_use(self):
        self.allowed_to_use = True


from blockchain import Blockchain
from car_sharing import Owner, Car, Customer




def show_balance(cust_balance, owner_balance):
    print("Customer balance: %s" % (cust_balance,))
    print("Owner balance: %s" % (owner_balance,))


def show_rental_cost(cost):
    print("Rental cost: ", cost)


def start(owner_bal, customer_bal,dayss, daily_price):
    blockchain = Blockchain()
    customer = Customer(customer_bal)
    owner = Owner(owner_bal)
    eth = 50


    show_balance(customer.balance, owner.balance)


   
    owner.deploy(eth, blockchain)


 
    customer.request_book(eth, blockchain)


 
    car = "Bugatti"
   
    owner.add_car_to_rent(daily_price, car)
    customer.pass_number_of_days(dayss)


   
    owner.encrypt_and_store_details(blockchain)
    owner.allow_car_usage()


   
    customer.access_car()


   
    customer.end_car_rental()


 
    owner.withdraw_earnings()
    customer.retrieve_balance()


    show_rental_cost(daily_price*dayss)
    show_balance(customer.balance, owner.balance)




if __name__ == '__main__':
    owner_bal = int(input("Enter owner balance: "))
   
    daily_price = int(input("Per day price: "))
    capacity = int(input("capacity: "))
   
    for i in range(capacity):
        customer_bal = int(input("Enter customer balance: "))
        dayss = int(input("how many days do you want it for? "))
        if customer_bal < daily_price*dayss:
            print("Insufficient funds")


        else:
            start(owner_bal, customer_bal, dayss, daily_price)
