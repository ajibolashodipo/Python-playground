def canSum(targetSum, numbers):
    # visualize solution as a table

    # define a table size based on the inputs
    table = [False] * (targetSum + 1)  # +1 cos of zero-based index

    # seed trivial answers into the table
    table[0] = True

    # iterate through the table based on current position
    for i in range(len(table)):
        if table[i] is True:
            for num in numbers:
                if i + num <= targetSum:
                    # update further values
                    table[i + num] = True

    print(table[targetSum])
    return table[targetSum]


canSum(300, [7, 14])
