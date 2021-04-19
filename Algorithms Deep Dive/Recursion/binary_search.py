def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = (left + right) // 2
        found = arr[pivot]

        if found == target:
            return pivot
        elif found < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
