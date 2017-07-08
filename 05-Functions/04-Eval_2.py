def calc(x,y,opr):

    return eval('x'+opr+'y')


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

    opr = todo.get(user_choice)

    print(calc(num_1,num_2,opr))
