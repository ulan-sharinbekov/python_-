
class Dog:
    count = []
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.nomer = len(self.count)
        self.count.append(1)

    # def add_trick(self, trick):
    #     self.tricks.append(trick)

dog1 = Dog("Sharik", "Alabai")
dog2 = Dog("Simba", "Alabai")
dog3 = Dog("Laika", "Alabai")
print(dog1.nomer)
print(dog2.nomer)
print(dog3.nomer)
# dog1.add_trick("roll over")
# dog2.add_trick("play dead")
#
# print(dog2.tricks)
# print(dog1.tricks)

