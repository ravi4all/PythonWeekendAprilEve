import random

a = [1,2,3,4,5,6]
cpu = random.choice(a)
counter = 0

while True:
    
    user = int(input("Enter your num : "))
    print("CPU",cpu)
    
    if user == cpu:
        print("You're Out")
        print("Score is",counter)

    elif user != cpu:
        counter += user
        print("Score is",counter)

    else:
        print("CPU is Out")

    cpu = random.choice(a)
