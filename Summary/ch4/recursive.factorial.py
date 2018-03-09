def factorial(n):
    if n in (0, 1):  # base case
        return 1
    return factorial(n - 1) * n  # recursive case


print([factorial(n) for n in range(10)])


from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(1, n + 1), 1)


f5 = factorial(5)  # f5 = 120
print(f5)
print([factorial(k) for k in range(10)])


def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result

f5 = factorial(5)  # f5 = 120
print(f5)
