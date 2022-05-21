# In python, pointers do not exist
# Objects are passed to function by reference

def menu():
    print("-----------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit Program")

def addFraction():
    var1 = int(input("Enter first number: "))
    var2 = int(input("Enter second number: "))
    result = var1 + var2
    print(result)

def subFraction():
    var1 = int(input("Enter first number: "))
    var2 = int(input("Enter second number: "))
    result = var1 - var2
    print(result)

def multiplyFraction():
    var1 = int(input("Enter first number: "))
    var2 = int(input("Enter second number: "))
    result = var1 * var2
    print(result)

def divideFraction():
    var1 = int(input("Enter first number: "))
    var2 = int(input("Enter second number: "))
    result = var1 / var2
    print(result)

while True:
    menu()
    userChoice = int(input("Select an operation to perform: "))
    if userChoice == 1:
        addFraction()
    elif userChoice == 2:
        subFraction()
    elif userChoice == 3:
        multiplyFraction()
    elif userChoice == 4:
        divideFraction()
    elif userChoice == 5:
        raise SystemExit
    else:
        print("Invalid choice, try again.")
