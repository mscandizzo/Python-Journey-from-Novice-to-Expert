"""
Filtering using functions
"""

def is_multiple_of_five(n):
    return not n % 5


def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))


print(get_multiples_of_five(50))

"""
Advance Filtering using Lambda functions
"""

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))


print(get_multiples_of_five(50))
