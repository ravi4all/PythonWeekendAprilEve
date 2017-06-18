from modules import my_module

class Calc:

    def take_input(self):
        self.num_1 = int(input("Enter first number : "))
        self.num_2 = int(input("Enter second number : "))

    def show_result(self):
        print(my_module.add(self.num_1,self.num_2))
        print(my_module.sub(self.num_1,self.num_2))
        print(my_module.div(self.num_1,self.num_2))
        print(my_module.mul(self.num_1,self.num_2))

obj = Calc()
obj.take_input()
obj.show_result()