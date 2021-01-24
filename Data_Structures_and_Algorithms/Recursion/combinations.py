# nCr= n!/(n-r)! r!

# 1. Using regular factorials
def fact(n):
    if n <= 1: return 1
    return n * fact(n - 1)


def comb(n, r):
    res = fact(n) // (fact(n - r) * fact(r))
    return res


# 2. Using Pascal's triangle
def comb_pascal(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return comb_pascal(n - 1, r - 1) + comb_pascal(n - 1, r)


print(comb(500, 2))
print(comb_pascal(500, 2))
