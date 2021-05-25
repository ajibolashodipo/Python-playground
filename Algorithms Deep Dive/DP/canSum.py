
def canSum(targetSum, numbers, memo={}):
    print(memo)
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in numbers:
        # print(num)
        remainder = targetSum - num

        # check if function call returns true
        if canSum(remainder, numbers, memo):  # if this returns true
            memo[targetSum] = True

            return True

    memo[targetSum] = False

    return False


# works individually but dictionary doesn't clear between function calls.
# so it doesnt return an accurate result if it all runs at once. take note

print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
# print(canSum(8, [7,2, 3, 5]))
# print(canSum(300, [7, 14]))  # very slow
