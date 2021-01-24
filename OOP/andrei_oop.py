# private variables


class PlayerCharacter:

    def __init__(self, name="anonymous", age=0):
        if age > 18:
            # instance attributes
            self._name = name
            self._age = age

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
        return num1 * num2

    def run(self):
        print("run")
        return "done" + self._name


player1 = PlayerCharacter()
player2 = PlayerCharacter()


class User:

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Archer(User):
    pass


# wizard1 = Wizard("ajua", "velvet thunder")
# print(wizard.sign_in)


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Ajibola",
            "has_pets": False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 65

    # def __del__(self):
    #     print("deleteddddd")
    #     return

    def __call__(self):
        return "oh no no no no no"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])


# method resolution order

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())
