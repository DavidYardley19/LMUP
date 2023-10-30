if __name__ == "__main__":

    print("Welcome to Week 6 practicals\nLists and Tuples")

    ####################################################################################################################
    # LISTS
    ####################################################################################################################

    squares = [4, 9, 16, 25]

    # Task: write for loop to go over elements and print sqrt for each
    from math import sqrt as root

    for element in squares:
        print(root(element))

    # Task: use append to add 3 square values: 49, 64, 81
    # squares.append([49,64,81])
    # This does not work since append is for singular values, will need to use extend for more:
    squares.append(49)
    squares.append(64)
    squares.append(81)

    # Task: extend to add next 3 square vals, starting at 121
    squares.extend([121, 144, 169])

    # Task: insert value 2 at the start of the list
    squares.insert(0, 2)

    # Task: remove value 49, printed after to check
    squares.remove(49)

    # Task: remove value 3, notice how error given since it wasnt in the list
    # squares.remove(3)

    # Task: Create list with [1,2,3,1,2], then remove val 2
    simpleList = [1, 2, 3, 1, 2]
    simpleList.remove(2)
    # The first instance of the argument was removed.

    # Task: pop method squares then display last element
    squares.pop()
    print(squares[-1])

    # Task: pop first value of squares list, printed after to make sure it worked.
    squares.pop(0)

    # Task: sort method w no args, alphabetically sort names given below
    names = ["Eric", "anna", "Sophie", "sam"]
    names.sort()
    print(names)
    # That is pretty much the scope of the task. Remember that capital letters come before lower case. A < Z < a < z

    # Task: improve prev task s.t it ignores case used. Hint: Use key of a lambda expression that returns each string
    # as uppercase only
    names.sort(key=lambda n: n.upper())
    print(names)
    # So lambda seems to be local to the function.

    # reverse values in squares
    squares.reverse()

    # find index the colour blue in the following list
    colours = ["red", "green", "yellow", "blue", "red"]
    print(colours.index("blue"))

    # Task: copy colours then make changes to original list
    new_colours = colours.copy()
    colours.append("black")

    # NOTE: delete can be used to pop multiple values... Think of append vs. extend

    # Task: use list comprehension to create list called cubes that contains cubed vals from 2 to 20 inclusive
    cubes = [x * x * x for x in range(2, 21)]

    # Task: Examine code below, which usernames will be placed in some_users list. What's the condition?
    all_users = ["123456789", "dave", "bob", "steve", "0"]
    some_users = [u for u in all_users if len(u) < 8]
    print(some_users)
    # Only the users which have a length of less than 8.

    ####################################################################################################################
    # TUPLES
    ####################################################################################################################

    student = ("Griffin, P.", 2, 38.2)
    # This is known as tuple packing. Can be created without brackets but I prefer them.

    # Task: Create tuple called address with house number, street, postcode
    address = (30, "My street", "AB1 1CD")

    # Note! To create a tuple with just one element, do not use myTuple = ("oneElement")
    # Instead use: myTuple = "oneElement",
    len1Tuple = (1,)
    print(type(len1Tuple))
    # But this works too, I will stick with brackets!
    # It is common to include a trailing comma even when one is not needed.

    # Task: Sequence unpack to extract vals stored in address.
    houseNumber, street, postcode = address

    # Task: print contents of address. Ensure * prefix used so elements extract before passing to function.
    # Compare this to not using * prefix

    for i in address:
        print(i, end=" ")
    print()
    # This also does the same as the below... However, I do have a space at the end of the string using the code above.
    print(*address)
    # The below outputs everything in parentheses.
    print(address)

