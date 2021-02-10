# good for almost sorted lists. generally has bad performance though
def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        swaps = False
        for j in range(n - 1-i):
            if arr[j + 1] < arr[j]:
                swaps = True
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("printing")
        print(arr)
        if not swaps:
            # list is sorted
            return arr
    return arr


print(bubblesort([2, 4, 4, 5,45,23,89,31, 6, 7, 8]))
