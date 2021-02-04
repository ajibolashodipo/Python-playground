def isOperand(op):
    if op in ("+", "-", "*", "/"):
        return False
    return True


def precedence(op):
    if op in ("+", "-"):
        return 1
    elif op in ("*", "/"):
        return 2
    return 0


def convert(infix):
    stack = []
    postfix = []

    for el in infix:
        print(el)
        # check if current element is an operand
        if isOperand(el):
            postfix.append(el)
        else:
            # check if stack is empty
            if len(stack) == 0:
                stack.append(el)
            elif len(stack):
                # check for precedence
                if precedence(stack[-1]) < precedence(el):
                    # push to stack
                    stack.append(el)
                else:
                    # empty the stack since stack consists of members of equal or greater precedence
                    print("sff" + str(stack))
                    while stack:
                        postfix.append(stack.pop())

                    # then append el that prompted the stack pop to here. an empty stack
                    stack.append(el)
    # now empty what's left of the stack
    while stack:
        postfix.append(stack.pop())

    print(postfix)
    str_postfix = "".join(postfix)
    print(str_postfix)
    return str_postfix


convert("a+b*c-d/e")
