## Variables & Data Types

### Python data types:
- **Integers ('int')** → Whole numbers; positive and negative.
- **Floats ('float')** → Decimal numbers; positive and negative. Python floats have built in double precision.
- **Strings ('str')** → Text, python supports both single and double quotes.
- **Booleans ('bool')** → True, False.
- **None ('NoneType')** → Absence of value. Not to be confused with undefined variables.

Python variables are assigned dynamically:

    x = 10   # Is sufficient to declare an integer.
    x = 1.0  # Is sufficient to declare a float.

All variables in python are Truthy.

For instance empty strings return False in an if statement. Non-empty return True

Same for empty and non-empty lists, dictionaries, tuples etc.

None is always treated as False.

For integers and floats: 0 returns False, anything else returns True. Even negative numbers.

### Type Casting
It's possible to specify a variable type:
- int(x)
  - Will cast the variable x to be an integer. If possible, throws a ValueError if not.
  - Floats will be rounded down.
- float(x)
  - Will cast the variable x to be a float. If possible, throws a ValueError if not.
- str(x)
  - Will cast the variable x to be a string. Should always be possible, unless the variable is unassigned.
- bool(x)
  - Will cast the variable x to be a bool. Kinda... pointless?
  - Since all types can return True or False based on their value. (Truthy)
  - (Apart from NoneType which is always False)

When casting there are things to consider. For instance when dividing integers the result could be a float.

Casting the result as an integer could have unintended consequences, like rounding.
