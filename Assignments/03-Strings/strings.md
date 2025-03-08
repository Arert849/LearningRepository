# Strings
 Some basic string methods and slicing.

## Methods
* ### Modifications
  - **.upper()**
    - Converts the string to upper case.
  <br><br>
  - **.lower()**
    - Converts the string to lower case.
  <br><br>
  - **.strip()**
    - Strips the string of leading and trailing whitespace.
    - Can be provided with a character parameter and will instead strip leading or trailing characters.
    - There's also **.lstrip()** and **.rstrip()** to only strip the string from left or right. 
  <br><br>
  - **.split()**
    - Splits the string, by default on whitespace
    - Can be provided a substring and will split the string based on the substring instead.
  <br><br>
  - **.replace(query, repl, n)**
    - Replaces the first occurrence of the query parameter with the repl parameter, n amount of times.
    - If parameter n is not provided, it replaces the first occurrence of the query.
    - Doesn't throw an error if query is not found, simply returns the string.
  <br><br>
  - **.join(iterable)**
    - This method constructs a string by separating the iterables with the string it attaches to.
    -     # Example
          text = ["some", "text", "here"]
          print("_".join(text))  # Prints "some_text_here"
          
* ### Booleans
  - **.startswith(substr)**
    - Returns True if the string starts with parameter substr.
  <br><br>
  - **.endswith(substr)**
    - Returns True if the string ends with parameter substr.
  <br><br>
  - **.isalnum()**
    - Returns True if the string is alphanumeric. (Contains only a-z, 0-9, case-insensitive)
  <br><br>
  - **.isalpha()**
    - Returns True if the string only contains character a-z case-insensitive.
  <br><br>
  - **.isdigit()**
    - Returns True if the string only contains numbers, 0-9.
* ### Indexing
  - **.find(substr, start, end)**
    - Searches the string for the substr parameter and returns its starting index if found.
    - The start and end parameters are optional, they indicate where to start and end the search.
    - Returns -1 if not found
    - **.rfind(substr)** searches in reverse
  - **.index(substr, start, end)**
    - Same as find, but raises a ValueError if not found.
    - **.rindex(substr)** also exists.

Not all string methods are covered, most of them self-explanatory or will be explained later.

In terms of string formatting there are f"" strings and the .format() method.

    text = "{name} is {age} years old and lives in {city}"
    print(text.format(name="Dorothy", age=11, city="Kansas"))
    
    name, age, city = "Alice", 7, "Wonderland"
    print(f"{name} is {age} years old and lives in {city}")

Both options format the string.
A lot of the time f"" strings will be sufficient. 

**.format()** method however remains useful in cases where placeholders need to be dynamically set.
Like forms, formatting templates, localization, translations.


## Slicing
Slicing refers to slicing the string by specifying a start index and an end index:

    text = "some text here"
    print(text[3:8])  # Prints "e tex"

Started at index 3 (Indexing starts at 0) and ended at index 8 (non-inclusive).
Not setting a start or end index defaults to beginning and end of the string.

A step can also be specified:

    print(text[3:8:2]  # Prints "etx" (3rd, 5th, and 7th index)

A negative step makes the slice go backwards instead.
Need to remember that beginning index needs to be higher than ending index since we're traversing in reverse.

    print(text[7:2:-1])  # Prints "xet e"
