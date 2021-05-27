def howSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num

        # recursive call
        remainderResult = howSum(remainder, numbers, memo)

        if remainderResult is not None:
            # equivalent of spread operator in js
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]

    # if for loop returns none,
    memo[targetSum] = None
    return None


# print(howSum(7, [2, 3]))
# print(howSum(7, [5, 3, 4, 7]))
# print(howSum(7, [2, 4]))
# print(howSum(7, [2, 4], memo={}))
# print(howSum(8, [7,2, 3, 5],memo={}))
print(howSum(300, [7, 14],memo={}))  # very slow, before memoization
