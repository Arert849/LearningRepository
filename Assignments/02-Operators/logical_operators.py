
a, b = True, False

if a:
    print("a", a)

if a and b:
    print("a and b", a, b)  # Will not print as b is False

if a or b:
    print("a or b", a, b)   # Will print as a is true

if not a:
    print("Not a", a)    # Will not print

if b:
    print("b", b)    # Will not print

if not b:
    print("Not b", b)

if a and not b:
    print("a and not b", a, b)  # Will print as a is true and not b returns false as b is false
