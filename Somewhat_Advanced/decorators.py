# decorators super charge our functions

# steps:
# accepting a function
# defining a wrapper function
# calling accepted function in said wrapper
# returning the wrapper function

# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*******hhhh*******")
        func(*args, **kwargs)
        print("**************")

    return wrap_func


@my_decorator
def hello(greeting, emoji=":)"):
    print(greeting)


hello("hiiiii")

# without the decorator,
h1 = my_decorator(hello)
h1("serendipithelloooo")
