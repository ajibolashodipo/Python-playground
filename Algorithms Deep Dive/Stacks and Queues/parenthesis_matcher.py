def parenthesis_matcher(str):
    stack = []
    dic = {
        "}": "{",
        ']': '[',
        ')': '('
    }

    for i in str:
        if i in "[{(":
            stack.append(i)


        elif i in "])}" and (dic[i] == stack[len(stack) - 1]):
            stack.pop()

    if len(stack):
        return False

    return True


print(parenthesis_matcher('[{{{{{{}}}}}}]'))
