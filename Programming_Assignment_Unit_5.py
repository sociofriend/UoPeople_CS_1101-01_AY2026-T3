"""
Write program to display your name and perform following operations on it:
Task 1. Display n characters from left. (Accept n as input from the user)
Task 2. Count the number of vowels.
Task 3. Reverse it.
"""

# Task 1
def get_name():
    myName = input("Enter your name: ")
    for c in myName:
        # recurse if the name contains any non-alpabetic character
        if not c.isalpha():
            print("Your name should only contain letters. Please try again. ")
            return get_name()
    return myName


def get_number_of_characters(name):
    number_of_charactes_from_left = input("Please enter the number of characters you'd like to see from the left side of the string: ")
    try:
        converted_number = int(number_of_charactes_from_left)
    except ValueError:
        print("Please enter a valid integer.")
        return get_number_of_characters()

    if converted_number > len(name):
        print(f"There are only {len(name)} characters in the string.")
        return get_number_of_characters(name)
    else:
        return converted_number

def get_characters_from_left(n, name):
    if len(name) == 0 or n == 0:
        print("Number of charachters of the name and 'n' shall be greater than zero.")

    if n > len(name):
        print(f"{n} is grater than number of character of {name}")
        return get_characters_from_left(n, name)

    print(name[:n])
    return name[:n]


safe_name = get_name()
safe_number = get_number_of_characters(safe_name)
# print(safe_name, safe_number)
get_characters_from_left(safe_number, safe_name)

