## Collection Arrays
A quick overview of properties for each array:
- List
    - Ordered
    - Changeable
    - Allows duplicate members
<br><br>
- Dictionary
    - Ordered
    - Changeable
    - Unique members
<br><br>
- Set
    - Unordered
    - Unchangeable
    - Un-indexed
    - Unique members
    - Hash table
<br><br>
- Tuple
    - Ordered
    - Unchangeable
    - Allows duplicate members

## Lists

Lists consist of several elements.
You can call an element by its index or iterate through the list.

    [Element_1, Element_2, Element_3]

An element can be assigned on pop. For instance:

    fruits = ["apple", "banana", "cherry", "orange"]

    x = fruits.pop() 
would assign 'x' to be "orange" and remove "orange" from the list. I don't know in what order. 
Can't think of a case where the order would matter though.

## Dictionaries
Dictionaries consist of a key paired with a value:
You can call on a value by its key, you can also iterate over the items of a dictionary in pairs.

    {key_1: value_1, key_2: value_2, key_3: value_3}

Unlike with lists; the key parameter in a dict.pop(key) is not optional.

dict.get(key, None) can assign a default value should the get fail

    fruit = {"apple":0, "banana":1, "cherry":2, "orange":3}
    x = fruit.get("kiwi", None)
Would assign None to the 'x' variable as the key "kiwi" does not exist.

On the other hand: 

    x = fruit["kiwi"]
Would raise a KeyError.

## Sets
A set is another one of Pythons built-in collection array.
A key feature of sets is that they use hash functions to check for membership.
To determine the membership in a list for instance you need to iterate over the list. Sets can pull it directly.

O(1) vs O(n) complexity.

    # List
    x = [0, 1, 2, 3, 4]
    if 4 in x:          # Will iterate over the entire list to get to 4.
        print(x)

    # Set
    x = {0, 1, 2, 3, 4}
    if 4 in x:          # Uses the hash table to search for 4 and finds it
        print(x)

On small scale it makes no real difference. 
On a bigger scale it's the difference between no time at all and a huge waste of time.
E.g. 0.5 seconds and 40 seconds or more. Massive data collections could take forever.

A set's members are unchangeable, but they can be removed and a new one added.