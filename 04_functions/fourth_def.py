import math

def circle_stats(radius):
    pi_value = round(math.pi, 3)
    print(pi_value)
    area = pi_value * radius ** 2
    circumference = 2 * pi_value * radius
    return area, circumference

a, c = circle_stats(45)
print("Area", a, "Circumference", c)
