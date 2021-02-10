def insertion_sort(arr):
    for i in range(1, len(arr)):
        # hold value of current
        current = arr[i]
        for j in range(i - 1, -2, -1):
            if current >= arr[j]:
                break

            else:
                arr[j + 1] = arr[j]

        arr[j + 1] = current
        print(j)
    return arr


print(insertion_sort([1, 3, 5, 4, 6, 7, 2, 9, 0, 2, 0, 1, 2, 7, 4, -2]))
