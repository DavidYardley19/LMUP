if __name__ == "__main__":
    print("Welcome to Week 6 - Exercises")

    names = [1, 2, 3]
    # Would the below be a function call or a method call?
    names.reverse()
    # method call? Think in reference to OOP. You may have methods and attributes.

    # Write python statement appending 1 element to end of list using a method call - so this confirms the last question
    prices = [2.65, 7.65, 8.25, 9.56]
    prices.append(1.11)

    # write another which adds 3 elements to the list
    # We could append 3 times or just extend.
    prices.extend([2.2, 3.3, 4.4])

    # write for loop to go over each element and print to screen
    """
    for i in prices:
        print(i)
    """

    # Is a method that changes the contents of the associated value referred to as a mutator?
    # Yes

    # What would the contents of the primes list look like after executing the following
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    primes.pop()
    # it would look like the same list, but without 19 on the end.
    primes.reverse()
    # following pop, it would then reverse the order entirely.
    primes.remove(7)
    # after the prev two methods, it would remove the value 7 from the list. > may confuse me in the future with index.

    # give example of how insert method can be used to add val of 10 to start of list:
    temps = [32, 46, 95, 10, 50]
    temps.insert(0, 10)

    # use accessor method to find index of val 95 in list
    temps.index(95)

    # use another accessor method to count how many times 10 appears in the list.
    temps.count(10)

    # What is stored in samples after the following is executed:
    samples = [100.2, 100.6, 99.2, 765.2, 900.2, 400]
    samples = samples.reverse()
    print(samples)
    # it prints none. This may be because it's not a list of strings? Or perhaps it uses two different data types.
    # No there is something more than that.
    # You need to create a new list, may it be temporary. This is because it's an "in place operation".
    # Perfect to know I think.

    # use list comprehension to produce the same list as the following
    # I mean the question is wrong since it uses n and x
    """
    values = []
    for n in range(100, 200):
        values.append(x * x)
    """
    values = [x * x for x in range(100, 200)]

    # Now amend the above code, so it only uses even numbers
    values = [x * x for x in range(100, 200) if x % 2 == 0]

    # What is the data type of:
    info = ("Ken", "bae-192", 62)
    # tuple

    # Are they mutable, no

    # Make a tuple with 1 element
    mySingleTuple = (1,)

    # unpack the following tuple into 3 vars called x y z
    coord = (100, 200, 150)
    x, y, z = coord

    # use indexing to access second element of tuple and store in var called height
    height = coord[1]

    # for loop to print each val in tuple
    for i in coord:
        print(i)

    # What prefix can be used to unpack a tuple prior to a function call
    # *

    # heterogeneous used to describe type of stored values. What does this mean.
    # This is the ability to store elements of different data types

    # What sister phrase is used to refer to the type of values stored in a list.
    # homogeneous
