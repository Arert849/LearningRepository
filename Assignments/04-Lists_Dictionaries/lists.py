fruits = ["banana", "apple", "banana", "cherry"]
print(fruits[1])    # "apple"  indexing starts at 0
print(fruits[-1])   # "cherry"  -1 is first in reverse order

fruits.append("orange")  # appends to the end of the list
print(fruits[-1])   # "orange"

fruits.remove("banana")  # Removes the first occurrence of "banana"
print(fruits)

fruits.pop()    # Removes the last index
print(fruits)

fruits.pop(0)   # Removes index 0
print(fruits)

fruits.clear()  # Empties the list
print(fruits)
