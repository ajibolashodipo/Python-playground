# O (n^3) complexity
def three_sum_naive(arr, target):
    l = len(arr)
    for i in range(0, l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                my_sum = arr[i] + arr[j] + arr[k]
                print(i, j, k, my_sum)
                if my_sum == target:
                    print("numbers exist")
                    return [i, j, k]
    return "sum does not exist within array"


def two_sum(i, arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]

        if curr < target:
            left += 1
        elif curr > target:
            right -= 1
        else:
            print("sum exist at index: " + str(arr[left]) + " , " + str(arr[right]) + " , " + str(i))
            return True
    return False


# O(n^2) complexity
def three_sum_optimal(arr, target):
    # iterate through the array once to reduce the problem to a two-sum type
    l = len(arr)
    # so that i stops with enough room for last two sum
    for i in range(0, l - 2):
        new_target = target - arr[i]
        # new reduced array
        sliced = arr[i + 1:]
        res = two_sum(arr[i], sliced, new_target)
        if res:
            return "shit exists"
    return "Sum does not exist"


# print(three_sum_naive([1, 2, 3, 5, 12], 19))
print(three_sum_optimal([1, 2, 3, 5, 12], 19))
