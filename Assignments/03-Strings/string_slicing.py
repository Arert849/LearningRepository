text = "Python"

print(text[0:4])    # Prints 'Pyth' index starts at 0 'P' and goes to 4 'h' (inclusive)
print(text[-3:])    # Prints 'hon' -3 index starts going backwards. Since no end is specified it goes to end of string.
print(text[::-1])   # Reverses the string.

print(text[0:-1:2])    # The last number is a step parameter, that's why -1 reverses it. ^
