# Single Level Inheritance

# Base Class/Parent Class
class Employee:

    def __init__(self):
        self.company = 'HCL'
        self.dept = 'IT'
        self.designation = 'Developer'

# Inheritance
# Sub Class/Child Class
class Emp_1(Employee):

    def __init__(self,id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        # Employee.__init__(self)
        super().__init__()

    def commonDetails(self):
        print("Common Details :",self.company,self.dept,self.designation)

    def personalDetails(self):
        print("Emp details :",self.id, self.name, self.salary)


class Emp_2(Employee):

    def __init__(self,id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        # Employee.__init__(self)
        super().__init__()

    def commonDetails(self):
        print("Common Details :",self.company,self.dept,self.designation)

    def personalDetails(self):
        print("Emp details :",self.id, self.name, self.salary)

obj_1 = Emp_1(1,'Ram',15000)
obj_1.commonDetails()
obj_1.personalDetails()

obj_2 = Emp_1(2,'Shyam',25000)
obj_2.commonDetails()
obj_2.personalDetails()
