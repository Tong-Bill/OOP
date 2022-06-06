import os.path
global number, lname, fname, gpa
# Classes are not helpful for this particular assignment in python

def getStudents():
    with open(name, "r") as f:
        lines = f.readlines()
        count = 0
        for x in lines:
            number.append(x.split(" ")[0])
            lname.append(x.split(" ")[1])
            fname.append(x.split(" ")[2])
            gpa.append(x.split()[3])
            count += 1
        return count

def findMaxStudent():
    highest_gpa = 0
    for x in gpa:
        if x > x-1:
            highest_gpa = x
    print(highest_gpa)

def printStudentTable():
    pass

name = "students.txt"
if os.path.exists(name):
    number = []
    lname = []
    fname = []
    gpa = []
    student_count = getStudents()
    findMaxStudent()

else:
    print(f"The file {name} does not exist.")