def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


hi_func= outer_function("hi")
bye_func= outer_function("bye")

hi_func()
bye_func()

