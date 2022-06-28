# Avoid using built in list structure for Stacks, it may have memory reallocation issues
from collections import deque

stack = deque()
expression = input("Enter expression: ")
items = expression.split(" ")
remove_value = "("
remove_value2 = ")"
items = [value for value in items if value != remove_value]
items = [value for value in items if value != remove_value2]
operators = ["+", "-", "*", "/"]

items[2], items[1] = items[1], items[2]
# Append() + pop() + Index()
# Moves middle operator to end in postfix form
items.append(items.pop(items.index(items[3])))
items[5], items[4] = items[4], items[5]

for x in items:
    if x not in operators:
        stack.append(x)
    else:
        operand1 = float(stack.pop())
        operand2 = float(stack.pop())

        if x == "+":
            stack.append(operand2 + operand1)
        elif x == "-":
            stack.append(operand2 - operand1)
        elif x == "*":
            stack.append(operand2 * operand1)
        elif x == "/":
            stack.append(operand2 / operand1)

print(stack[-1])

