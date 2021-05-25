# def fib(n, memo={}):  # initialize memo dictionary
#
#     if n in memo:
#         return memo[n]
#     if n <= 2:
#         return 1
#
#     # why does this work?
#     memo[n] = fib(n - 1) + fib(n - 2)
#     print(memo)
#     return memo[n]
#
#
# print(fib(5))
# print(fib(7))
# print(fib(9))
# print(fib(10))
# print(fib(50))


from datetime import datetime
from time import sleep


def tester(time=datetime.now()):
    return time


for i in range(10):
    sleep(2)
    print(tester(), datetime.now())
