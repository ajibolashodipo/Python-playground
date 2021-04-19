# this is the naive solution btw. cos it uses linear search to find the start and end index of the target value

def search_range(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = (left + right) // 2
        found = arr[pivot]

        if found == target:
            break
            # return pivot
        elif found < target:
            left = pivot + 1
        else:
            right = pivot - 1

    if left > right:
        return [-1, -1]

    # pivot contains the first index value of target
    pre = pivot
    while pre >= 0 and arr[pre - 1] == target:
        pre -= 1

    # pivot contains the first index value of target
    post = pivot
    while post <= len(arr) - 1 and arr[post + 1] == target:
        post += 1

    return [pre, post]


print(search_range([1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9], 5))
