class Animal:

    def __init__(self, theNumLegs, theCall, theName):
        self.numLegs = theNumLegs
        self.call = theCall
        self.name = theName

    def speak(self):
        print("Method must be implemented in derived class")


class Dog(Animal):
    def __init__(self, theNumLegs, theCall, theName):
        super().__init__(theNumLegs, theCall, theName)

    # def speak(self):
    #     pass
    # print("I am a")


myDog = Dog(4, "Woof!", "Fido")
myDog.speak()
