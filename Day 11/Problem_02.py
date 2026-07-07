class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof Woof!"

d = Dog("Buddy")
print(d.bark())  # Output: Buddy says Woof Woof!