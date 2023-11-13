if __name__ == "__main__":

    print(" Welcome to wk8 practical"
          " Today: IO, string format, file handle, read write files, random file access")

    # FORMATTING WITH F STRINGS

    print("Most recent approach to formatting is called 'Formatted string literals'... AKA f strings."
          "Check the below out")
    name = "David"
    print(f"Hello {name}")

    # Task: Write code that uses f string to calc then displ a message stating:
    # "The area of a rectangle with a width of 104.32 and a height of 15.654 is ..." with correct ans
    width = 104.32
    height = 15.654
    print(f"The area of a rectangle with a width of {width} and a height of {height} is {width * height}")

    # FORMAT SPECIFIERS

