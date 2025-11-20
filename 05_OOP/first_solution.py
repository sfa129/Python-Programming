class Car:
    def __init__(self, brand, model, name):
        self.brand = brand
        self.model = model
        self.name = name

new_car = Car("Toyota", 1999, "Corolla")
print(new_car.brand)
print(new_car.model)
print(new_car.name)