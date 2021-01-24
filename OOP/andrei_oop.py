class PlayerCharacter:

    def __init__(self, name="anonymous", age=0):
        if age > 18:
            # instance attributes
            self.name = name
            self.age = age

    # Class attribute: defined in the class. doesnt change across different instances
    membership = True

    # class methods using decorators. they can be used without instantiating an object
    # cls gives you access to the class object
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # similar to class methods but we do not get access to the class object as a first argument
    # use static when we do not care about the class attributes/state
    @staticmethod
    def adding_things_2(num1, num2):
        return num1*num2



    def run(self):
        print("run")
        return "done" + self.name


player1 = PlayerCharacter()
player2 = PlayerCharacter()

print(PlayerCharacter.adding_things_2(3,6))
