class Student:

    id = 0
    #avg = 0
    def __init__(self,name):
        self.name = name
        self.grade = ''
        Student.id += 1
        print("Id :",Student.id)
        #print("Name : {}, Grade {}".format(self.name,self.grade))

    def marks(self,physics,chem,math):
        self.avg = (physics+chem+math)//3
        #print("Average of {} is {}:".format(self.name,avg))
        print("Average of %s is %s:"%(self.name,self.avg))

    def gradingSystem(self):
        if self.avg > 90:
            self.grade = 'A'
            print("Name : {}, Grade {}".format(self.name,self.grade))
        elif self.avg < 90 and self.avg > 75:
            self.grade = 'B'
            print("Name : {}, Grade {}".format(self.name,self.grade))
        elif self.avg < 75 and self.avg > 60:
            self.grade = 'C'
            print("Name : {}, Grade {}".format(self.name,self.grade))
        else:
            print("Not Eligible")


##ram = Student("Ram",'A')
##shyam = Student("Shyam",'B')

ram = Student("Ram")
ram.marks(65,55,76)
ram.gradingSystem()

shyam = Student("Shyam")
shyam.marks(90,78,88)
shyam.gradingSystem()
