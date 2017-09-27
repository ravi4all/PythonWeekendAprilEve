class Car:
    a = 10
    b = 12
    c = a+b
    print("My first class...")
    print(c)

x = Car.a
print("Value of a inside class",x)

print(Car.b)
Car.b = 13
print(Car.b)
