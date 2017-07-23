try:
    file = open("demo.txt",'r')
    file.read()

except FileNotFoundError as f:
    print(f)

finally:
    # I will always execute
    print("Try to execute me")

print("Try me too")