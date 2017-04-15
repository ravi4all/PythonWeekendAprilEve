import random

while True:

    a = ["Hi","Hello","Hey","Wass up","Namaste","Heya","Hola","Hie"]
    b = random.choice(a)
    user_message = input("Enter your message: ")
    print("Your Message",user_message)
    print("Bot Message",b)
