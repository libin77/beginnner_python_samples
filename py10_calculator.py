from art import logo_calc


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo_calc)


def calculator():
    """Docstring: Take numbers and calculate based on
  choosen operators"""
    calculating = True
    num1 = float(input("First Number: "))
    for operators in operations:
        print(operators)

    while calculating:
        operation_symbol = input("choose operation symbol: ")
        num2 = float(input("Next number: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        opt = input(f"Type y to continue with {answer} ")
        if opt.lower() != "y":
            calculating = False
            calculator()


calculator()
