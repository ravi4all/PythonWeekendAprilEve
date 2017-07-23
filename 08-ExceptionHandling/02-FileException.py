try:
    file = open("demo.txt",'r')
    file.read()

except FileNotFoundError as f:
    print(f)