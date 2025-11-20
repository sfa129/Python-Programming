numbers = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, 7]

positive_count_num = 0
for num in numbers:
    if num > 0:
        positive_count_num += 1
print("Positive numbers count is:", positive_count_num)