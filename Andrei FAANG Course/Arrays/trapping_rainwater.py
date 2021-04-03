# given an array of integers representing an elevation map where the width of
# each bar is 1, return how much rainwater can be trapped


def trapping_rainwater(arr):
    water = 0
    for index, val in enumerate(arr):

        # ignore first and last elements
        if index == 0 or index == len(arr) - 1:
            continue
        else:

            # ensure that index contains itself during left and right comparison. so worst case, it is equal to itself
            # thus making the if statement  on line 20 redundant
            left = max(arr[0:index + 1])
            right = max(arr[index:])
            mini = min(left, right)

            # check for boundedness
            # if left > val and right > val:
            wtr = mini - val
            water += wtr
    return water


def optimized_trapping(arr):
    total_water = 0
    # populate left array
    left = [0]*len(arr)
    left[0] = arr[0]
    for i in range(1, len(arr)):
        left[i] = max(arr[i], left[i - 1])

    # populate the right array from reverse
    right = [0]*len(arr)
    l = len(arr) - 1
    right[l] = arr[l]
    for j in range(l-1, -1, -1):
        right[j] = max(arr[j], right[j + 1])

    #     find the min of left and right index
    for i in range(len(arr)):
        mini = min(left[i], right[i])
        total_water += mini- arr[i]
    return total_water


arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(trapping_rainwater(arr))
print(optimized_trapping(arr))
