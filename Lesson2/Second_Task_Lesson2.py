class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(self.make, self.model, self.year)

car1 = Car("Toyota", "Corolla", 2020)
car1.describe()