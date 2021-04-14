def brackets_to_remove(str):
    stack = []
    arr = list(str)
    for k, v in enumerate(arr):
        if v == "(":
            stack.append(k)

        # check if stack is empty
        elif v == ")" and len(stack) == 0:
            # delete specific index from track arr
            # you shouldn't delete from the array as this will mess with the index.
            # replace with an empty string instead
            arr[k] = ""

        elif v == ")" and len(stack):
            # pop from stack
            stack.pop()

    # at the end of array, delete indices that remain in the stack. they are extraneous
    for el in stack:
        # again don't be tempted to delete. we need the indices intact
        arr[el] = ""

    # then convert back to a string
    s = "".join(arr)
    return s

