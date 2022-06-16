
class Calculator:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def getOperands(self):
        self.operand1 = input("First operand: ")
        self.operand2 = input("Second operand: ")

    def addition(self):
        return self.operand1 + self.operand2

    def subtraction(self):
        return self.operand1 - self.operand2

    def multiplication(self):
        return self.operand1 * self.operand2

    def division(self):
        return self.operand1 / self.operand2

class Complex:
    pass


def getCalcType():
    print("CALCULATOR MODES")
    print("===================")
    print("1.   Integer Calculator")
    print("2.   Floating Calculator")
    print("3.   Complex Calculator")
    print("0.   EXIT")
    return input()

def getOperation():
    pass

def integerCalculator():
    pass

def complexCalculator():
    pass

userChoice = getCalcType()
if int(userChoice) == 1:
    pass
elif int(userChoice) == 2:
    pass
elif int(userChoice) == 3:
    pass
elif int(userChoice) == 0:
    raise SystemExit
else:
    print("Invalid option.")
