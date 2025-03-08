text = "    Hello, Python!    "

print(text.strip())     # Removes leading and trailing spaces
print(text.upper())     # Converts to upper case
print(text.lower())     # Converts to lower case
print(text.replace("Python", "World"))  # Replaces the first substring with the second. (Python with World)
print(text.split(","))  # Splits the text at ',' returns a list ['    Hello,', ' Python!    ']
print(text.split())     # By default, splits at space hence trailing and leading spaces are gone in the list.

# Formatted strings
name = "Alice"
age = 7
city = "Wonderland"

print("{} is {} years old and lives in {}".format(name, age, city))  # Formats the string with the variable.
print(f"{name} is {age} years old and lives in {city}")  # Directly formats the string
