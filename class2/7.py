class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.__year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year


car1 = Car("Audi", "A8", "white", 2010)

car1.year = 2009

print(car1.year)