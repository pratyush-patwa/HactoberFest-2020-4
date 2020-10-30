num1 = float(input("Enter the first number: "))
op = input("Enter the operator +, -. *, /  ")
num2 = float(input("Enter the second number: "))


def calculate(op, num1, num2):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1 - num2
    elif op== "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Not a valid operator"

print(calculate(op, num1, num2))
