
class Calculator:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def getOperands(self):
        self.operand1 = input("First operand: ")
        self.operand2 = input("Second operand: ")

    def addition(self):
        return int(self.operand1) + int(self.operand2)

    def subtraction(self):
        return int(self.operand1) - int(self.operand2)

    def multiplication(self):
        return int(self.operand1) * int(self.operand2)

    def division(self):
        return int(self.operand1) / int(self.operand2)

class Complex:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def getOperands(self):
        self.operand1 = input("First operand: ")
        self.operand2 = input("Second operand: ")

    def addition(self):
        try:
            return int(self.operand1) + int(self.operand2)
        except:
            return self.operand1 + "+" + self.operand2

    def subtraction(self):
        try:
            return int(self.operand1) - int(self.operand2)
        except:
            return self.operand1 + "-" + self.operand2

    def multiplication(self):
        try:
            return int(self.operand1) * int(self.operand2)
        except:
            return self.operand1 + "*" + self.operand2

def getCalcType():
    print("CALCULATOR MODES")
    print("===================")
    print("1.   Integer Calculator")
    print("2.   Floating Calculator")
    print("3.   Complex Calculator")
    print("0.   EXIT")
    return input()

def getOperation():
    print("1.   Addition")
    print("2.   Subtraction")
    print("3.   Multiplication")
    print("4.   Division")
    return int(input())

def integerCalculator():
    opChoice = getOperation()
    set_operands.getOperands()
    if opChoice == 1:
        print(set_operands.addition())
    elif opChoice == 2:
        print(set_operands.subtraction())
    elif opChoice == 3:
        print(set_operands.multiplication())
    elif opChoice == 4:
        print(set_operands.division())
    else:
        print("Invalid operation.")

def complexCalculator():
    opChoice = getOperation()
    set_complex.getOperands()
    if opChoice == 1:
        print(set_complex.addition())
    elif opChoice == 2:
        print(set_complex.subtraction())
    elif opChoice == 3:
        print(set_complex.multiplication())
    elif opChoice == 4:
        print("This complex Calculator does not support division.")
    else:
        print("Invalid operation.")

def floatingCalculator():
    print("In python 3, integers are converted to floats as needed.")
    print("As a result, the standard integer calculator acts as a floating calculator when needed.")
    print("Redirecting to integer Calculator...")

userChoice = getCalcType()
set_operands = Calculator(None, None)
set_complex = Complex(None, None)
if int(userChoice) == 1:
    integerCalculator()
elif int(userChoice) == 2:
    floatingCalculator()
    integerCalculator()
elif int(userChoice) == 3:
    complexCalculator()
elif int(userChoice) == 0:
    raise SystemExit
else:
    print("Invalid option.")
