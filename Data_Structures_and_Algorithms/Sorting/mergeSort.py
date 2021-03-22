

def mergeSort(arr, l, h):
    # base case: if index of left is less than index of right, it means moer than one element exists.
    # that's our cue to proceed
    if l < h:

        # find index of midpoint
        mid = (l + h) // 2

        # recurse using lower index and mid index
        mergeSort(arr, l, mid)

        # recurse using mid index to last index
        mergeSort(arr, mid + 1, h)

        # merge the two arrays (lower to mid) and (mid+1 to high)
        merge(arr, l, mid, h)

    return arr


print(mergeSort([8, 2, 9, 6, 5, 3, 7, 4], 0, 7))


# merge a single list made up of 2 individually sorted arrays
def merge(arrA, l, mid, h):

    # copy content of original array
    arrC = arrA.copy()

    # initialize variables
    a = l
    b = mid + 1
    k = l

    print(arrA)
    print(l, mid, h)
    while a <= mid and b <= h:
        if arrC[a] < arrC[b]:
            arrA[k] = arrC[a]
            a += 1
            k += 1
        else:
            arrA[k] = arrC[b]
            b += 1
            k += 1

    # to take care of the remainder values when either array reaches its end
    # only one of these gets to run cos only one gets to be true
    while a <= mid:
        arrA[k] = arrC[a]
        a += 1
        k += 1

    while b <= h:
        arrA[k] = arrC[b]
        b += 1
        k += 1

    print(arrA)
    print("-----------------")


# merge([1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12, 14, 16, 18], 0, 5, 14)


# merge 2 distinct lists to a bigger list
def merge2(arrA, arrB):
    arrC = []
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            arrC.append(arrA[a])
            a += 1
        else:
            arrC.append(arrB[b])
            b += 1

    # to take care of the remainder values when either array reaches its end
    # only one of these gets to run cos only one gets to be true
    while a < len(arrA):
        arrC.append(arrA[a])
        a += 1

    while b < len(arrB):
        arrC.append(arrB[b])
        b += 1

    print(arrC)
    return arrC

# merge2([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14])
