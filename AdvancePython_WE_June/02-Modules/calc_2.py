from modules import my_module_2

class Calc:

    def main_menu(self):
        print("""
        1. Add
        2. Sub
        3. Div
        4. Mul
        """)
        options = {"1":"+",
                   "2":"-",
                   "3":"/",
                   "4":"*"}
        user_choice = input("Enter your choice : ")
        self.take_input()
        #options.get(user_choice,self.errHandler)(self.num_1,self.num_2)
        self.show_result(user_choice,options)

    def take_input(self):
        self.num_1 = int(input("Enter first number : "))
        self.num_2 = int(input("Enter second number : "))

    def show_result(self,user_choice,options):
        print("Result is ",my_module_2.calculate(options[user_choice],self.num_1,self.num_2))

obj = Calc()
obj.main_menu()
#obj.take_input()
#obj.show_result()