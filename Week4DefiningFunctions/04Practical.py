from math import sqrt
# This will be greyed out if not used
import math

if __name__ == "__main__":
    print("Welcome to week 4 Practical\n"
          "Topics include:\n"
          "\tImport/ using functions\n"
          "\tdefining documenting functions\n"
          "\tdefault and keyword arguments\n"
          "\tArbitrary length argument lists\n"
          "\tLambda expressions\n")

    print(sqrt(4))
    print(math.pi)


    # Sometimes best to place def functions at the top? Especially with small programs where they definitely will be
    # used.
    def myfunction(name):
        # name here is a formal parameter
        print(f"Hello {name}")


    userInput = input("What is your name: ")
    myfunction(userInput)
    # userInput here is an actual parameter

    # TASK: Write some code that imports only the log2() function from the math module, then
    # call this function to calculate the log base 2 value of 1024. Print the result to the screen

    from math import log2

    print(log2(1024))


    # TASK: Input the above function definition. Once that is done make several calls to the
    # function passing different argument values for testing

    def displayTwice(msg):
        print(msg)
        print(msg)


    # You can pass pretty much anything :)

    # TASK: Re-Input the above function definition, but this time add a docstring that includes a
    # description of the function’s purpose. Once that is done enter a command such as
    # help(displayTwice) and see what it displays.

    def displayTwice(msg):
        """
        :param msg: this is the formal parameter, local only to this function. This can be any data type.
        :return: None, however there are in built print functions to assist.
        """
        print(msg)
        print(msg)


    help(displayTwice)


    # Useful when sharing code with others.

    # TASK: Input the above function definition. Once that is done make several calls to the
    # function passing different argument values and displaying the returned value.

    def findMax(a, b):
        """Finds the maximum of two values."""
        if (a > b):
            max = a
        else:
            max = b
        return max


    # This can be any data type as we can use operators such as < > != etc for string bool int char and so on.

    # TASK: Define a function that takes two numeric values, multiplies them together then returns
    # the result. If the function is called with only a single argument however, then the value should
    # be multiplied by itself. Once the function is defined, call it several times and display the
    # returned values for testing purposes.

    def multiplication(a, b=None):
        if b is not None:
            return a * b
        else:
            return a ** 2


    print(multiplication(5))


    # TASK: Enter the example function shown above, then try calling it using the keyword
    # arguments in several different orders.

    def someFunc(x, y, z):
        print("x is", x, "\ny is", y, "\nz is", z)


    someFunc(y=2, z=1, x=3)
    # order does not matter here.

    # TASK: The built-in print() function supports a keyword argument called sep. This is used
    # to decide what character to display between each of the provided positional parameters.
    # Write some code that makes several calls to the print() function while setting the sep
    # argument to values other than a space (which is the default).

    # extra note, it also supports the argument "end"... works just like console.write if you use end=""

    print("Hello", "There", sep=" ")
    print("Hello", "There", sep="1")
    # for formatting the date
    print('16', '10', '2023', sep='-')


    # Arbitrary Length Argument Lists
    # We define arbitrary length arguments by prefixing the formal parameter name with an
    # asterisk (*) character, which indicates the use of a Tuple
    def calcAve(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)


    # tuple is immutable whilst lists are mutable, think of strings where you cant change the nth index of a string
    print(calcAve(21, 2, 23, 44, 23))

    # Lambda Expressions
    # for def small simple functions
    # anonymous and can be dealt with as a value > store in variables or passed to functions as arguments.
    # Only consist of a single expression, not a block of code.

    hypot = lambda a, b: math.sqrt(a * a + b * b)
    # keyword args can also be used in the below.
    hypot(3, 4)
    # a,b are the formal parameters, which are then accessible as local variables within the expression.

    # TASK: Enter the example lambda expression shown above, then find out the data type of
    # the hypot variable using a call to the type() function. Notice the result.

    # hovering over it does the exact same thing. This may be because we used math.sqrt

    # TASK: Write a lambda expression that takes two formal parameters, hours and minutes.
    # The expression should calculate and return the total number of equivalent seconds. Assign
    # the expression to a variable called to_seconds, then call the function several times for
    # testing.

    to_seconds = lambda hours, minutes: minutes * 60 + hours * 3600
    print(to_seconds(hours=1, minutes=0))

# TASK: Improve your previous lambda expression so that if only one argument is passed
# within a call, then the number of minutes defaults to 0, as detailed below:

    to_seconds2 = lambda hours, minutes = 0: minutes * 60 + hours * 3600
    print(to_seconds2(1))
