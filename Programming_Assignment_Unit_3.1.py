"""Q1.Recursive countup function"""

# CODE
# Function recursively gets user input and checks if it is a valid integer. If not, it prompts the user to enter a valid integer.
def get_user_input():
    user_input = input("Enter a number: ")
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_user_input()

# Function gets the number and checks it to be greater than or equal to 0. If it is, it calls the countup function recursively.
def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

# Function gets the number and checks it to be less than or equal to 0. If it is, it calls the countdown function recursively.
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

# Function prompts the user to restart the program.
def restart():
    user_input = input("Do you want to restart? (y/n): ")
    if user_input == 'y':
        countup_user_unput()
    elif user_input == 'n':
        return
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        restart()
        return

# Function calls the get_user_input function and checks the result of it. If it is greater than or equal to 0, it calls the countdown function. Otherwise, it calls the countup function. After the countdown or countup recursion, it prompts the user to restart.
def countup_user_unput():
    number = get_user_input()
    if number >= 0:
        countdown(number)
    else:
        countup(number)
    restart()


# Call the countup_user_unput function to get user input, implement countup or countdown recursion, and prompt the user to restart the program.
countup_user_unput()

#OUTPUT
"""
(.venv) ➜  CS_1101-01_AY2026-T3 python Programming_Assignment_Unit_3.1.py
Enter a number: 6
6
5
4
3
2
1
Blastoff!
Do you want to restart? (y/n): y
Enter a number: 0
Blastoff!
Do you want to restart? (y/n): -n
Invalid input. Please enter 'y' or 'n'.
Do you want to restart? (y/n): y
Enter a number: -10
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
Blastoff!
Do you want to restart? (y/n): n
(.venv) ➜  CS_1101-01_AY2026-T3 
"""


# ZERO case explanation:
"""
ZERO Case Explanation

As the assignment specifies that the countup recursion should handle negative numbers, we assume that the countup function should not be called when the input is 0.

The countdown function, however, already includes 0 in its base condition (n <= 0). Therefore, for an input of 0, we have two possible approaches:
	1.	Call the countdown function, or
	2.	Handle the 0 case separately without calling any recursive function.

From a time complexity perspective, both approaches run in O(1) time for the input 0, since only a single operation (or function call) is performed.

Because there is no difference in Big-O complexity, we choose to handle 0 together with positive numbers by calling the countdown function. This keeps the logic consistent and avoids introducing unnecessary conditional branches that would make the code more complex.
"""

"""Q2.Recursive """

