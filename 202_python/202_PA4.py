

def getStudents():
    pass

def findMaxStudent():
    pass

def printStudentTable():
    pass

def getMenuChoice():
    print("STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1.   Display Students")
    print("2.   Add Courses")
    print("3.   Display Student Schedule")
    print("4.   Find Highest GPA Student")
    print("0.   EXIT")
    return input()

def getStudentOption():
    pass

def addCourses():
    pass

while True:
    if int(getMenuChoice()) == 1:
        pass
    elif int(getMenuChoice()) == 2:
        addCourses()
    elif int(getMenuChoice()) == 3:
        pass
    elif int(getMenuChoice()) == 4:
        findMaxStudent()
    elif int(getMenuChoice()) == 0:
        break
