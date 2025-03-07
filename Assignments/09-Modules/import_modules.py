import random   # Imports the random module
from random import randint  # From the random module imports the randint() function.


print(random.randrange(0, 30, 2))   # Will print even numbers between 0 and 30 (Because step is set to 2)
print(randint(0, 30))    # Will print all numbers between 0 and 30
