a = 16
try:
    # Logic
    b = a/0
    print(b)

except ZeroDivisionError as e:
    # Exception
    print("Try Again because",e)