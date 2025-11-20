fruits = ["apple", "banana", "mango", "apple", "cherry"]

unique_fruit = set()

for fruit in fruits:
    if fruit in unique_fruit:
        print("Duplicate", fruit)
        break
    unique_fruit.add(fruit)
