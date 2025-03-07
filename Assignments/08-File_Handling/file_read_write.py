with open("text.txt", "w") as file:
    file.write("First line\n")

with open("text.txt", "w") as file:
    file.write("Second line\n")

with open("text.txt", "r") as file:
    print(file.read())  # As the previous files were open as "w" this will print "Second line\n"

with open("text.txt", "a") as file:
    file.write("Third line\n")  # This appends the line to the end of the file

with open("text.txt", "r") as file:
    print(file.readline())  # Will only print the first line

with open("text.txt", "r") as file:
    print(file.read())  # Will print everything in the file.

file = open("text.txt", "r")
print(file.read())
file.close()

with open("text.txt", "rb") as file:
    print(file.read())  # Will print b'Second line\r\nThird line\r\n'
