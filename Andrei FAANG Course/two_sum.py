# given an array of integers, return the indices of the two numbers that add up to a given target

# brute force analysis: 2 for loops
# time- O(n^2)
# space- O(1)

def twoSum(arr, t):
    for i in range(len(arr)):
        numToFind = t - arr[i]
        for j in range(i + 1, len(arr)):
            if numToFind == arr[j]:
                return i, j
    return None


# Optimized solution 1
#  time - O(nlogn) cos of sorting
# space - O(1)
# only problem is that this guy changes the index. something to take note of

def optimizedTwoSum(arr, t):
    arr.sort()
    # initialize 2 pointers
    i = 0
    j = len(arr) - 1
    while i < j:
        mySum = arr[i] + arr[j]
        if mySum == t:
            return i, j
        elif mySum < t:
            i += 1
        else:
            j -= 1
    return None


# Optimized solution 2: using a hash map. lookups are constant time
# time- O(n)
# space - O(n)

def optimizedTwoSum2(arr, t):
    dic = {}

    # so the idea is this yeah. say you've got a current value of 2. And your target is 5.
    # you need to find if the hash map contains a 3 (5-2). if it does, return the index. else, add to hash map
    for i in range(len(arr)):
        val = arr[i]
        numToFind = t - val

        # check if numToFind exists in dictionary
        if numToFind in dic:
            print(dic)
            return dic[numToFind], i
        else:
            # if numtofind doesnt exist, add array value as key, and its index as value
            dic[val] = i

    return None


arr1 = [2, 1, 6, 3, 5]
print(twoSum(arr1, 4))
print(optimizedTwoSum(arr1, 4))
print(optimizedTwoSum2(arr1, 4))
