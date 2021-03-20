def partition(arr, lb, ub):
    # choose first element as pivot element
    pivot = arr[lb]

    # set partition limits
    start = lb
    end = ub

    while start < end:

        # keep incrementing the start pointer UNTIL current element is greater than pivot
        while arr[start] <= pivot:
            start += 1

        # keep decrementing the end pointer UNTIL current element is lower or equal than pivot
        while arr[end] > pivot:
            end -= 1

        # after finding the correct values of start and end, we then swap
        # as long as index of start is less than index of end
        if start < end:
            swap(arr, start, end)

    # when start becomes equal to end, we must break out of the big loop
    # and swap the end index with pivotIndex(lower bound, lb)
    swap(arr, lb, end)
    return end


def swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]


def quickSort(arr, lb=0, ub=14):
    if lb < ub:
        pivotIndex = partition(arr, lb, ub)
        quickSort(arr, lb, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, ub)
    return arr


print(quickSort([1, 4, 7, 3, 8, 105, 3, 6, 0, 3, 54, 7, 3, 6, 23]))
