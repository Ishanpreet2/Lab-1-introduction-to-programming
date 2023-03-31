def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")
    return num1, num2, op
def displayResult():
    num1, num2, op = takeInput()
    if op == "+":
        result = num1 + num2
        formula = f"{num1} + {num2} = {resut}"
    elif op == "-":
        result = num1 - num2
        formula = f"{num1} - {num2} = {result}"
    elif op == "*":
        result = num1 * num2
        formula = f"{num1} * {num2} = {result}"
    elif op == "/":
        result = num1 / num2
        formula = f"{num1} / {num2} = {result}"
    else:
        formula = "Invalid operator entered!"
        result = None
    print(formula)
    print("Result:", result)
