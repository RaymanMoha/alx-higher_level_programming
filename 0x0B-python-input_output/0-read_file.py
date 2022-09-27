<<<<<<< HEAD
#!/usr/bin/python3
"""Defines a text file reading function."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout."""
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
=======
#!/usr/bin/python3

"""Defines a text file reading function."""

def read_file(filename=""):

"""Reads a text file and prints it to stdout."""

with open(filename, "r", encoding="UTF-8") as i:

for line in i:

print( line, end=" ")
>>>>>>> e3496b6106074e1bb4333def217297a7eae7810e
