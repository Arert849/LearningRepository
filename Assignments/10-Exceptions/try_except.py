def addition(a, b):
    """ Attempt to add a and b """
    try:
        print(a + b)

    except TypeError as e:
        print(e)  # Will print the TypeError if it's raised


def concatenate(a, b):
    """ Concatenate the strings if a is longer than b """
    try:
        assert len(a) > len(b), "a is shorter than b"
        print(a + b)

    except AssertionError as e:
        print(e)  # prints "a is shorter than b" if the assertion fails and raises the error


def division(a, b):
    """ Attempts to divide a by b """
    try:
        print(a / b)

    except Exception as e:
        print(F"Unexpected ERROR: ({type(e).__name__}) {e}")  # Will print 'Unexpected ERROR: (ExceptionType) exception'


concatenate("a", "abc")
addition(1, "2")
division(10, 0)


