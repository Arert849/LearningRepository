person = {
    "name": "Alice",
    "age": 7
}
print(person["name"])   # "Alice"
person["city"] = "Wonderland"
print(person)

person.pop("age")   # Removes the age out of the dictionary
print(person)

print(person.get("city"))   # returns the value assigned to the key
print(person.get("lastname", None))  # Returns the value assigned to the key or None if nothing is found

print(person.values())  # .values() returns a view object of the values.

print(person.items())   # .items() returns a view object of the key: value pairs

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
fruit_dict = dict.fromkeys(fruits, 0)   # Makes a dictionary with given keys and value
print(fruit_dict)

print(person["lastname"])
