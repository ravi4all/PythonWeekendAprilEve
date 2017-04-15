import random

def cpu_win(b,user_input,counter):
    print("CPU's",b,"beats your",user_input)
    print("Counter:",counter)

def you_win(b,user_input,counter):
    print("CPU",b)
    print("Your's",user_input,"beats",b)
    print("Counter:",counter)

def mainLoop():

    a = ["stone","paper","scissor"]
    b = random.choice(a)
    counter = 0
    
    while True:
        
        user_input = input("Enter your choice : ")

        if user_input == b:
            print("Match Tie")
        elif user_input == "stone" and b == "paper":
            counter -= 1
            cpu_win(b,user_input,counter)
        elif user_input == "paper" and b == "scissor":
            counter -= 1
            cpu_win(b,user_input,counter)
        elif user_input == "scissor" and b == "stone":
            counter -= 1
            cpu_win(b,user_input,counter)

        elif user_input == "stone" and b == "scissor":
            counter += 1
            you_win(b,user_input,counter)
        elif user_input == "paper" and b == "stone":
            counter += 1
            you_win(b,user_input,counter)
        elif user_input == "scissor" and b == "paper":
            counter += 1
            you_win(b,user_input,counter)

        b = random.choice(a)

mainLoop()
