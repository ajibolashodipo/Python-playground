# map, filter, zip, reduce
from functools import reduce


# map
def multiply(el):
    return el * 2


res = list(map(multiply, [1, 3, 5]))
print(res)

# using lambda
a = list(map(lambda el: el * 2, [1, 3, 5]))
print(a)


# filter
def is_adult(el):
    return el >= 18


res1 = list(filter(is_adult, [1, 5, 26, 76]))
print(res1)

# zip
my_list = [1, 3, 5]
your_list = (10, 20, 30)
their_list = [4, 7, 9]
res2 = list(zip(my_list, your_list, their_list))
print(res2)

# reduce
my_list = [1, 3, 5, 7, 9]


def accumulator(acc, item):
    return acc + item


res3 = reduce(accumulator, my_list, 0)
print(res3)

# using lambda expressions
c = reduce(lambda acc, item: acc + item, my_list, 0)
print(c)

# lambda expressions: one time anonymous functions
# lambda param: action(param)


# comprehensions
# quick way to create lists and sets and stuff

# list comprehensions
# my_list= [param for param in iterable]

asd = [char for char in "hello"]
zx = [num for num in range(0, 100) if num % 2 == 0]
print(asd)
print(zx)

# set comprehensions
ert = {char for char in "ajibola"}
print(ert)

# dictionary comprehensions
simple_dict = {
    "a": 1,
    "b": 2
}
rty = {k: v ** 2 for k, v in simple_dict.items()}
print(rty)

ghj= {num: num**2 for num in [1,2,3]}
print(ghj)