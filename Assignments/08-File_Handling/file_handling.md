### File Handling
The with statement can be used for files to avoid having to manually close them.

    with open(file, mode) as f:
        """ do something """
    
    # File automatically closes after the with statement

The open(file, mode) method has several modes:
- **"r"** = read
  - Opens a file for reading, if the file doesn't exist raises a FileNotFound error.
- **"w"** = write
  - Opens a file for writing, creates the file if it doesn't exist.
- **"a"** = append
  - Opens a file for appending, creates the file if it doesn't exist.
- **"x"** = create
  - Creates the file, if the file already exists it raises a FileExists error.

It can be specified in what way the file should be handled:
- **"t"** = text
  - e.g. **"rt"** reads the file in text mode. (Default)
- **"b"** = binary
  - e.g. **"rb"** reads the file in binary mode.

Important to note, write mode writes the entire file.
If a text file has several lines: 

    with open(file, "w") as f:
        f.write("Everything is gone!")

Turns the file into a single line "Everything is gone!"

To modify specific lines in the file it is necessary to read it first and iterate over the read lines.

    with open(file, "r") as f:
        lines = f.readlines()    # Returns a list of the lines

    with open(file, "w") as f:
        for line in lines:
            if line == "banana\n":
                f.write("kiwi\n")
            else:
                f.write(line)

Will first read the file, then iterate over the lines, and finally if the line is "banana\n" replace it with "kiwi\n".

readlines() finds the lines according to the line separator character.
The write() method automatically converts to the operating system's default line separator.

I will go over copying, moving, directory creation, metadata, permissions, and archiving in later steps.