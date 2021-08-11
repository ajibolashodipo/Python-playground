def insertionSort(arr):
    l = len(arr)

    # assume first element of array is sorted
    # hence our loop must begin from i=1  (as opposed to 0) through i= n.....remember there are just n-1 passes
    for i in range(1, l):
        # get element value at grid[i]
        x = arr[i]

        # initialize j from i-1. this makes sense since j cannot begin from i
        j = i - 1

        # now loop through the array till you find a new home for x
        # we check for j>-1 so that j does not proceed indefinitely or worse(negative indexing)
        while arr[j] > x and j > -1:
            # while these conditions are true, move element in j by one
            arr[j + 1] = arr[j]

            # decrement j
            j -= 1

        # when loop ends, insert i into j+1th position. this makes sense, pls think about it
        arr[j + 1] = x

    print(arr)


insertionSort([1, 4, 7, 3, 8, 3, 6, 0, 3, 54, 7, 3, 6, 23])
