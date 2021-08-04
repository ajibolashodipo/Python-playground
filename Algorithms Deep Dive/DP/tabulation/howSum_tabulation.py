def howSum(targetSum, numbers):
    # size of table based on input parameters
    table = [None] * (targetSum + 1)

    # seed initial value
    table[0] = []

    for i in range(len(table)):

        if table[i] is not None:

            for nums in numbers:
                if i + nums <= targetSum:
                    table[i+nums] = table[i].copy()
                    table[i+nums].append(nums)

    return table[targetSum]


print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(7, [2, 4], ))
print(howSum(8, [7, 2, 3, 5]))
