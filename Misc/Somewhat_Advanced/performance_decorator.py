from time import time


# Decorator
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} seconds')
        return result

    return wrapper


@performance
def long_time():
    print("1")
    for i in range(10000000):
        i * 5


@performance
def long_time2():
    print("2")
    for i in list(range(10000000)):
        i * 5


# with generators we get to not hold things in memory. range is an example of generator
long_time()
long_time2()
