
def addStudents():
    pass
def displayStudentInitials():
    fopen = open("students.txt", "r")
    content = fopen.read()
    print(content)
    print("Student #    Student-Initials")
    print("-----------------------------")
    print()
    print("-----------------------------")
    fopen.close()

def displayStudentGpas():
    pass
def menu():
    print("-----------------------------")
    print("Welcome to the Program Menu.")
    print("1. Display Student Initials")
    print("2. Display Student GPAs")
    print("3. Add Students")
    print("4. Exit Program")
    print("-----------------------------")
    userChoice = input("What action would you like to perform? ")
    return userChoice

def main():
    while True:
        if menu() == "1":
            displayStudentInitials()
        elif menu() == "2":
            displayStudentGpas()
        elif menu() == "3":
            addStudents()
        elif menu() == "4":
            return False
        else:
            print("Invalid action. Try again.")

main()