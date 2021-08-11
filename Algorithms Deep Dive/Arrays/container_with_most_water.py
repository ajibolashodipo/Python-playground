# You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
# Find two lines which together with the x-axis forms a container that would hold the greatest amount of water.
# Return the area of water it would hold


# test cases
# [7,1,2,3,9]- 28
# [] - 0
# [7] -0
# [6,9,3,4,5,8]- 6*5=30, 8*4= 32

# # logical solution

# iterate through array using 2 pointers
# initialize max to be 0
# inside nested loop, perform multiplication and compare with running max
# print max at the end


# Brute Force Solution
# time O(n^2)
# space O(1)
def container(arr):
    max_area = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            area = min(arr[i], arr[j]) * (j - i)
            max_area = max(area, max_area)
    return max_area


# optimized solution:
# go through array once. noting that
# only the minimum of (grid[i], grid[j]) at any point defines whether or not the area changes

# time O(n)
# space O(1)
def container1(arr):
    i = 0
    j = len(arr) - 1
    max_area = 0
    while i < j:
        area = min(arr[i], arr[j]) * (j - i)
        max_area = max(area, max_area)

        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    return max_area


print(container([7, 1, 2, 3, 9]))
print(container1([7, 1, 2, 3, 9]))
