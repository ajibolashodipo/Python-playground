def merge(arr, l, mid, r):
    # merge sort uses extra space. so copy the array without guilt :))
    # be careful with the slice index. very easy to get it wrong.
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]

    print("left and right")
    print(left)
    print(right)
    temp = []

    # initialize counter variables i and j
    i = 0
    j = 0

    # initialize index that helps modify the array to be sorted
    k = l

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    # check for extra elements
    while i < len(left):
        temp.append(left[i])
        i += 1

    while j < len(right):
        temp.append(right[j])
        j += 1

    # copy values from temp back into arr
    for i in range(len(temp)):
        arr[k] = temp[i]
        # print(k)
        k += 1

    return arr


def mergeSort(arr):
    left = 0
    right = len(arr) - 1

    def mergeHelper(arr, l, r):
        # this condition means the sub-array has more than one element
        if l < r:
            # find middle index and round down
            mid = (l + r) // 2
            # recurse on left and right sub-arrays (post-order traversal)
            mergeHelper(arr, l, mid)
            mergeHelper(arr, mid + 1, r)

            # merge sub-arrays accordingly
            merge(arr, l, mid, r)

    # call helper function
    mergeHelper(arr, left, right)
    return arr


print(mergeSort([8, 2, 9, 6, 5, 3, 7, 4]))
