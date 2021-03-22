# algorithm is very fast. O(n). Only problem is that it takes up a lot of memory as we will see

def countSort(arr):
    # first find the maximum element of the array
    m = max(arr)
    l = len(arr)
    # initialize empty array of length m+1. m+1 cos of zero based indexing.
    temp = [0] * (m + 1)

    # traverse the unsorted list and update aux array based on frequency of occurrence of elements
    for i in arr:
        temp[i] += 1

    print(temp)

    # now update the original array
    k = 0
    for i in range(0, len(temp)):
        if temp[i] == 0:
            continue
        while temp[i] > 0:
            arr[k] = i
            temp[i] -= 1
            k += 1

    return arr


print(countSort([5, 5, 2, 2, 2, 3, 4]))
print(countSort([1, 4, 7, 3, 8, 19, 3, 6, 0, 3, 54, 7, 3, 6, 23]))
