number = 29
prime_number = True

if number > 1:
    for ranges in range(2, number):
        if (number % ranges) == 0:
            prime_number = False
            break
print(prime_number)