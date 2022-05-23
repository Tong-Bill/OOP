import os.path

class students():
    def __init__(self, fname, lname, number, gpa ):
        self.fname = fname
        self. lname = lname
        self.number = number
        self.gpa = gpa

    def getStudents(self):
        pass
    def findMaxStudent(self):
        pass

name = "students.txt"
if os.path.exists(name):
    f = open(name, "r")
    f.close()
else:
    print(f"The file {name} does not exist.")