# Unlike C/C++, Python has inbuilt garbage collection & uses dynamic memory allocation
# This is why C++ is prone to memory leaks

class Team:
    def __init__(self, name, num_students):
        self.name = name
        self.num_students = num_students
        self.roster = []

    def getName(self):
        self.name = input("Team Name: ")
        return self.name

    def getNumStudents(self):
        self.num_students = int(input("How many students to add? "))
        return self.num_students

    def display(self):
        print(f"Team: {self.name} ")
        print("============================")
        for i in [self.roster[x:x+3] for x in range(0,len(self.roster),3) if x % 3 == 0]:
            print(*i)

class Student:
    def __init__(self, fName, lName, grade):
        self.fName = fName
        self.lName = lName
        self.grade = grade

    def getName(self):
        self.fName = input("First Name: ")
        self.lName = input("Last Name: ")
        self.grade = float(input("GPA: "))
        tInstance.roster.append(self.fName)
        tInstance.roster.append(self.lName)
        tInstance.roster.append(self.grade)

tInstance = Team(None, None)
sInstance = Student(None, None, None)
tInstance.getName()

max_Count = tInstance.getNumStudents()
count = 0
while count < max_Count:
    sInstance.getName()
    count += 1

tInstance.display()