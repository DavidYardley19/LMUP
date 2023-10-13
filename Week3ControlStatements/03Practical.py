if __name__ == "__main__":
    print("NOTE: To Comment Selected Code, Use CTRL + / ... Works for un-commenting code.")
    print("CTRL ALT L >>> Reformat code\n")

    # Topics covered:
    # ● Boolean Expressions
    # ● Decision-making using ‘if’
    # ● Membership testing
    # ● Logical operators
    # ● Ternary operators
    # ● Iteration using ‘while’ and ‘for’
    # ● Breaking and continuing loops

    # Bool expressions
    #
    # print(10<3) #false
    # print(3<=3) #true
    # print(10>3) #true
    # print(3>=3) #true
    # print(3==3) #true >> Need to be two equal signs for boolean algebra
    # print(10!=3) #true >> This means not equal

    # Task: Define var "age", compare against 18, 21 and 31
    #
    # age = int(input("Please enter your age: "))
    # if age >= 18:
    #     if age >= 21:
    #         if age >= 31:
    #             print("You're older than 30")
    #         else:
    #             print("You're older than 20")
    #     else:
    #         print("You're older than 17")
    # else:
    #     print("You're younger than 18")

    # Task: Input the following code and note the results
    #
    # print("a" < "b")
    # print("b" < "a")
    # print("John" < "Terry")
    # # Okay, is it case-sensitive?
    # print("John" < "john")
    # print("john" < "John")
    # # Answer = yes. Capitals come first.

    # Also possible with lists
    #
    # print([1, 2, 3] < [1, 2, 3])
    # # false
    # print([1, 2, 3] < [1, 2, 2])
    # # true
    # print([1, 2, 3] < [0, 4, 4])
    # # false. Any value in the list can influence this. All need to be true within the boolean expression.

    # Considering Compatability... Think of char > int > long / float etc.
    #
    # print(5 < 10.2)
    # # print(5 < "Monty") ## This will not work
    # print(5 < "5") ##same thing as above
    ## You cant seem to declare characters in py? ... even if you did myChar = "a"... It's stored as a string.
    # There are no built-in functions for it. Mi-No-Like.
    ## The == Sign is a little more forgiving.. 5 == "5" will output false.

    # Logical Operations within expressions
    #
    # In precedences order. But brackets make sure no logical errors are made.
    # NOT > return true if operands evaluate to false, and vice versa.
    # AND > return true if both operands are true
    # OR > return true if at least one operand is true
    # Did this in further depth in my maths degree...   :/

    # Task: try inputting the following code.
    #
    # age = 30
    # print(age >= 18 and age <= 65)
    # # True. since 30 is older than or equal to 18, and younger than or equal to 65
    # print(age < 18 or age > 65)
    # # False. since 30 is neither younger than 18, nor older than 65
    # print(not age > 18)
    # # False. This is because yes age is older than 18... But then the boolean is flipped with not.
    # print((age >= 18 and age <= 65) and (not age == 30))
    # # False. First brackets: True, Second brackets: False... AND operator between a true and a false produces a false.

    # The operations can be chained. Works the same as the AND operator.
    #
    # Instead of writing: 100 < weight and weight < 200
    # Use 100 < weight < 200

    # Membership Testing
    #
    # # checks if an element appears within a compound type such as strings and lists.
    # # This uses the keywords in and not in.
    # letters = ["a", "b", "c", "d"]
    # print("a" in letters)
    # # Outputs true since a is indeed in letters
    # print("e" not in letters)
    # # Outputs true since e is indeed not in letters
    # # NOTE: Since python is a dynamically typed language,
    # # variables may work in some places but if they are changed to another type, this may cause issues.
    # # Good practice may be to set variables in upper case to give an indication that these are constants.
    # # E.g. PI = 3.14159265, GRAVITY = 9.80665

    # if statement
    #
    # Task: Check if age is between 18-30, output nice message
    # age = int(input("Please give your age: "))
    # if 18 < age < 30:
    #     print("You are still young!")

    # else statement
    #
    # Optional clause should the if statement be false.
    # elif allows you to chain if statements.

    # Non-Boolean conditions
    # #
    # total = 0
    # if total:
    #     print("Total is non-zero")
    # else:
    #     print("Total is 0")
    # print(total * 1)
    # # using integers for conditions, if it is 0, then it results in false. This is new to me.
    # # But then I have issues when I set total equal to None. I get it, but still iffy'.
    # # Works for lists and strings... if it is empty then this is equal to false.
    # name = ""
    # print(len(name))
    # if name:
    #     print("Your name is", name)
    # else:
    #     print("A name was not provided")
    # # future issues: If the name was equal to a bunch of spaces then it's still not a valid name. Need to look out!
    # # So maybe this is based on the length of the string or lists? How many elements are there, is there more than 0?
    # # It would feel a lot clearer to others reading the code in the future by specifying the condition.

    # Task: literally what I mentioned in the last comment, write the same code but with expressions.
    # #
    # name = "David"
    # if len(name) > 0:
    #     print(f"Your name is {name}")
    # else:
    #     print("A name was not provided.")

    # # Ternary operator. if statement written on a single line. Returns one or two possible values.
    # # First returns true, second returns false.
    # a = 10
    # b = 20
    # bigger = a if a > b else b
    # # This is used instead of:
    # if a > b:
    #     bigger = a
    # else:
    #     bigger = b
    # # Must always use an else statement... I wonder if you can use elif? No. You just learnt that David.

    # Task: rewrite the following code:
    # age = 17
    # if age >= 18:
    #     print("you are an adult")
    # else:
    #     print("you are not an adult, yet!")
    # #
    # print("You are an adult" if age >= 18 else "You are not an adult yet!")

    # While and For loops
    #
    # While works while condition is true
    # For iterates over a sequence of values... Remember for each when working in c#
    for n in [2, 4, 6, 8, 10]:
        print(f"{n} multiplied by {n} equals", n * n)

    # Task: for loop that iterates for list of 4 names, printing each to the screen
    names = ["Adam", "Bob", "Charlie", "David"]
    for i in names:
        print(i, end=" ")

    # Range() function. Allows a range of values to be specified. Generates arithmetic progression between 2 boundaries.
    # Range also includes an optional step value. This is automatically 1 unless changed. Below I have set it to -1.
    for n in range(10, 5, -2):
        print(n)
    # Task using range
    for i in range(2, 11, 2):
        print(f"{i} to the power of {i} =", i ** i)

    # Using break > causes a loop to terminate immediately
    value = int(input("Please enter a number: "))
    for n in range(2, value // 2):
        if value % n == 0:
            print(f"{value} is not a prime number")
            break
    else:
        print(f"{value} is a prime number")
        # The else runs if the loop terminates normally, not from the break. Break would jump to after the else.

    # Using continue. It will skip to the next step/ iteration in the loop
    grades = [20, 50, 43, 33, 90, 15]
    pass_mark = 40
    passes = 0
    total = 0
    for grade in grades:
        if grade < pass_mark:
            continue
    passes += 1
    total += grade
    print("average pass mark was", total / passes)

    # Task: input code containing a for loop which iterates over a list of numbers. Printing running total at each step.
    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    total = 0
    for i in numbers:
        total += i
        if i > 100:
            break
        else:
            print(total)

    # Amended the above code so any value over 100 breaks immediately

    # TASK: Amend your previous solution once again, so that the message “all numbers
    # processed” is printed when the loop completes, but only if all values were less or equal to
    # 100 (i.e. the loop did not break early)

    # easiest method may be the following, although there may be a better method in relation to the python syntax.
    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    total = 0
    for i in numbers:
        total += i
        if i > 100:
            break
        else:
            print(total)
    if total == sum(numbers):
        print("All numbers processed")
    else:
        print("Not all numbers were processed")

    # There is probably a much better way to write this.


