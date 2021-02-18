# find the maximum of any contiguous subarray of size k

def max_sum_subarray_naive(arr, k):
    is_global = -100000
    for i in range(0, len(arr) - k + 1):
        is_sum = 0
        for j in range(i, i + k):
            is_sum += arr[j]
        if is_sum > is_global:
            is_global = is_sum
    return is_global


def max_sum_subarray_optimal(arr, target):
    max_sum = float("-inf")
    start = 0
    current = 0
    for end, val in enumerate(arr):
        current += val
        if end - start + 1 == target:
            max_sum = max(current, max_sum)
            # delete the first element and add the next in the array
            current -= arr[start]
            start += 1
    return max_sum


print(max_sum_subarray_naive([2, 5, 1, 12, 9, 6], 3))
print(max_sum_subarray_optimal([2, 5, 1, 12, 9, 6], 3))
