# I will be setting these out as multiple choice questions, so it's easier to code.

if __name__ == "__main__":

    print("Good day. Welcome to the exercises for the first week!\n"
          "This will be set out as a multiple choice quiz :)\n"
          "You will only need to output a single letter between A-D per question.\n")

    print("Question 1\n"
          "What is the name of the programming language that we will be using on this module?\n"
          "A. Pascal\n"
          "B. PHP\n"
          "C. Perl\n"
          "D. Python\n")
    answer = input("Enter your answer: ")
    if answer.capitalize() == "D":
        print("YES!")
    else:
        print("No!")




