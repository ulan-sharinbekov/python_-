import math


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


circle1 = Circle(2, "red")

print(circle1.get_area())
