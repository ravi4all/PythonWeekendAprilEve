class Student:
    id = 0
    def __init__(self,name):
        self.name = name
        self.grade = 'A'
        Student.id += 1

class StudentMarks(Student):

    def __init__(self,name):
        super().__init__(name)
        print(self.name)

    def show_student(self):
        print("Student id {}".format(Student.id))
        print("Name is {} and grade is {}".format(self.name,self.grade))

obj = StudentMarks('Ram')
obj.show_student()

obj_2 = StudentMarks('Shyam')
obj_2.show_student()