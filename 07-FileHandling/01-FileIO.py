# file = open('demo.txt', 'w')
# str = "This file is written with a script"
# file.write(str)

# file = open('demo.txt', 'r')
# r = file.read()
# print(r)

# file = open("demo.txt", 'w')
# str = "Write me too in this file"
# file.write(str)

file = open("demo.txt", 'a')
str = "\nI am gonna append...."
file.write(str)