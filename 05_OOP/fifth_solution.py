# Polymorphism
# how many times instances of the class have made
class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

# Inheritance

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Battery"

my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())
my_electric_car = ElectricCar("Tesla", "Safari", "90kWH")
print(my_electric_car.fuel_type())

print(Car.total_cars)


