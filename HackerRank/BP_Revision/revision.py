# == is an equality test. checks just value
# "is" is an identity test. checks if they are the very same object

a = "hello bambi i am a man of means "
b = "hello bambi i am a man of means"

c = "hello1"
d = "hello2"

# when a new string is created, python first searches its memory to see if an exact string already exists. if it does
# exist, python stores the new variable in the same memory location. Hence they are essentially the same object
print(a is b)
print(id(a))
print(id(b))

print(c is d)
print(id(c))
print(id(d))
