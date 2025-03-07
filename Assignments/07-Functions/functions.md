### Functions
Defining a function means you can call on it whenever needed rather than rewriting it.

Syntax:

    def func(arg):
        """ do something """        

You can add type hinting to the functions arguments or return value:

    def func(arg: int) -> int:
        """ do something """
        return var

It'll hint at the types it needs and the IDE should give a warning when the type is mismatched.
It's important to note that it's still just hinting not enforcement.
If a string is passed to the function it will NOT automatically raise a TypeError, but instead try to work with it.
