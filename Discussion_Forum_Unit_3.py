"""
Discussion Forum Unit 3
Difference between Chained and Nested Conditionals

When alternative cases must be evaluated, we use alternative execution if there are only two possible outcomes (Downey, 2015, p. 41, Section 5.5, para. 1). However, when more than two possibilities exist, we use chained execution (Downey, 2015, p. 41, Section 5.6, para. 1).

A chained conditional is defined as “a conditional statement with a series of alternative branches” (Downey, 2015, Glossary, p. 47, para. 1). When we need to evaluate more than two cases, we use elif (short for “else if”). Although multiple elif clauses may be included, only one branch will execute (Downey, 2015, p. 42, Section 5.6, para. 2). The conditions are evaluated sequentially, and even if more than one condition is true, only the first true branch executes; after that, the statement terminates (Downey, 2015, p. 42, para. 4).

In contrast, nested conditionals contain sub-cases within other conditional branches. These inner branches may include simple statements, such as a print function call, or they may contain additional if statements. Although the Python language requires proper indentation with compile-time checks, to clarify the structure, deeply nested conditionals can reduce readability and make code more difficult to follow, especially when there are multiple levels of depth (Downey, 2015, p. 42, Section 5.7, para. 4).
"""

# Lists of numbers
numbers_1_to_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_11_to_20 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Total list of numbers
numbers_1_to_20 = numbers_1_to_10 + numbers_11_to_20

# Prompt for user input
prompt = "Please, kindly enter a number between 1 and 20:\n"

# function to convert user input into int. returns none incase of failure
def convert_to_int(user_input) -> int | None:
    """Attempts to convert input to integer, returns None if invalid."""
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

# function to search the number in the list with nested conditional statements
def search_func_with_nested_conditional(number):
    """A nested conditional that categorizes a number."""
    if number in numbers_1_to_20:
        if number in numbers_1_to_10:
            if number % 2 == 0:
                print(f"{number} is even in 1-10")
            elif number % 3 == 0:
                print(f"{number} is a multiple of 3 in 1-10")
            else:
                print(f"{number} is odd in 1-10")
        else:
            if 16 <= number <= 18:
                print(f"{number} is between 16 and 18 in 11-20")
            elif number % 5 == 0:
                print(f"{number} divisible by 5 in 11-20")
            else:
                print(f"{number} not divisible by 5 in 11-20")
    else:
        print(f"{number} is not in the list")

# function to search the number in the list with chained conditional statements
def search_func_with_chained_conditional(number):
    """A chained conditional that categorizes a number."""

    if number not in numbers_1_to_20:
        print(f"{number} is not in the list")

    elif number in numbers_1_to_10 and number % 2 == 0:
        print(f"{number} is even in 1-10")

    elif number in numbers_1_to_10 and number % 3 == 0:
        print(f"{number} is a multiple of 3 in 1-10")

    elif number in numbers_1_to_10:
        print(f"{number} is odd in 1-10")

    elif 16 <= number <= 18:
        print(f"{number} is between 16 and 18 in 11-20")

    elif number in numbers_11_to_20 and number % 5 == 0:
        print(f"{number} divisible by 5 in 11-20")

    elif number in numbers_11_to_20:
        print(f"{number} not divisible by 5 in 11-20")

# -------------------------------
# Execution
# -------------------------------

# get user input
user_input = input(prompt)

# try to convert into an integer
valid_number = convert_to_int(user_input)

# if there is a validly converted integer, call search function and pass valid_number as an argument
if valid_number is not None:
    print(f"Result with nested conditional:")
    search_func_with_nested_conditional(valid_number)

    print(f"Result with chained conditional:")
    search_func_with_chained_conditional(valid_number)


"""
Summary

Chained and nested conditionals are both used to control how a program makes decisions, but they are structured differently.  The code examples show that both methods can produce the same result. However, chained conditionals are usually easier to read and maintain because they use less indentation and keep all decision branches at the same level.
"""


# -------------------------------
# References
# -------------------------------
# Downey, A. (2015). Think Python: How to think like a computer scientist. pp. 29-47