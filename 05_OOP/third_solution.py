class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Inheritance

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Safari", "90kWH")
print(my_electric_car.full_name())
print(my_electric_car.brand)
print(my_electric_car.battery_size)

