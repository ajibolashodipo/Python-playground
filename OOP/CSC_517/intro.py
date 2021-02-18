class Person:
    # define the initializer
    def __init__(self, theName, theAge, theWeight, theHeight):
        self.name = theName
        self.age = theAge
        self.weight = theWeight
        self.height = theHeight

    def birthday(self):
        pass


# use the class person
p1 = Person("Alice", 21, 65.0, 165.0)
print(type(p1))
