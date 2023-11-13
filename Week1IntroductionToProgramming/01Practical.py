if __name__ == "__main__":
    # Topics
    # ● Types of Programming Languages
    # ● Using the Python Interpreter
    # ● Entering basic expressions
    # ● Understanding operators and precedence
    # ● Dealing with Errors
    # ● Key programming terminology

    # Basic Expressions:
    additionVariable = 20 + 20
    subtractionVariable = 20 - 20
    multiplicationVariable = 20 * 20
    divisionVariable = 20 / 20

    powerVariable = 20 ** 20
    floorDivisionVariable = 20 // 20
    modulusVariable = 20 % 20
    # Precedence: (),   **,     *,/,//,%,      +,-
    # BODMAS

    # Syntax error:
    # Print("Hello World!")
    # This is because print should be in lower case. Like so:
    print("Hello World!")

    # Task: input and execute the following code:
    print("the program has executed")

    # task: input the following and note the difference
    a = 12 + (5 * 2 + 3)
    b = 12 + (5 * (2 + 3))
    print(a)
    print(b)

    # Errors
    print(""
          "Syntax is most common - language syntax not been used correctly. Think of grammar.#"
          "Logical - occur during runtime, not as easy to spot"
          ""
          "A well written program should always handle errors gracefully, reporting the problem to the user."
          "")

    # Task: look into the phrases and ensure you understand each one.
    # Source code, machine code, interpreter, compiler, 2gl, 3gl, 4gl, executable, expressions, operators, operands, syntax errors, logical errors.
    print(" Source code is what has been inputted by the programmer however a computer cannot understand this just yet.")
    print(" Machine code is source code that has been compiled such that the computer can then execute the code. This is represented by 1s and 0s")

    print("An interpreter executes the code line by line. This is done whilst the program is running")
    print("A Compiler translates the etire code prior to running the program. This can cause issues if running into any errors"
          "Extra note: Compiled langs are usually faster and more efficient to execute. They give more control over hawdware aspects.")

    print("2gl, 3gl, 4gl... assembly, portable and programmer friendly, specialisation towards specific domains such as database management (respectively)")
    print("An executable contains an encoded sequence of instructions that the system can directly execute when the user clicks on the icon file"
          "They most commonly have the .exe file extension. >>> So by my understanding, all exe files should be 2GL?")

    print(" My interpretation of an expression is either a calculation/ concatenation of values - may that be int or string or bool where it typically takes 2 operands and 1 operator")
    print(" An operator may be + - != < ^ etc1")
    print(" An operand is a piece of information which will be compared or aritmetically calculated against another operand.")

    print("Syntax = program grammar issues, read a py-book, or something.")
    print("Logical = 'hidden' bugs... The code looks right but you do not get any indication that it's not the intended output.")
