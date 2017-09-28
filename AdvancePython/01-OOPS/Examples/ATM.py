class Bank:

    def __init__(self, name,acc_bal):
        self.name = name
        self.acc_bal = acc_bal

    def userPin(self):
        self.pin = input("Enter your PIN : ")

        if self.pin == "1234":
            print("Welcome {} to HDFC...".format(self.name))
            # print("Total balance is {}".format(self.acc_bal))
            self.menu()
        else:
            print("Wrong PIN")

    def menu(self):
        print("""
        1. Withdraw
        2. Deposit
        3. Balance Enquiry
        4. Quit
        """)

        user_ch = input("Enter your choice : ")

        todo = {
            "1" : self.withdraw,
            "2" : self.deposit,
            "3" : self.balEnquiry,
            "4" : quit
        }

        todo.get(user_ch)()

    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw : "))
        self.acc_bal = self.acc_bal - amount
        print("Remaining Balance is {}".format(self.acc_bal))
        self.menu()

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit : "))
        self.acc_bal = self.acc_bal + amount
        print("Total Balance is {}".format(self.acc_bal))
        self.menu()

    def balEnquiry(self):
        print("Available Balance is {}".format(self.acc_bal))
        self.menu()


name = input("Enter your name : ")
bal = int(input("Enter your balance : "))

if __name__ == '__main__':
    obj = Bank(name, bal)
    obj.userPin()


