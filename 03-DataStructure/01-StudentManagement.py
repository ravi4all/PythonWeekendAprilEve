studentList = []
#studentList = {}

def addStudent():

    roll_no = int(input("Enter the roll number : "))
    name = input("Enter the name of student : ")
    age = int(input("Enter the age of student : "))
    
    studentList.append([roll_no,name,age])

    for s in studentList:
        print(s)

    #print(studentList)

while True:

    print("""
    1 : Add Student,
    2 : Delete Student,
    3 : Update Student,
    4 : Read All Students,
    5 : Quit
    """)

    user_choice = int(input("Enter your choice : "))

    if user_choice == 1:
        addStudent()
    elif user_choice == 5:
        quit()

