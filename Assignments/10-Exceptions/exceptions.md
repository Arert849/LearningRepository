## Exceptions
Wrapping a function in:

    try:
        """ do something """
    except Exception:
        """ do something if an exception occurred """
    finally:
        """ Do something at the end """

Lets us catch, control, log, and debug errors. It can be more specific than simply "Exception",
as there are many types of exceptions.

Short list:
- FileNotFound
  - raised when a specified file could not be found.
- IndexError
  - raised when a specified index is out of range for the obj
- TypeError
  - raised when attempting an operation on an object of wrong type.
  - e.g. attempting to add a string and an integer.
- AssertionError
  - raised when an assert statement fails

There are many others and they can be manually raised:
    
    a, b = 10, "2"
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both values must be numbers.") 

        return a + b

    except TypeError as e:
        print(e)  # Prints "Both values must be numbers."

    finally:
        print("The function has ended")

It's worth noting that "Exception" catches every exception and could be added as the last except statement to catch
unexpected errors.

    try:
        with open(file, "r") as file:
            """ do something """
    except Exception as e:
        print(f"Unexpected ERROR: ({type(e).__name__}) {e}")

Let's say the file does not exist, this will print out:
"Unexpected ERROR: (FileNotFound) [Errno 2] No such file or directory: 'filename'"
