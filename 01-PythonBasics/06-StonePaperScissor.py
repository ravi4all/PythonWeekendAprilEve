import random

a = ["stone","paper","scissor"]
b = random.choice(a)

counter = 0

while True:
    
    user_input = input("Enter your choice : ")

    if user_input == b:
        print("Match Tie")
    elif user_input == "stone" and b == "paper":
        print("CPU's",b,"beats your",user_input)
        counter -= 1
        print("Counter:",counter)
    elif user_input == "paper" and b == "scissor":
        print("CPU's",b,"beats your",user_input)
        counter -= 1
        print("Counter:",counter)
    elif user_input == "scissor" and b == "stone":
        print("CPU's",b,"beats your",user_input)
        counter -= 1
        print("Counter:",counter)

    elif user_input == "stone" and b == "scissor":
        print("CPU",b)
        print("Your's",user_input,"beats",b)
        counter += 1
        print("Counter:",counter)
    elif user_input == "paper" and b == "stone":
        print("CPU",b)
        print("Your's",user_input,"beats",b)
        counter += 1
        print("Counter:",counter)
    elif user_input == "scissor" and b == "paper":
        print("CPU",b)
        print("Your's",user_input,"beats",b)
        counter += 1
        print("Counter:",counter)

    b = random.choice(a)
