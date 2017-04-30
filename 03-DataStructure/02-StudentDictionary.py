#studentList = []
studentList = {}
result = []

def addStudent():

    roll_no = int(input("Enter the roll number : "))
    name = input("Enter the name of student : ")
    age = int(input("Enter the age of student : "))

    studentList['roll_no'] = roll_no
    studentList['name'] = name
    studentList['age'] = age

    result.append(studentList.copy())
    
    #studentList.append([roll_no,name,age])

    for s in result:
        print(s)

    #print(studentList)

def deleteStudent():
    to_delete = int(input("Enter roll no of student :"))

    #index_of_to_delete = result.index(to_delete)
    del(result[to_delete-1])

def updateStudent():
    pass

def readStudent():
    for s in result:
        print(s)


def errHandler():
    print("You have pressed something wrong")

while True:

    print("""
    1 : Add Student,
    2 : Delete Student,
    3 : Update Student,
    4 : Read All Students,
    5 : Quit
    """)

    toDo = {
        "1" : addStudent,
        "2" : deleteStudent,
        "3" : updateStudent,
        "4" : readStudent,
        "5" : quit
        }

    user_choice = input("Enter your choice : ")

    toDo.get(user_choice,errHandler)()

##    if user_choice == 1:
##        addStudent()
##    elif user_choice == 5:
##        quit()

