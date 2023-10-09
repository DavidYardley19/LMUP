if __name__ == "__main__":
    print("Welcome to week 3 programs!")

    # Modify your greeting program so that if the user does not enter a name (i.e. they just press enter),
    # the program responds "Hello, Stranger!". Otherwise, it should print a greeting with their name as before
    """
    print("Program 1")
    name = input("What is your name? ")
    if name == "":
        print("Hello, Stranger!")
    else:
        print(f"Well hey {name}")
    """

    # Write a program that simulates the way in which a user might choose a password.
    # The program should prompt for a new password, and then prompt again. If the two
    # passwords entered are the same the program should say "Password Set" or
    # similar, otherwise it should report an error.
    """
    print("Program 2")
    password_1 = input("Please enter a password: ")
    password_2 = input("Please repeat that password: ")
    if password_2 != password_1:
        print("They are not the same")
    else:
        print("Password Set")
    """

    # Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long
    """
    print("Program 3")
    password_1 = input("Please enter a password between 8-12 characters: ")
    password_2 = input("Please repeat that password: ")
    if password_2 != password_1:
        print("They are not the same")
    else:
        if 8 < len(password_1) < 12:
            print("Password Set")
        else:
            print("The password is not between 8-12 characters.")
    """

    # Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus:
    # BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    # SELF NOTE: I believe this may have something to do with contains? ...
    # Or check that the string is in the list... This gives a boolean
    """
    print("Program 4")
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    is_bad_password = False
    password_1 = input("Please enter a password between 8-12 characters: ")
    password_2 = input("Please repeat that password: ")
    if password_2 != password_1:
        print("They are not the same")
    else:
        if 8 < len(password_1) < 12:
            for bad_password in BAD_PASSWORDS:
                if bad_password in password_1:
                    is_bad_password = True
            if is_bad_password:
                print("That is a bad password")
            else:
                print("Password Set")
        else:
            print("The password is not between 8-12 characters.")
    """

    # Modify your program a final time so that it executes until the user successfully chooses a password.
    # That is, if the password chosen fails any of the checks,
    # the program should return to asking for the password the first time.
    """
    print("Program 5")
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    is_bad_password = False
    password_successful = False
    while not password_successful:
        password_1 = input("Please enter a password between 8-12 characters: ")
        password_2 = input("Please repeat that password: ")
        if password_2 != password_1:
            print("They are not the same")
        else:
            if 8 < len(password_1) < 12:
                for bad_password in BAD_PASSWORDS:
                    if bad_password in password_1:
                        is_bad_password = True
                if is_bad_password:
                    print("That is a bad password")
                else:
                    print("Password Set")
                    password_successful = True
            else:
                print("The password is not between 8-12 characters.")
    """

    # Write a program that displays the "Seven Times Table".
    # That is, the result of multiplying 7 by every number from 0 to 12 inclusive. The output might start:
    """
    print("Program 6")
    for i in range(0, 13):
        print(f"{i} * 7 = {i * 7}")
    """

    # Modify your "Times Table" program so that the user enters the number of the table they require.
    # This number should be between 0 and 12 inclusive.
    """
    print("Program 7")
    multiplier = int(input("Between 0-12. Enter what you would like to multiply 7 by: "))
    if 0 <= multiplier <= 12:
        print(7*multiplier)
    else:
        print("That is outside of the range specified")
    """

    # Modify the "Times Table" again so that the user still enters the number of the table,
    # but if this number is negative the table is printed backwards. So entering "-7"
    # would produce the Seven Times Table starting at "12 times" down to "0 times".
    """
    print("Program 8")
    multiplier = int(input("Between 0-12. Enter what you would like to multiply 7 by: "))
    if 0 <= multiplier <= 12:
        print(7*multiplier)
    elif -12 <= multiplier <= -1:
        for i in range(-12, 1):
            print(f"{i} * 7 = {i * 7}")
    else:
        print("That is outside of the range specified")
    """

