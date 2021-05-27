def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num

        # recursive call
        remainderCombination = bestSum(remainder, numbers, memo)

        if remainderCombination is not None:

            # equivalent of spread operator in js
            combination = [*remainderCombination, num]

            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    # after loop completes
    memo[targetSum] = shortestCombination
    return shortestCombination


print(bestSum(100, [1, 2, 5, 25], memo={}))  # very slow, before memoization
