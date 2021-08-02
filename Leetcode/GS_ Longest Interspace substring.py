def gap(a, b):
    return abs(ord(a) - ord(b))


def func(s, k):
    temp, maxi = "", ""
    for i in range(len(s) - 1):
        temp += s[i]
        print(temp)
        if gap(s[i], s[i + 1]) > k:
            maxi = maxi if len(maxi) > len(temp) else temp
            temp = ""
    return maxi


s = "ababbacaabbbb"

print(func(s, 1))





























