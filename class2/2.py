class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type


dog1 = Dog("Sharik", "Alabai")
print(dog1.name)
print(dog1.type)