x = 0


def func(n):
    if n > 0:
        global x
        x += 1
        print(x)
        return func(n - 1) + x

    return 0


print(func(3))
