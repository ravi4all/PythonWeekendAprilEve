class Car:
    """This is class and object demo"""
    color = 'red'
    speed = 250

audi = Car()
# print(type(audi))
print(audi.color, audi.speed)
print(audi.__class__)
print(audi.__doc__)

bmw = Car()
bmw.color = 'black'
bmw.speed = 200
print(bmw.color, bmw.speed)
