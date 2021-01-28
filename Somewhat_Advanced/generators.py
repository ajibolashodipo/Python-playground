# helps us generate a sequence over time using yield to pause and resume functions
# generates stuff one at a time without taking so much space in memory

def make_list(num):
    res = []
    for i in range(num):
        res.append(i * 2)
    return res


# my_list = make_list(100)
# print(my_list)


# iterable is any object we are able to loop through cos it has the dunder method __iter__
# iterate: act of taking an item from an iterable and doing something with it

# generator is a subset of an iterable

def generator_function(num):
    for i in range(num):
        yield i


# generators allow us to hold one item in memory at a time
# for item in generator_function(100):
#     print(item)


 g = generator_function(100)
# thing is yield pauses the function and comes back to it when next is called. yield keeps track of state
next(g)
next(g)
next(g)
next(g)
print(next(g))






