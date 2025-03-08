# Mutable vs Immutable Objects
In Python everything is an object and the object can be mutable or immutable.

The difference being that mutable objects can be changed after they're created. 

That means you can modify them without creating a new object.

Immutable objects cannot be changed after creation. When you alter a string, you don't modify the string object.
You make another string object with the new value.

Example:

    # Lists a mutable
    x = [1, 2, 3, 4]
    x[0] = 77
    print(x)  # Prints out [3, 2, 3, 4]

    # Strings are not
    x = "Some string"
    print(x[0])  # Will print out index 0 (S)
    x[0] = "P"  # Will throw a TypeError

### Mutable objects include:
- Lists
    - **[ele_1, ele_2, ele_3]**
- Dictionaries
    - **{key_1: val_1, key_2: val_2, key_3: val_3}**
- Sets
    - {ele_1, ele_2, ele_3}

### Immutable objects include:
- Strings
    - "Some string here"
- Tuples
    - (ele_1, ele_2, ele_3)
- Integers
    - 1, 2, 3, 4
- Floats
    - 1.0, 2.5, 3.9
- Booleans
    - True, False

It's important to know as this can affect performance and how you work with them.

Immutable object are simpler and allow for safer use, preventing accidental changes.

Mutable objects on the other hand can be updated which improves efficiency and performance.
Not necessarily important for smaller scripts, but larger datastructures could suffer.

### Identity and value:
If a variable refers to an immutable object, and you assign this variable to another.
They both refer to the same object.
If you then modify one of the variables 
they split as Python creates a new object with the new value for the modified variable.

Example:
    
    # Immutable
    x = 10      # x referts to integer object 10
    y = x       # y now refers to the same object as x
    x += 5      # x has changed and now refers to a new object
    print(x, y) # Prints out 15, 10

    # Mutable
    list_1 = [0, 1, 2, 3]   # list_1 refers to list object
    list_2 = list_1         # list_2 refers to the same list object
    list_1.append(4)        # append 4 to list_1 [0, 1, 2, 3, 4]
    print(list_1, list_2)   # Prints [0, 1, 2, 3, 4] twice