# given an array of integers representing an elevation map where the width of
# each bar is 1, return how much rainwater can be trapped


def trapping_rainwater(arr):
    water = 0
    for index, val in enumerate(arr):

        # ignore first and last elements
        if index == 0 or index == len(arr) - 1:
            continue
        else:
            left = max(arr[0:index])
            right = max(arr[index + 1:])
            mini = min(left, right)

            # check for boundedness
            if left > val and right > val:
                wtr = mini - val
                water += wtr
    return water


arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(trapping_rainwater(arr))
