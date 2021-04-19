def question2(s):
    lst = list(s.upper())
    s1 = ""

    while len(lst) > 0:
        for j in ["W", "D", "L"]:
            if j in lst:
                s1 += j
                lst.remove(j)
    return s1


print(question2("ldwdl"))


def countArithmeticMeans(a):
    res = 0
    arr = [0] * (len(a) + 2)
    for i in range(1, 1 + len(a)):
        arr[i] = a[i - 1]
    for j in range(1, len(arr) - 1):
        if arr[j - 1] + arr[j + 1] == 2 * arr[j]:
            res += 1

    return res
