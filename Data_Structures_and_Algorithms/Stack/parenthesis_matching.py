# Parenthesis matching

# ((a+b) * (c-d))

def parenthesis_matcher(str):
    stack = []
    for el in str:
        if el == "(":
            stack.append(el)
        elif el == ")":
            # check if stack is empty here. if yes, means parenthesis doesnt match.
            # reason: extra closing bracket
            if len(stack) == 0:
                print("Stack ain't empty bro. Parenthesis do not match")
                return False
            stack.pop()

    # now check if stack is empty. if stack is empty, parenthesis match. else, it doesnt
    if len(stack):
        # if stack is not empty after loop is done, means there is an extra opening bracket
        print("Stack not empty guy. Parenthesis do not match")
        return False
    # final condition
    else:
        print("Empty stack yayy. Parenthesis match")
        return True


test_string = "(((a*b)+(c*d)))"
parenthesis_matcher(test_string)
