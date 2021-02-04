def isOperator(op):
    if op in ("+", "-", "*", "/"):
        return True
    return False


def postfix_evaluate(psfx):
    stack = []

    for el in psfx:
        if not isOperator(el):
            # push to stack
            stack.append(el)
        else:
            b = stack.pop()
            a = stack.pop()
            c = eval(f'{a}{el}{b}')
            # push evaluated value back into stack
            stack.append(c)

    print(stack[0])
    return stack[0]


postfix_evaluate("35*62/+4-")
