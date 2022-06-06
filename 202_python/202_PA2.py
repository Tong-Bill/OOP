import os.path
global number, lname, fname, gpa
# Classes are an added complexity to a simple task like this one and not needed

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
    highest_gpa = max(gpa)
    position = gpa.index(highest_gpa)
    return position

def printStudentTable():
    print("  First   Last  Number")
    print("=======================")
    for e in zip(fname, lname, number):
        print("{:>7} {:>7} {:>7}".format(*e))

name = "students.txt"
if os.path.exists(name):
    number = []
    lname = []
    fname = []
    gpa = []
    student_count = getStudents()
    student_cell = findMaxStudent()
    printStudentTable()
    print(f"\nThe student with the highest gpa is: {fname[student_cell]} {lname[student_cell]}")
else:
    print(f"The file {name} does not exist.")