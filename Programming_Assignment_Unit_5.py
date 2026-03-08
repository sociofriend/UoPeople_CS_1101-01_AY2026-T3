"""
Write program to display your name and perform following operations on it:
Task 1. Display n characters from left. (Accept n as input from the user)
Task 2. Count the number of vowels.
Task 3. Reverse it.
"""

# region Task 1. Display n characters from left

# Function uses a for loop to iterate through the characters of the name input, and if any non-alphabetical input is detected, it recurses to get a valid name. When a valid name is received, and the for loop ends, the name is returned.
def get_name():
    my_name = input("Enter your name: ")
    for c in my_name:
        # recurse if the name contains any non-alpabetic character
        if not c.isalpha():
            print("Your name should only contain letters. Please try again. ")
            return get_name()

    return my_name

# Function returns a number of characters to return from left to right. A maximum number of characters is passed as an argument. A try-catch block is used to convert the input to an integer. If the input is not a valid integer, the function recurses to get a valid input. If the input is greater than the maximum number of characters, the function recurses to get a valid input. Otherwise, the function returns the converted number.
def get_number_of_characters_for(max_number):
    number_of_characters_from_left = input(f"How many first letters to preview. Please enter a value less than or equal to {max_number} (n): ")
    try:
        converted_number = int(number_of_characters_from_left)
    except Exception as e:
        print("Please enter a valid integer.")
        return get_number_of_characters_for(max_number)

    if converted_number > max_number:
        print(f"There are only {max_number} characters in the string.")
        return get_number_of_characters_for(max_number)
    else:
        return converted_number

# Function gets two arguments: n as the given number of characters to return from left to right and name as the name to get characters from. If the length of the name or the number itself equals to zero, the function prints a description and returns an empty string. If the number is greater than the length of the name, the function prints an explanation and returns the entire name. Otherwise, it creates a substring for the first n characters of the name and returns it.
def get_characters_from_left(n, name):
    if len(name) == 0 or n == 0:
        print("Number of characters of the name and 'n' shall be greater than zero.")
        return ""

    if n > len(name):
        print(f"{n} is grater than number of character of '{name}'")
        return name

    substring = name[:n]
    print(f"First {n} character/s of '{name}' is/are: '{substring}'")
    return substring
# endregion

# region Task 2. Count the number of vowels

# Function checks if a character is a vowel. As the python does not provide a built-in function for vowel checks, and we have a limited count for the vowels in the natural language, the function initially creates a list of lower-cased characters vowels and then checks whether the given argument is in the list. The check is implemented in try-catch block, hence if a type or other kind of error occurs, the except block will print an explanation of the error and return False value.
def is_vowel(c):
    try:
        vowels =['a', 'e', 'i', 'o', 'u']
        return c.lower() in vowels
    except Exception as e:
        print(f"An error occurred: {e}.")
        return False

# Function counts the total number of vowels found in a given string. It uses a for loop to iterate through the name input and check each character for vowel. If the is_vowel function returns True, the local variable count is incremented by 1.
def count_vowels(name):
    count = 0
    for c in name:
        if is_vowel(c):
            count += 1
    print(f"There are {count} vowels in name '{name}'")
    return count
# endregion

# region Task 3. Reverse it
# The function reverses the given valid string. If the argument is not a valid string, the function returns an empty string. A for loop is used to iterate through the name input and reverse the string.
# A try-catch block is used to handle any exceptions that may occur during the execution of the function.
def reverse_name(name):
    try:
        len_name = len(name)
        if len_name == 0:
            print("Empty string.")
            return ""

        reversed_name = ""

        for i in range(len_name):
            reversed_name += name[len_name - 1 - i]
        print(f"The reversed string of '{name}' is: '{reversed_name}'")
        return reversed_name
    except Exception as e:
        print(f"Error: {name} is not a valid name.")
        return ""
# endregion

# region Execution
# get name
safe_name = get_name()

# get number for left side preview
print("\n")
max_num = len(safe_name)
safe_number = get_number_of_characters_for(max_num)

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

#Summary
"""
In the current assignment a program is created that takes a name as input and performs various operations on it. The program includes functions for counting vowels, reversing the name, and previewing a given number of characters from the left side of the string. The program also includes error handling for invalid inputs.
"""