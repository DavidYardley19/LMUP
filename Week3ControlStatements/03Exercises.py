if __name__ == "__main__":
    print("Welcome to the exercises")

    # ################################################################################################################
    # Anything surrounded by #'s need to be looked over!
    # ################################################################################################################

    # What is the data-type of the result when evaluating comparison (relational) expressions such as < and >?
    """
    print(1.)
    print(3.1 < 3.2)
    print("a" < "b")
    """

    # Outputs are boolean

    # For each of the following expressions write the result of their evaluation
    """
    print(2.)
    print(100 < 101)  # TRUE
    print(100 > 99)  # TRUE
    print(100 >= 100)  # TRUE
    print(100 != 100)  # FALSE
    """

    # For each of the following expressions write the result of their evaluation.
    """
    print(3.)
    print("abc" < "xyz")  # TRUE
    print("abc" < "XYZ")  # FALSE since capitals come first
    print("100" == 100)  # FALSE since they are different data types
    """

    # For each of the following expressions write the result of their evaluation.
    """
    print(4.)
    print(10 > 20 and 10 >= 10)  # FALSE since at least one of them is false, and we use an and operator
    print(10 > 30 > 20)  # FALSE since all needs to be true
    print(40 < 20 or 20 < 30)  # TRUE since at least one of them need to be right
    print(not True)  # FALSE since not flips the boolean
    """

    # What would be the output shown following the execution of the following Python statements?
    """
    print(5.)
    colours = ["Blue", "Black", "Orange"]
    print("The colour black is in the list : ", "Black" in colours)  # "black" in colours = TRUE
    print("The colour orange is in the list : ", "orange" in colours)  # FALSE
    """

    # Which of the following concepts does the Python ‘if’ statement support? Sequence, Selection or Iteration?
    # ################################################################################################################
    # SEQUENCE NEED TO LOOK INTO THIS IN MORE DEPTH
    # ################################################################################################################


    # What would be the output shown following the execution of the following Python statements?
    """
    print(6.)
    num1 = 100
    num2 = 10
    if num1 % num2 == 0:
        print("num1 is divisible by num2")
    else:
        print("num1 is not divisible by num2")  # IF was successful since the condition was true. It is divisible.
    """

    # What would be the output shown following the execution of the following Python statements?
    """
    print(7.)
    num1 = 99
    num2 = 70
    if num1 < num2:
        print("num1 is less than num2")
    elif num1 > num2:
        print("num1 is greater than num2")  # This, since the elif condition was TRUE
    else:
        print("num1 is equal to num2")
    """

    # What is the name given to the following type of Python operator shown below?
    """
    print(8.)
    x, y = 1, 2
    lowest = x if x < y else y  # NAME = TERNARY OPERATOR > only works for one or two outputs.
    print(lowest)
    """

    # And, what value would be assigned to the variable ‘lowest’ when ‘x’ was equal to 10 and ‘y’ was equal to 5?
    """
    print(9.)
    x, y = 10, 5
    lowest = x if x < y else y  # y
    print(lowest)
    """

    # Within the answer box below write a small Python program, that asks the user to enter avalue between 1 and 10.
    """
    print(10.)
    correctInput = False
    while correctInput == False:
        userInt = int(input("Please enter a value between 1-10: "))
        if 1 < userInt < 10:
            correctInput = True
            print("Thank you")
    """

    # write a program that asks the user to enter two values. Store these in variables called x and y respectively.
    """
    print(11.)
    x = int(input("Please enter your x value: "))
    y = int(input("Please enter your y value: "))
    if x > y:
        print("The value 'x' is larger than the value 'y'")
    else:
        print("The value 'y' is larger than the value 'x'")
    """

    # Examine the output by the above program. Is the displayed text entirely accurate in all cases? If not Why?
    # If both numbers are the same, then the else will be printed. This is bad.

    # asks the user to enter two values.
    # Store values in variables. output a message displaying the result of dividing the first value by the second value.
    # Include code: prevents a run-time error being reported when the user inputs a value of '0' for the second input.
    """
    print(12.)
    x = int(input("Please enter an x value: "))
    y = int(input("Please enter a y value: "))
    if y == 0:
        print("division by 0 is not possible")
    else:
        print(x / y)
    """

    # Which of the following concepts does the Python while statement support?
    # Sequence, Selection or Iteration?
    # ################################################################################################################
    # Sequence and iteration
    # ################################################################################################################

    # What would be the output shown following the execution of the following Python statements?
    """
    print(13.)
    num = 5
    while num > 0:
        print(num)
        num -= 1  # 5 4 3 2 1
    """

    # Write a small Python program that prints your name to the screen 100 times, then enter the
    # program into the answer box below. Hint: use a ‘while’ loop... This can be done with for loops
    """
    print(14.)
    for i in range(100):
        print("dav", i)
    """

    # What would be the output shown following the execution of the following Python statements?
    """
    print(15.)
    vals = ["A", "B", "C", "D"]
    for letter in vals:
        print(letter)  # A B C D >> Remember For each loops in c#
    """

    # What would be the output shown following the execution of each of the following Python statements?
    """
    print(16.)
    for num in range(5):
        print(num)  # 0 1 2 3 4
    for num in range(10, 16):
        print(num)  # 10 11 12 13 14 15
    for num in range(0, 10, -1):
        print(num)  # 10 9 8 7 6 5 4 3 2 1 >> This is wrong. Because we start with 0... if it was 10,0 it would be fine.
    for num in range(10, 0, -1):
        print(num)  # Then the above would be correct.
    """

    # Enter and execute the python code shown below, then show the exact output into the answer box.
    """
    print(17.)
    for x in range(1, 10):
        for y in range(1, x):
            print("*")  # range 1,1 then range 1,2 then range 1,3... all the way to 1,10
        print()  # So the last one would show 9 "*"s >> Wrong? It only shows 8?
        # This is because x will only go to 9... so range(1,9) will only go to 8
    """

    # What is the term used to refer to code blocks that appear inside other code blocks as in the above program?
    # ################################################################################################################
    # Statements ?
    # ################################################################################################################
