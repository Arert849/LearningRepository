# Ranges are non-inclusive
for i in range(6):  # Starts at 0, ends at 3.
    print(i)    # Prints 0, 1, 2, 3, 4, 5

for i in range(2, 6):  # Starts at 1, ends at 3.
    print(i)    # Prints 2, 3, 4, 5

for i in range(0, 6, 2):
    print(i)    # Prints 0, 2, 4

fruits = ["apple", "banana", "cherry", "orange"]

for fruit in fruits:    # Iterate over the list
    print(fruit)        # Prints apple, banana, cherry, orange

for i, fruit in enumerate(fruits):      # Enumerates the list starting from 0.
    print(f"{fruit} is indexed at {i}")

fruits = {"apples": 5, "bananas": 3, "cherries": 8, "oranges": 3}

for key in fruits:  # Iterates of the dict keys
    print(key)

for key, value in fruits.items():   # Iterates over the item pairs in the dict
    print(f"There are {value} {key}")

for key in fruits:
    print(key)
    if key == "kiwi":
        break
else:
    print("The loop finished its iterations.")
