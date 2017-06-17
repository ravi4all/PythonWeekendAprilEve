class Emp:
    # Docstring
    "This is my first class demo"

    id = 0
    name = ""
    age = 0

Emp.id = 101
Emp.name = "Ram"
Emp.age = 20


print("Id : {}, Name: {}, Age : {}".format(Emp.id,Emp.name,Emp.age))

emp_1 = Emp()
emp_2 = Emp()

emp_1.id = 101
emp_2.id = 102

print("Emp_1",emp_1.id)
print("Emp_2",emp_2.id)
