# array has to be sorted btw
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]

        if curr < target:
            left += 1
        elif curr > target:
            right -= 1
        else:
            print("sum exist at index: " + str(left) + " , " + str(right))
            return
    print("sum does not exist")
    return


two_sum([1, 4, 6, 7, 9, 23], 13)
