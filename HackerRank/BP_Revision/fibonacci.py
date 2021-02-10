def fibonacci_iterative(n):
    if n < 2:
        return n

    a = 0
    b = 1
    for el in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


def fibonacci_recursion_bad(n):
    if n < 2:
        return n
    res = fibonacci_recursion_bad(n - 1) + fibonacci_recursion_bad(n - 2)
    return res


def fibonacci_recursion_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_recursion_memo(n - 1, memo) + fibonacci_recursion_memo(n - 2, memo)
    return memo[n]


print(fibonacci_iterative(40))

print(fibonacci_recursion_memo(40))

print(fibonacci_recursion_bad(40))