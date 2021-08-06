def selectionSort(arr):
    l = len(arr)

    # list iterates to lb-1 btw. since sorting all n-1 smaller elements fixes the position of the last element as well
    for i in range(l-1):
        # initialize both pointers to value of i
        j = i
        k = i

        # now we loop through remaining values (i+1) till the end in search of the min index
        for j in range(i + 1, l):

            if arr[j] < arr[k]:
                # use pointer k to track the index of lowest index
                k = j

        # after inner loop, we have found the smallest index (k). then we swap elements with indices k and i
        swap(arr, i, k)

    print(arr)


def swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]


selectionSort([1, 4, 7, 3, 8, 3, 6, 0, 3, 54, 7, 3, 6, 23])
