# def add(x,y):
#     return x + y
#
# def sub(x,y):
#     return x - y
#
# def mul(x,y):
#     return x * y
#
# def div(x,y):
#     return x/y

def calc(x,y,opr):

    return eval('x'+opr+'y')

    # if ch == "1":
    #     return x + y
    # elif ch == "2":
    #     return x - y
    # elif ch == "3":
    #     return x * y
    # else:
    #     return x / y


def errHandler():
    print("Wrong Choice, Try Again......")

while True:

    print("""
    1. Add
    2. Sub
    3. Multiply
    4. Divide
    5. Quit
    """)

    # todo = {
    #     "1" : calc,
    #     "2" : calc,
    #     "3" : calc,
    #     "4" : calc,
    #     "5" : quit
    #
    # }

    todo = {
        "1" : "+",
        "2" : "-",
        "3" : "*",
        "4" : "/",
        "5" : quit
    }

    user_choice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    # print(todo.get(user_choice, errHandler)(num_1,num_2,user_choice))

    opr = todo.get(user_choice)

    print(calc(num_1,num_2,opr))
