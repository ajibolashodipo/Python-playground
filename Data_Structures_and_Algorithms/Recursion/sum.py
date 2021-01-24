def my_sum(n):
    if n == 0:
        return 0
    else:
        return my_sum(n - 1) + n


print(my_sum(7))
