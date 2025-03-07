a = 0
while a < 10:
    a += 1
    print(a)

print("Will print after 10")

a = 0
while True:
    a += 1
    print(a)
    if a == 10:
        break

a = 0
while a < 10:
    a += 1
    print(a)
    if a == 10:
        break
else:
    print("Will not print after 10 as break was called")
