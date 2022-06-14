import student
text_file = "students.txt"
number_list = []
fname_list = []
lname_list = []
gpa_list = []

def getStudents():
    try:
        count = 0
        with open(text_file, "r") as f:
            for x in f.readlines():
                parts = x.strip().split()
                new_student = student.Student(parts[0], parts[2], parts[1], parts[3])
                number_list.append(new_student.number)
                lname_list.append(new_student.lastName)
                fname_list.append(new_student.firstName)
                gpa_list.append(new_student.gpa)
                count += 1
            return count
    except:
        print(f"The file {text_file} could not be opened.")
        raise SystemExit

def findMaxStudent():
    highest_gpa = max(gpa_list)
    highest_index = gpa_list.index(highest_gpa)
    highest_fname = fname_list[highest_index]
    highest_lname = lname_list[highest_index]
    return str(highest_fname), str(highest_lname)

def printStudentTable():
    print("First    Last    Number")
    print("=========================")
    for e in zip(fname_list, lname_list, number_list):
        print("{:8} {:7} {}".format(*e))

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
    print("Option   First   Last")
    print("=========================")

def addCourses():
    pass

while True:
    userChoice = int(getMenuChoice())
    if userChoice == 1:
       num_students = getStudents()
       printStudentTable()
    elif userChoice == 2:
        pass
    elif userChoice == 3:
        pass
    elif userChoice == 4:
        highest_name = findMaxStudent()
        print("The student with the highest gpa is: " + highest_name[0] + " " + highest_name[1])
    elif userChoice == 0:
        break
