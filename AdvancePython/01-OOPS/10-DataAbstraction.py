class A:
    _x = 10
    __y = 12

    def __get__(self):
        self._x = "Changing value of x"
        return self._x
    def __set__(self):
        self.__y = "Changing value of y"
        return self.__y


obj = A()
# print("Value of x is {} and y is {}".format(obj.x, obj.y))
#
# obj.x = 12
# obj.y = 11
# print("Value of x is {} and y is {}".format(obj.x, obj.y))
#
# print("Value of x is {} and y is {}".format(A.x, A.y))
print(obj.__get__())
print(obj.__set__())

# obj._x = "Hello"
# obj.__y = "World"
# print("Value of x is {} and y is {}".format(obj._x, obj.__y))
#
# print("Object id",id(obj._x), id(obj.__y))
# print("Class id",id(A._x), id(A.__y))

print(obj._x)
