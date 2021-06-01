class Animal:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("say something")

class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def say(self):
        print("gaf")

dog1 = Dog("Sharik", "Alabai")
print(dog1.name)
print(dog1.type)
dog1.say()