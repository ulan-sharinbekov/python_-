class Dog():
    def __init__(self, type, name, color):
        print(self, "class")
        self.name = name
        self.type = type
        self.color = color

dog1 = Dog("Alabai", "Sharik", "brown")
print(dog1, "code")
dog2 = Dog("Alabai", "Simba", "black")
print(dog2, "simba")