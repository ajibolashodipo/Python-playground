import random

import collections as c
# rng = random.Random()
rng = random
dice_throw = rng.randrange(1, 7)
delay = rng.random() * 5.0

for i in range(5):
    delay = rng.random() * 5.0
    print(delay)


list1 = ['x','y','z','x','x','x','y', 'z']
res= c.Counter(list1)
print(res)
print(res["x"])

