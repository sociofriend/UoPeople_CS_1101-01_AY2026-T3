#Discussion Forum Unit 4

"""
Section 6.9 of Think Python by Allen B. Downey explains that when a function is not working, there are three main possibilities to examine. These three possibilities involve preconditions, postconditions, and return values (Downey, 2015, Section 6.9, para. 1).

First, there may be something wrong with the arguments the function receives, meaning it could violate a precondition. A precondition is something that must be true before a function runs. When the function is waiting for one kind of parameters, e.g. integer, and receives something else, e.g. string, without proper error handling and the guardian approach, we say that the precondition has been violated.
For example, if a function expects a positive number but receives a negative number, the function may fail.
"""

# region Example 1 - Violation of the Precondition

# function is waiting for one argument of a numeric type
def precondition_violation_example(number):
    result = number + 100
    print("Function implementation without error handling or guardian approach:")
    print("Argument type is: ", type(number))
    print("Result is: ", result, "\n")

# function handles type errors with try-except block
def precondition_violation_example_with_error_handling(number):
    print("Function implementation with error handling:")
    try:
        result = number + 100
        print("Argument type is: ", type(number))
        print("Result is: ", result, "\n")
    except TypeError:
        print("Error: Argument must be numeric, but got", type(number), "\n")

#function checks the type of the argument, and if it is not numeric, it prints a warning message; otherwise it safely reuses precondition_violation_example function
def precondition_violation_example_with_guardian_approach(number):
    print("Function implementation with guardian approach:")
    if type(number) is not int and type(number) is not float:
        print("Error: Argument must be numeric, but got", type(number), "\n")
        return

    precondition_violation_example(number)

# # if we pass an integer or a floating number to it, it will work fine
# precondition_violation_example(10)
# precondition_violation_example(10.5)
# # but if we pass a string, it will fail
# precondition_violation_example("ten")

# # now we will do the same with the error handling and the guardian approach
# precondition_violation_example_with_error_handling("ten")
# precondition_violation_example_with_guardian_approach("ten")
# precondition_violation_example_with_guardian_approach(10)
# endregion

# region Example 2 - Violation of the Postcondition

# function is supposed to return a string
# expected: "John Doe"
def postcondition_violation_example(name, surname):
    print("Name: ", name)
    print("Surname: ", surname)
    result = name + surname
    print("Result is: ", result)

# postcondition_violation_example("John", "Doe")
# endregion
