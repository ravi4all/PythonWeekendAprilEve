class LoanManagement:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.score = 0

    def eligible(self):

        if self.balance < 25000 and self.balance > 15000:
            self.score = 650
            print("Congrats {} your balance is {} and score is {}".format(self.name,self.balance,self.score))
        elif self.balance < 15000:
            self.score = 500
            print("Not eligible because your score is {}".format(self.score))


obj_1 = LoanManagement('Ram', 18000)
obj_1.eligible()
