def merge(arrA, arrB):
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


merge([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14])
