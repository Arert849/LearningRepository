### Variables & Data Types
Python data types:
- **Integers ('int')** → Whole numbers; positive and negative.
- **Floats ('float')** → Decimal numbers; positive and negative. Python floats have built in double precision.
- **Strings ('str')** → Text, python supports both single and double quotes.
- **Booleans ('bool')** → True, False.
- **None ('NoneType')** → Absence of value. Not to be confused with undefined variables.

Python variables are assigned dynamically:

x = 10 # No need to declare type ie: x = int(10)

Other variables can also, in circumstances, be treated as bool.

For instance empty strings return False in an if statement. Non-empty return True

None is always treated as False.

Same for empty and non-empty lists, dictionaries, tuples etc.

For integers and floats: 0 returns False, anything else returns True. Even negative numbers.
