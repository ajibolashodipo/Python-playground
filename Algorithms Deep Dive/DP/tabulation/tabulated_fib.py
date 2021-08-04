# tabulated fibonacci

def tabulated_fibonacci(n):
    table = [0] * (n + 1)
    table[1] = 1

    # for i in range(n + 1):
    #     try:
    #         table[i + 1] += table[i]
    #         table[i + 2] += table[i]
    #
    #     # handle index error exception
    #     except IndexError:
    #         pass
    #
    # print(table)

    for i in range(n + 1):

        # out of bounds checks. makes sense

        if i + 1 < n + 1:
            table[i + 1] += table[i]
        if i + 2 < n + 1:
            table[i + 2] += table[i]

    print(table)


tabulated_fibonacci(8)
