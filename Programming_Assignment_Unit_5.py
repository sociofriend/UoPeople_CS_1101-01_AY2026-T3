"""
Write program to display your name and perform following operations on it:
Task 1. Display n characters from left. (Accept n as input from the user)
Task 2. Count the number of vowels.
Task 3. Reverse it.
"""

# region Task 1. Display n characters from left
def get_name():
    myName = input("Enter your name: ")
    for c in myName:
        # recurse if the name contains any non-alpabetic character
        if not c.isalpha():
            print("Your name should only contain letters. Please try again. ")
            return get_name()
    return myName

def get_number_of_characters_for(name):
    number_of_charactes_from_left = input("How many first letters to preview: ")
    try:
        converted_number = int(number_of_charactes_from_left)
    except Exception as e:
        print("Please enter a valid integer.")
        return get_number_of_characters_for(name)

    if converted_number > len(name):
        print(f"There are only {len(name)} characters in the string.")
        return get_number_of_characters_for(name)
    else:
        return converted_number

def get_characters_from_left(n, name):
    if len(name) == 0 or n == 0:
        print("Number of charachters of the name and 'n' shall be greater than zero.")

    if n > len(name):
        print(f"{n} is grater than number of character of '{name}'")
        return get_characters_from_left(n, name)

    substring = name[:n]
    print(f"First {n} character/s of '{name}' is/are: '{substring}'")
    return substring
# endregion

# region Task 2. Count the number of vowels
def is_vowel(c):
    try:
        vowels =['a', 'e', 'i', 'o', 'u']
        return c.lower() in vowels
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        return False

def count_vowels(name):
    count = 0
    for c in name:
        if is_vowel(c):
            count += 1
    print(f"There are {count} vowels in name '{name}'")
    return count
# endregion

# region Task 3. Reverse it
def reverse_name(name):
    len_name = len(name)
    if len_name == 0:
        print("Empty string.")
        return ""

    reversed_name = ""

    for i in range(len_name):
        reversed_name += name[len_name - 1 - i]
    print(f"The reversed string of '{name}' is: '{reversed_name}'")
    return reversed_name
# endregion

# region Execution
# get name
safe_name = get_name()

# get number for left side preview
print("\n")
safe_number = get_number_of_characters_for(safe_name)

# preview a given number of characters from left to right side of the string
print("\n")
get_characters_from_left(safe_number, safe_name)

# count vowels of the name
print("\n")
count_vowels(safe_name)

# revers name and print it
print("\n")
reverse_name(safe_name)
# endregion