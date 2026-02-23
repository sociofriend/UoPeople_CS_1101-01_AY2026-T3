# Written Assignment Unit 2
"""
This assignment demonstrates the use of variables, functions, and exception handling in Python.
A global constant for pi is defined, and a parameterized function is created to calculate the
circumference of a circle based on a given radius.
The function also includes error handling to ensure the program does not crash when invalid
data types are passed as arguments.
"""
#region Shared logic for beautiful print
# create a global function to print values in a beautiful format
def beautiful_print(val1: any, val2: any, total_width: int = 40):
    # convert values to string
    str1 = str(val1)
    str2 = str(val2)
    # print values with left alignment
    print(f"{str1:<{total_width - len(str2)}}{str2}")

# assign pi value to a global variable
global_pi = 3.14159
#endregion

#region Part 1
"""
In Part 1, the print_circum() function was implemented to calculate and print the circumference of a circle
using the formula (2 * pi * radius). The function handles both integer and floating-point inputs and
rounds the result to five decimal places. Additionally, exception handling was introduced to catch
type errors and other unexpected issues (commented).
"""

# Create a parameterized function that gets the radius value as an argument and returns the circumference.
# The name of the function is print_circum, and it takes radius as an argument, which is included in parentheses (Downey, 2015, Section 3.1, para.3)
def print_circum(radius):
    # Use Try Except block as the user can pass arguments of any type:
    # try block test code for errors, while the except block allows us to handle the thrown errors.
    # the else and finally blocks are optional and haven't been used in this example (W3Schools, n.d., para.1-4).
    try:
        # Calculate circumference using (2 * pi * radius) formula and assign the result to a local variable named ‘circum.'
        circum = 2 * radius * global_pi

        # Round the result to 5 decimal places, as our original pi value in the task is presented with 5 decimal places.
        circum = round(circum, 5)

        # Use print nested function to output the result:
        # print(f"Circumferences of the circle with radius of {radius} is \t {circum}")
        beautiful_print(f"Circumferences of the circle with radius of {radius} is", circum, 70)

    # Catch TypeError as we intentionally want to pass a string value to the radius parameter:
    # during the first trial, the interpreter threw a TypeError, when trying to pass a string value,
    # hence it was decided to specifically handle it.
    except TypeError as e:
        print(f"Example of Type Error calculating circumference: {e}")

    # Make sure that we catch all other exceptions:
    except Exception as e:
        print(f"Error calculating circumference: {e}")

# This is the print block already.
print("Part 1")
print("- - - - - - - - - -")
# Call print_circum function 3 times with different radius values, passing in arguments: integers and a floating number value
print_circum(1)
print_circum(11.0)
print_circum(111)

# # Intentionally call print_circum function passing a string value as an argument to check the function's error handling:
# print_circum("name")
#
# # Call print function passing a global variable in arguments:
# x = 4
# print_circum(x)
print("-------------------\n")
"""
This task implementation shows how to use global variables, functions, and exception handling in Python. 
A function was created to calculate the circumference of a circle 
using a given radius and a predefined value of pi. 
The program handles valid numeric inputs and manages invalid inputs using Try Except block, 
ensuring the code runs without crashing.
"""
# endregion





#region Part 2
"""
This code defines two classes, Item and Combo, to represent products and bundle offers with discounts.
It then creates three individual items and several combos of those items. 
Finally, it prints a table of products and combos, along with their final prices after discounts are applied.
	•	Item holds a product’s id, price, and title.
	•	Combo holds a bundle of items, a title, and a discount, and calculates both the original price and the discounted price.
	•	After defining items and combos, the program prints them out in a formatted list.
"""
# Define Item class with id, price, and title variables:
class Item:
    def __init__(self, id: int, price: float):
        # id and price are required parameters
        self.id = id
        self.price = price
        # title is generated based on id
        self.title = f"Item {id}"


# Define a Combo class with items, title, and discount variables:
class Combo:
    def __init__(self, items: list[Item], title: str, discount: float):
        # items, title, and discount are required parameters
        self.items = items
        # ideally we shall have a function, e.g. create_combo() with items list, which will generate title
        # but here we will hardcode it.
        self.title = title
        # In the potential create_combo() function, the discount could be auto-calculated based on the number of unique items, even for part of the purchase.
        self.discount = discount

        # price_without_discount and price_with_discount are calculated based on items and the discount
        self.price_without_discount = items[0].price + items[1].price
        self.price_with_discount = self.price_without_discount * (1 - self.discount)


# We will hard-code our 3 given items with given ids and prices, retrieved from the assignment's attached example screenshot
item1 = Item(1, 200.0)
item2 = Item(2, 400.0)
item3 = Item(3, 600.0)

# Create an array of the given 3 items:
items = [item1, item2, item3]

# Create an array of the given 3 combos:
combos_of_two = [
    Combo([item1, item2], "Combo 1 + 2", 0.1),
    Combo([item2, item3], "Combo 2 + 3", 0.1),
    Combo([item1, item3], "Combo 1 + 3", 0.1),
]

# Create the special combo of 3 items.
# Unlike the other combos, this combo's discount is 25%.
combo_of_three = Combo([item1, item2, item3], "Combo 1 + 2 + 3", 0.25)

# Implementing the print part:
print("Part 2")
print("Output")
print("- - - - - - - - - -")

# We will use our general beautiful_print() function which takes two variables,
# converts them into a string, and divides the hardcoded width into two parts.
# The first argument is presented left-aligned.
beautiful_print("Product(s)", "Price")
print("-------------------")

# We will use a for loop cicle to print all elements' details of items and combos arrays:
for i in items:
    beautiful_print(i.title, i.price)

for c in combos_of_two:
    beautiful_print(c.title, c.price_with_discount)

# And we will print the special combo separately:
beautiful_print(combo_of_three.title, combo_of_three.price_with_discount)
print("-------------------")
print("For delivery Contact: 98764678899")

"""
This example provides an opportunity to implement classes, functions, for loops, and exception handling.
All these independent blocks together compose the program to print the form (Downey, 2015, Section 3.3. para.2).
Adding a new function like beautiful_print() allowed handling formatted printing and reusing the code throughout the assignment.
While preparing the code, the flow of execution was taken into account and continuously improved until the moment the desired output was printed (Downey, 2015, Section 3.6., para.1).
"""
#endregion

#References
# Downey, A. (2015). Think Python: How to think like a computer scientist. 2nd Edition, Green Tea Press. Version 2.4.0. pp. 9-26
# W3Schools. (n.d.). 2nd Edition, Version 2.4.0Python Try Except. W3Schools. Retrieved on Feb. 12th, 2026 from https://www.w3schools.com/python/python_try_except.asp
