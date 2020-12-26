print(type("hello"))
x= 2**3**2
print(x)

a= "banana"
b= "banana"
print(a is b)

xs = [1,2,3,4,5]
for(i, val) in enumerate(xs):
    xs[i] = val**2
    print(type(xs))

print(xs)
