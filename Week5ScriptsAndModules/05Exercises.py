if __name__ == "__main__":
    print("Welcome to week 5 exercises.")

    # Topics covered:
    # ● Writing code in files
    # ● Executing program files
    # ● Accessing command line arguments
    # ● Writing and importing modules
    # ● The modules search path

########################################################################################################################
# EXECUTING A SCRIPT
########################################################################################################################

# large programs stored in one or more text files, then can be executed later... often called SCRIPTS
# Plain text files that end in .py
# With REPL, outputs are provided immediately, this is not always the case with scripts.
# An explicit function must be called like print to produce an output.
# We can also define functions and classes within our files, which can be reused on more programs.

# To execute a script, use "python programName.py" >> make sure you are in the current directory for this to work.

# TASK 1: use an editor to enter python code then save it to a file called first_prog.py... execute from the cmd line.
# I used git bash for this. Worked fine after I changed directory.

# TASK 2: edit the text file with some comments. >> still works just fine.

# TASK 3: find out if a value is divisible by 10, write in if statement already there.
# I was worried if 0 was going to be an issue, but since the definition is that it must have a remainder of 0, it's fine

########################################################################################################################
# COMMAND LINE ARGUMENTS
########################################################################################################################

# Cmd line arguments. Can pass through arguments to be used as parameters in the code (?)... yes.
# This will be stored as a list of strings, only strings!
# Arguments passed must be seperated by spaces, not commas
# In the code we must use the module "sys" via import method. sys.argv takes the arguments provided from the cmd line.

# TASK 4: Import the following into a txt editor and run. I will also be adding comments.
'''
import sys
count = len(sys.argv)
total = 0
while count > 1:
    count -= 1
    total += float(sys.argv[count])
print("Total is", total)
'''

# TASK 5: add code that also calculates and prints the average, note what happens if no args are passed.
# Works just fine after cutting off the first part of the list. Since the name was used at index 0
# Entering nothing does not work out too well since nothing can be divided by 0

# TASK 6: check if no args are passed, print "no args were given". And add comments.

# The below was placed into the txt file, don't worry.
# I noticed there would still be an issue if all arguments provided were 0
'''
import sys

count = len(sys.argv)
# Notice that sys.argv was used on its own, there was no need to include a () after it.
# Perhaps this is because sys.argv is an attribute rather than a method.
total = 0

# Loops through the list provided, once the last is added, count = 0
while count > 1:
    count -= 1
    total += float(sys.argv[count])
print("Total is", total)
if total != 0:
    print("The average is", (total / len(sys.argv[1:])))
else:
    print("No args were given")
'''
# So perhaps working with just total is not ideal. Perhaps I need to evaluate if the length of the arguments list is 1
# i.e. just the name provided. The 0 index.
'''
import sys

count = len(sys.argv)
# Notice that sys.argv was used on its own, there was no need to include a () after it.
# Perhaps this is because sys.argv is an attribute rather than a method.
total = 0

# Loops through the list provided, once the last is added, count = 0
while count > 1:
    count -= 1
    total += float(sys.argv[count])
print("Total is", total)
if len(sys.argv) != 1:
    print("The average is", (total / len(sys.argv[1:])))
else:
    print("No args were given")
'''
# This is much better

########################################################################################################################
# WRITING MODULES
########################################################################################################################

# Not just scripts, but we can also import programs.
# Any .py file containing definitions and statements is called a module. Such as math, or sys.
# A collection of modules is called a library.
# When importing modules, the .py is omitted at the end.

# TASK 7: use editor to input python prog provided, store as my_utils.py
# worked just fine. Only the welcome message showed.

# TASK 8: create another prog called utils_test.py... import my_utils then call average function
# import my_utils ... no .py is required.
# QUESTION: would this only work if they are in the same directory? What if it is a subdirectory, or the parent dir?

'''
import my_utils
listOfValues = list(input("Please enter a list of numbers, seperated by spaces"))
print("Average is", my_utils.average(float(listOfValues)))
'''
# Since the list is a string at the moment, I am unable to convert it into a float
testVariable = "10.1"
testConvertStrToFloat = float(testVariable)
# This works just fine. So I can change each element type individually, but not the list type.
# What if I did a for loop to sift through the list, changing each element - since the list is mutable.
'''
listOfStrings = ["1.1", "2.2", "3.3"]
for i in range(len(listOfStrings)):
    listOfStrings[i] = float(listOfStrings[i])
print(listOfStrings)
'''
# This works out just fine. But doesn't seem to work in the text file?
listOfStrings = ["1.1", "2.2", "3.3"]
test = list(map(float, listOfStrings))
print(test)
print(sum(test))
# Why doesn't it work in the text file!
# Check what the output is after I made a list?
''' 
# Current
import my_utils
listOfValues_string = list(input("Please enter a list of numbers, seperated by spaces: "))
listOfValues_float = list(map(float, listOfValues_string))
print("Average is", my_utils.average(float(listOfValues_float)))
'''
# The reason this didn't work was because I didn't specify what it was split by
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
# So try: take the input, then assign it to a list var using split
'''
import my_utils
numbers_provided = input("Please enter a list of numbers, seperated by spaces: ")
listOfValues_string = numbers_provided.split(" ")
listOfValues_float = list(map(float, listOfValues_string))
print("Average is", my_utils.average(float(listOfValues_float)))
'''
# Bruh, just use sys.args. You just learnt this.
# worked in the end with:
'''
import my_utils
import sys
listOfValues_float = list(map(float, sys.argv[1:]))
print("Average is", my_utils.average((listOfValues_float)))
'''

