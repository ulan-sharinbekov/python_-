class Car():
    def __init__(self, brand, model, color, type, oil):
        self.brand = brand
        self.model = model
        self.color = color
        self.type = type
        self.oil = oil

    def drive(self):
        print(self.model, "drive")

    def oil_check(self):
        if self.oil < 4:
            print("you need refill oil")
        else:
            print("your oil:", self.oil)

    def fill_oil(self):
        self.oil = 8
        print("your oil is",8)

car1 = Car("Audi", "A8", "black", "sidan", 4)
car2 = Car("Toyota", "Camry", "white", "sidan", 3)

car1.oil_check()
car2.oil_check()
car2.fill_oil()
car1.oil_check()