def bestSum(targetSum, numbers):
    arr = [None] * (targetSum + 1)

    arr[0] = []

    for i in range(len(arr)):

        if arr[i] is not None:

            for num in numbers:
                # check against array bound shit
                if i + num <= targetSum:

                    # store the current value and potential new value in a variable
                    old = arr[i + num]
                    new = [*arr[i], num]

                    # first condition accounts for case of None
                    if arr[i + num] is None or len(old) > len(new):
                        arr[i + num] = new
                    else:
                        arr[i + num] = old

    print(arr[targetSum])
    return arr[targetSum]


print(bestSum(100, [1, 2, 5, 25]))
