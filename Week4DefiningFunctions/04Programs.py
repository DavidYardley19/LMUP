if __name__ == "__main__":
    print("Welcome to week 4 programs")

    # Question 1.
    # Functions are often used to validate input. Write a function that accepts a single
    # integer as a parameter and returns True if the integer is in the range 0 to 100
    # (inclusive), or False otherwise. Write a short program to test the function.
    """
    def checkInt(integer):
        if 0 <= integer <= 100:
            return True
        else:
            return False


    print(checkInt(int(input("Please enter an integer: "))))
    """

    # Question 2.
    # Write a function that has a single string as its parameter, and returns the number of
    # uppercase letters, and the number of lowercase letters in the string. Test the
    # function with a short program.
    """
    def checkUpperAndLowerCase(userString):
        # adds 1 for each character if chars.isupper = true
        upperChars = sum(1 for chars in userString if chars.isupper())
        lowerChars = len(userString) - upperChars
        print(f"There are {upperChars} upper characters in that string")
        print(f"There are {lowerChars} lower characters in that string")

    checkUpperAndLowerCase(input("Please enter a string containing upper and lower characters: "))
    """

    # Question 3.
    # Modify your "greetings" program so that the first letter of the name entered is
    # always in uppercase with the rest in lowercase. This should happen even if the user
    # entered their name differently. So if the user entered arthur, ARTHUR, or even
    # arTHur the name should be displayed as Arthur.
    """
    def formatString(userInput):
        print(f"Well greetings, {str.capitalize(str.lower(userInput))}")

    formatString(input("Please enter your name: "))
    """

    # Question 4.
    #  When processing data it is often useful to remove the last character from some
    # input (it is often a newline). Write and test a function that takes a string parameter
    # and returns it with the last character removed. (If the string contains one or fewer
    # characters, return it unchanged.)
    """
    def changeString(userString):
        if len(userString) <= 1:
            return userString
        else:
            return userString[:-1]

    print(changeString(input("Enter a string: ")))
    """

    # Question 5.
    # Write and test a function that converts a temperature measured in degrees
    # centigrade into the equivalent in fahrenheit, and another that does the reverse
    # conversion. Test both functions. (Google will find you the formulae).
    """
    def cToF(cTemp):
        return (cTemp * 9 / 5) + 32

    def fToC(fTemp):
        return (fTemp - 32) * 5 / 9

    print(cToF(float(input("Please enter temp in C: "))))
    print(fToC(float(input("Please enter temp in F: "))))
    """

    # Question 6.
    # Write a program that takes a centigrade temperature and displays the equivalent in
    # fahrenheit. The input should be a number followed by a letter C. The output should
    # be in the same format.
    """
    def cToF(cTemp):
        return (cTemp * 9 / 5) + 32

    cUserInput = input("Please enter the temp in C: format nC where n = a float >> ")
    ftemp = cToF(int(cUserInput[:-1]))
    print(f"That value in f is {ftemp}f")
    """

    # Question 7.
    # Write a program that reads 6 temperatures (in the same format as before), and
    # displays the maximum, minimum, and mean of the values.
    # Hint: You should know there are built-in functions for max and min. If you hunt, you
    # might also find one for the mean.

