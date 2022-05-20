
def menu():
    print("-----------------------------")
    print("1. Display Student Initials")
    print("2. Display Student Gpas")
    print("3. Add Students")
    print("4. Exit Program")

def displayStudentInitials():
    f = open("students.txt", "r")
    lines = f.readlines()
    sid = []
    initial = []
    for x in lines:
        sid.append(x.split(" ")[0])
        initial.append(x.split()[2])
    print("Student # | Student Initials")
    for e in zip(sid, initial):
        print(*e)

def displayStudentGpas():
    f = open("students.txt", "r")
    lines = f.readlines()
    sid = []
    gpas = []
    for x in lines:
        sid.append(x.split(" ")[0])
        gpas.append(x.split(" ")[1])
    print("Student # | Student Gpas")
    for e in zip(sid, gpas):
        print(*e)

def addStudents():
    f = open("students.txt", "a+")
    num_students = int(input("How many students would you like to add? "))
    count = 0
    while count < num_students:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        sid = int(input("Input your student #: "))
        gpa = float(input("Input your Gpa: "))
        initial = input("Input your first & last initial: ")
        studentInfo = [str(sid) + " ", str(gpa) + " ", initial]
        f.writelines(studentInfo)
        count += 1
    f.close()

while True:
    menu()
    userChoice = int(input("Enter your option: "))
    if userChoice == 1:
        displayStudentInitials()
    elif userChoice == 2:
        displayStudentGpas()
    elif userChoice == 3:
        addStudents()
    elif userChoice == 4:
        raise SystemExit
    else:
        print("Invalid action, please try again.")