def is_even(n: int) -> bool:
    """ Check if number is even """
    return n % 2 == 0


def addition(a, b):
    """ Add the numbers together"""
    return a + b


print(is_even(10))
print(addition(5, 5))


def avc(a: int) -> str:
    print("This will print")
    return a % 2 == 0

print(avc("str"))   # This will raise a TypeError, though not because of hinting.
