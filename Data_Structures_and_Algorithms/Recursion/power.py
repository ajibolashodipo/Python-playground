def my_power(m, n):
    if n == 0:
        return 1
    else:
        return my_power(m, n - 1) * m


def my_power_2(m, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return my_power_2(m * m, n / 2)
    else:
        return m * my_power_2(m * m, (n-1) // 2)


# print(my_power(2, 5))
print(my_power_2(2, 5))
