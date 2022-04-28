def flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def isOperator(c):
    return c in ("-", "+", "*", "/", "%", "^", "!", "_")


def getPriority(C):
    if C == "-" or C == "+":
        return 1
    elif C == "*" or C == "/" or C == "%":
        return 2
    elif C == "^" or C == "!":
        return 3
    elif C == "_":
        return 4
    return 0


def infixToPrefix(infix):
    operators = []
    operands = []

    for i in range(len(infix)):

        if infix[i] == "(":
            operators.append(infix[i])

        elif infix[i] == ")":
            while len(operators) != 0 and (operators[-1] != "("):
                op1 = operands[-1]
                operands.pop()
                op2 = operands[-1]
                operands.pop()
                op = operators[-1]
                operators.pop()
                tmp = [op, op2, op1]
                operands.append(tmp)
            operators.pop()
        elif not isOperator(infix[i]):
            operands.append(infix[i] + "")

        else:
            while len(operators) != 0 and getPriority(infix[i]) <= getPriority(
                operators[-1]
            ):
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = [op, op2, op1]
                operands.append(tmp)
            operators.append(infix[i])

    while len(operators) != 0:
        op1 = ""
        op2 = ""
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()

        op = operators[-1]
        operators.pop()

        tmp = [op, op2, op1]
        operands.append(tmp)
    return flatten(operands[-1])