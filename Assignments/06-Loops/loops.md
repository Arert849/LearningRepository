### For loops

For loops iterate over an object or a range. The range() is non-inclusive and starts at 0 unless otherwise specified.

    for i in range(start, stop, step):
        """ do something """

Only the stop parameter is mandatory.

It's possible to iterate directly over an object

    fruits = ["apple", "banana", "cherry", "orange"]
    
    for fruit in fruits:
        """ do something """
        
### While loops
While loops will continue to iterate until the condition is fulfilled or the loop is broken.

    a = 0
    while a < 10:
        a += 1
        print(a)

This loop will continue to run until 'a' >= 10

    while True:
        """ do something """

This loop will continue to run until manually broken.
Previously mentioned in conditionals that for loops can have an else statement.
As can while loops:

    a = 0
    while a < 10:
        a += 1
        if a == 7:
            break
    else:
        print("Will not print as break is called")
It's worth keeping in mind. Though... I don't really use it.
