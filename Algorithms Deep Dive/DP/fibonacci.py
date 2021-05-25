def fib(n, memo={}):  # initialize memo dictionary

    # check for existence
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    # memo-insertion logic.remember to pass memo in as an argument
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(5))
print(fib(7))
print(fib(9))
print(fib(10))
print(fib(50))
