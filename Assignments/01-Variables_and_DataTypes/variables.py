# Integer
age = 25

# Float
price = 9.99

# String
name = "Alice"

# Boolean
is_student = True

# Print the types
print(type(age), type(price), type(name), type(is_student))

# Type Casting
a = int(9.99)  # converts the float to an integer, rounding down.
b = int("0")  # converts the string to an integer, if possible.
c = str(9.99)  # converts the float to a string
d = float(1)  # Converts the integer to float
e = float("9.99") # Converts the string to float if possible.
f = bool(-1)  # Converts to bool, everything, but 0, None, or empty obj will be True

# Print the types
print(type(a), type(b), type(c), type(d), type(e), type(f))
