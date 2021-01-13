def good_fibonacci(n):
    if n <= 1:
        return n, 0

    else:
        (a, b) = good_fibonacci(n - 1)
        return a + b, a


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


print(good_fibonacci(40))
print(bad_fibonacci(40))