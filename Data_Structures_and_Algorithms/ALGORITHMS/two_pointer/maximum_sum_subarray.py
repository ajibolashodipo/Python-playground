def maximum_subarray(arr):
    my_max = -10000
    l = len(arr)
    for i in range(0, l):
        my_sum = 0
        for j in range(i, l):
            my_sum += arr[j]
            print(i, j)

            if my_sum > my_max:
                my_max = my_sum

    return my_max


def kadane_algo(arr):
    global_max = -100000
    local_max = 0
    for i in arr:
        local_max = max(i, local_max + i)
        if local_max > global_max:
            global_max = local_max

    return global_max


print(maximum_subarray([2, 5, -3, 6, -10, -4]))
print(kadane_algo([2, 5, -3, 6, -10, -4]))
