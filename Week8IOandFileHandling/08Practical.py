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

    print("The real power from f strings comes from format specifiers"
          "This is a small string that is included after expressions, prefixed by a : character.")

    import math
    r = 10
    print(f"A circle with radius {r} has an area of {math.pi * r * r:.2f}")
    # Here, .2f implies the decimal points

    # Task - rewrite rectangle code but include format specifier that limits displayed result to 3 dp
    print(f"The area of a rectangle with a width of {width} and a height of {height} is {width * height:.3f}")

    print("You can also use format specifiers for column width and alignment")
    name = "Dave"
    age = 22
    print(f"{name:>15} - {age:10}")
    print(f"{name:a^15} - {age:10}")
    print(f"{name:#<15} - {age:10}")

    # Task: write print statement displaying name and age w width of 20 for each, both alligned right... age to 2dp, fill with $
    print(f"{name:>20}|{age:>20}")