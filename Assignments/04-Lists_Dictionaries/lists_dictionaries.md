## Lists and Dictionaries

Lists consist of several elements.
You can call an element by its index or iterate through the list.

    [Element_1, Element_2, Element_3]

An element can be assigned on pop. For instance:

    fruits = ["apple", "banana", "cherry", "orange"]

    a = fruits.pop() 
would assign a to be "orange" and remove "orange" from the list. I don't know in what order. 
Can't think of a case where the order would matter though.

Dictionaries consist of a key paired with a value:
You can call on a value by its key, you can also iterate over the items of a dictionary in pairs.

    {key_1: value_1, key_2: value_2, key_3: value_3}

Unlike with lists; the key parameter in a dict.pop(key) is not optional.

dict.get(key, None) can assign a default value should the get fail

    fruit = {"apple":0, "banana":1, "cherry":2, "orange":3}
    a = fruit.get("kiwi", None)
Would assign None to the 'a' variable as the key 'kiwi' does not exist.

On the other hand: 

    a = fruit["kiwi"]
Would raise a KeyError.
