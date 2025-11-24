class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Fortuner")

car1.drive()
car2.drive()
