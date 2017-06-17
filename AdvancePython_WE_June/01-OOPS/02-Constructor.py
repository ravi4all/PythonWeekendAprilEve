class Emp:

##    id = 0
##    name = ""
##    age = 0
    counter = 0

    def __init__(self,id,name,age):
        self.id = 0
        self.name = ""
        self.age = 0
        Emp.counter += 1
        print("Object Counter",Emp.counter)
        print("Id : {}, Name: {}, Age : {}".format(id,name,age))
    
##    def bio(self,id,name,age):
##        print("Id : {}, Name: {}, Age : {}".format(id,name,age))

    def salary(self,sal):
        print("Salary is",sal)

#Emp.counter = 0

emp_1 = Emp(101,"Ram",20)
emp_2 = Emp(102,"Shyam",22)

#emp_1.bio(101,"Ram",20)
emp_1.salary(12000)
