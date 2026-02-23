"""Q2.Create error handling tutorial for junior developers"""

# Create a Python program that prompts the user to enter two numbers.

def divide_error_handling():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        #Implement a division operation on the entered numbers.
        #In case num2 is zero, ZeroDevision runtime error should be raised.
        print("\nDivide function called with ZeroDivisionError handled")
        try:
            result = num1 / num2
            print(result)
        except ZeroDivisionError:
            print("Cannot divide by zero.")

def divide_throws():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        #Implement a division operation on the entered numbers.
        #In case num2 is zero, ZeroDevision runtime error should be raised.
        print("\nDivide_throws function called with error handling")

        return num1 / num2


# calling the functions
divide_error_handling()
divide_throws()


"""
Error handling is an essential concept in Python programming, particularly when dealing with runtime errors. According to Downey (2015), “Once your program is syntactically correct, Python can read it and at least start running it. What could possibly go wrong?” (p. 195, Appendix A.2, para. 1). This highlights that even when code is written correctly from a syntax perspective, errors may still occur during execution.  

In the divide_throws() function, when the second number entered by the user is zero, Python raises ZeroDivisionError. As Downey (2015) explains, “If something goes wrong during runtime, Python prints a message that includes the name of the exception, the line of the program where the problem occurred, and a traceback” (p. 196, Appendix A.2.3, para. 1). This traceback helps us identify exactly where the error occurred in the code. However, if the exception is not handled, the program will terminate abruptly.  To prevent this, the divide_error_handling() function places the division operation inside a try block. If a ZeroDivisionError occurs, it is caught in the corresponding except block, and the program prints a clear and user-friendly message. This approach aligns with the purpose of debugging and controlled error management.
 
 Downey (2015) notes that understanding runtime behavior is critical because errors may not stop the program from starting, but they can interrupt execution unexpectedly (Appendix A.2, p. 195). By handling the exception properly, the program continues running instead of crashing.  If division by zero is not handled, the potential impact includes sudden termination of the program, loss of user data, poor user experience, and unstable software behavior. For junior developers, this example demonstrates why exception handling is not optional but a necessary part of writing reliable and maintainable programs.
"""

