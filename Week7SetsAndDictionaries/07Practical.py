if __name__ == "__main__":

    print(" Welcome to wk7 sets and dictionaries: practical work")

    # intro to sets
    # comprehensions
    # mutable and immutable sets
    # operators and methods
    # intro to dictionaries
    # create and working with dictionaries

    ####################################################################################################################
    # Intro to sets
    ####################################################################################################################

    print(" A set is like list and tuple, however elements are not ordered and no duplicates are allowed.")
    print(" A set cannot contain immutable values such as lists however it is mutable itself.")
    print(" Not ordered, so no indexing slicing or any method in relation to element positions")

    vowels = {"a", "e", "i", "o", "u"}
    print(type(vowels))

    for i in range(3):
        print(vowels)
    # the set is unordered so any variance can be printed.
    # however it will remain the same order until the program is run again.

    print("set constructor = similar to functions but for initialising object based on named type")
    names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry", "David", "Dav", "Dave"])
    print(names)
    # names = set("John", "Eric", "Terry", "Michael", "Graham", "Terry")
    # print(names)
    print(" However, you must note that only a since parameter can be passed into set() > "
          " so this is convenient if the values already exist in some other iterable value like list and tuple")

    print(" An empty set must be created using set() constructor rather than empty braces >"
          " Since the latter creates a dictionary (more on this later).")

    ####################################################################################################################
    # Set Comprehensions
    ####################################################################################################################

    print(" Set comprehension works the same as list comprehension however {} is used instead of []")

    # What is cool here is that you can run a loop through a phrase to see how many letters appear in the
    # phrase at least once. This is due to the sets property which states that elements cannot be repeated.
    sentence = "this is a sentence containing some letters"
    unique_letters = {x for x in sentence}
    print(unique_letters)
    # This includes the space however which is not a letter.
    # Later we can use a set operation to remove the " " however for now we can specify within the set comprehension.
    unique_letters = {x for x in sentence if x != " "}

    ####################################################################################################################
    # Set Operations
    ####################################################################################################################

    print(" most common operation on a set is membership testing: use in or not in")
    name = input("Enter your name: ")
    if name in names:
        print("You are listed in the set of known names")
    # Elements are still case-sensitive here. > may be worth using name.capitalize or something similar.

    # Task: rewrite prev code, so it checks that the input name is NOT within the set of known names
    if name not in names:
        print(" That name does not come up in the set of known names")

    print(" Since sets are mutable, both accessor and mutator type operations exist. >"
          "it is also possible to perform special comparison type operations such as:"
          " | >>> union"
          " & >>> intersection"
          " - >>> difference"
          " ^ symmetric difference (which is just the union - intersection)")
    print("You can also call these special operations by methods() with respective names")

    all_staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}

    # Add 2 members
    all_staff |= {"a", "b"}
    print(all_staff)

    # Create a new set s.t. it doesn't contain any directors
    non_directors = all_staff - directors
    print(non_directors)

    # Task: create two initial sets staff and directors. Perform 4 math set operatins
    # but use the equivalent method calls to achieve the same results.
    """
    all_staff.union({"a", "b"})
    ...
    all_staff.intersection()
    all_staff.difference()
    all_staff.symmetric_difference()
    """
