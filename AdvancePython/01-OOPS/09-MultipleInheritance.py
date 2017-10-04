class Bank:

    def __init__(self):
        self.name = "HDFC"
        self.branch = "Rohini"
        self.ifsc = 10101010


class Account():

    def __init__(self):
        self.accType = "Saving Account"
        self.balance = "25,000"


class Customer(Bank, Account):

    def __init__(self, name, pin):
        self.userName = name
        self.pin = pin
        Bank.__init__(self)
        Account.__init__(self)

    def printCustomer(self):
        print("Customer Details")
        print(self.name,self.branch)
        print(self.userName,self.accType, self.balance)

cust = Customer('Ram',1234)
cust.printCustomer()
