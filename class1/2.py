class Dog():
    def __init__(self, type, name, color):
        print(self, "class")
        self.name = name
        self.type = type
        self.color = color

    def eat(self):
        print(self.name, "eating")

    def play(self):
        print(self.name, "playing")


dog1 = Dog("Alabai", "Sharik", "brown")

dog2 = Dog("Alabai", "Simba", "black")
dog1.play()
dog2.eat()