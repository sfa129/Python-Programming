# Encapsulation
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_model(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.full_model())
# print(my_car.model)