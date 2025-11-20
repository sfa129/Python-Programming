str = "teeterabc"

for char in str:
    if str.count(char) == 1:
        print("Non-repeated character is:", char)
        break
        