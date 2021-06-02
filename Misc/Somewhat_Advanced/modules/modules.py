import pyjokes
from collections import Counter, defaultdict, OrderedDict

joke = pyjokes.get_joke("en", "neutral")
print(joke)

li = [1, 2, 3, 4, 4, 5, 5, 5, 5, 6]
print(Counter(li))

dict = {"a": 1, "b": 2}

dict2= defaultdict(lambda: "does not exist", {"a":1, "b":2})
print(dict2["c"])
