def swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]


def partition(arr, left, right):
    # initialize two pointers i and j
    i = left
    j = left
    pivot = arr[right]
    while j < right:
        if arr[j] < pivot:

            # swap arr[i] and arr[j] and move both indexes
            swap(arr, i, j)
            j += 1
            i += 1

        # else just simply move j by 1
        else:
            j += 1

    # after loop is done, swap pivot with position f i
    swap(arr, i, right)

    return i


def quicksort(arr, left, right):
    if left < right:
        partitionIndex = partition(arr, left, right)
        quicksort(arr, left, partitionIndex - 1)
        quicksort(arr, partitionIndex + 1, right)

    # return arr


# print(quicksort([1, 4, 7, 3, 8, 105, 3, 6, 0, 3, 54, 7, 3, 6, 23], 0, 14))

def getKthLargest(arr, k):
    indexToFind = len(arr) - k
    quicksort(arr, 0, len(arr) - 1)
    return arr[indexToFind]


print(getKthLargest([1, 4, 7, 3, 8, 105, 3, 6, 0, 3, 54, 7, 3, 6, 23], 2))
