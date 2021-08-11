def partition(arr, lb, r):
    pivot = arr[lb]
    pivotIndex = lb

    left = lb
    right = r

    while left < right:
        print(left)

        # move the lb pointer and stop when grid[lb]> pivot (STRICTLY GREATER). this means the condition of the whilr
        # loop will be the opposite
        while arr[left] <= pivot:
            left += 1

        # decrement the right pointer to check for the other condition i.e stop when grid[r] < pivot. this means the
        # condition of the while loop will be the opposite
        while arr[right] > pivot:
            right -= 1

        # we only swap when the lb pointer is less than the right pointer btw
        if left < right:
            swap(arr, left, right)

    # finally we swap the element at the pivotIndex with that at the right pointer
    swap(arr, pivotIndex, right)

    # we return the right pointer. DO NOT FORGET THIS AS THE RIGHT POINTER IS THE PARTITION POINT
    return right


def swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]


def quickSort(arr, l=0, r=14):
    # this condition means that the sub-array to be sorted has more than one element
    if l < r:
        p = partition(arr, l, r)

        # call quickSort recursively on left and right sub-array.
        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, r)

    return arr


print(quickSort([1, 4, 7, 3, 8, 105, 3, 6, 0, 3, 54, 7, 3, 6, 23]))
