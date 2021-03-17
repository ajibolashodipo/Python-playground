# bubble sort

def bubbleSort(arr):
    l = len(arr)

    # for n elements in the array, we have n-1 passes
    for i in range(0, l - 1):

        # bubble sort is adaptive as well. means it can short circuit if array
        # is fully sorted. doing it in O(n) as opposed to typical O(n^2)

        # initialize flag to 0
        flag = 0
        for j in range(0, l - 1 - i):

            if arr[j] > arr[j + 1]:
                # swap
                swap(arr, j, j + 1)
                flag = 1
        # outside of the inner for loop, if flag remains zero, then we know that no swaps happened ergo list is sorted.
        # then we can break from the loop
        if flag == 0:
            break
    print(arr)


def swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]
    return


bubbleSort([1, 4, 7, 3, 8, 3, 6, 0, 3, 54, 7, 3, 6, 23])
