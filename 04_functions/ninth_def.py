# yield return a value and memorize its state in memory that kahan tak kaam hua hai
def yield_function(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in yield_function(10):
    print(num)