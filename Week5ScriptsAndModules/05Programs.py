if __name__ == "__main__":
    print("Welcome to the Programs for week 5")

# Note: Most of these programs process command-line arguments. In every case your program
# should not crash if no arguments are provided. In most cases it should just exit with some
# suitable error message.

########################################################################################################################
# PROGRAM 1
# Using command-line arguments involves the sys module. Review the docs for this module and using the information in
# there write a short program that when run from the command-line reports what operating system platform is being used.
########################################################################################################################
'''
    import sys
    print(sys.getwindowsversion()[2])
'''
########################################################################################################################
# PROGRAM 2
# Write a program that, when run from the command line, reports how many arguments were provided.
# (Remember that the program name itself is not an argument).
########################################################################################################################
'''
    import sys
    print("The number of arguments provided: ", len(sys.argv[1:]))
'''
########################################################################################################################
# PROGRAM 3
# Write a program that takes a bunch of command-line arguments, and then prints out the shortest.
# If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them
########################################################################################################################
'''

'''
import sys
argumentList = sys.argv
print(argumentList)
sortedList = argumentList.sort(key=len)
print(sortedList)


########################################################################################################################
# PROGRAM 4
# Write a program that takes a URL as a command-line argument and reports whether there is a working website
# at that address. Hint: You need to get the HTTP response code. Another Hint: StackOverflow is your friend
########################################################################################################################


########################################################################################################################
# PROGRAM 5
# Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed
# the maximum, minimum, and mean. Create a version of that program that takes the values from the command-line instead.
# Be sure to handle the case where no arguments are provided!
########################################################################################################################


########################################################################################################################
# PROGRAM 6
# Write a program that takes the name of a file as a command-line argument, and creates a backup copy of that file.
# The backup should contain an exact copy of the contents of the original and should, obviously, have a different name.
# Hint: By now, you should be getting the idea that there is a built-in way to do the heavy lifting here!
# Take a look at the "Brief Tour of the Standard Library" in the docs.
########################################################################################################################
