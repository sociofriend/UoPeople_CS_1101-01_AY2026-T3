# Discussion Forum Unit 7

"""
This post shows how tuples are returned when using zip, enumerate, and items. Tuples are useful because they allow us to work with multiple values at the same time inside loops. When looping over lists or dictionaries, Python often returns tuples automatically. This makes the code shorter, cleaner, and easier to understand.
"""

# my custom list of countries
countries = ["Armenia", "Spain", "Columbia", "USA", "China"]

# my custom list of the populations of the countries
population = [
    2780000,    # Armenia
    48300000,   # Spain
    52500000,   # Columbia
    341000000,  # USA
    1410000000  # China
]

# my custom dictionary for countries (keys) and their populations (values)
country_dict = {
    "Armenia": 2780000,
    "Spain": 48300000,
    "Columbia": 52500000,
    "USA": 341000000,
    "China": 1410000000
}


# -------------------------------------------------
# Task 1 — Usage of zip function
# zip returns tuples that combine values from lists (Downey, 2014, p.118, Section 12.5)

def use_zip_with_lists(my_countries, their_population):
    """
    Loops over two lists simultaneously using the built-in zip function
    and prints tuples containing each country with its corresponding population.

    Parameters:
    my_countries (list of str): A list of country names.
    their_population (list of int): A list of populations corresponding to each country.

    Returns:
    None
    """
    for pair in zip(my_countries, their_population):
        print("Country and population:", pair)


def use_zip_with_dict(my_dict):
    """
    Loops over a dictionary using the zip function to combine its keys and values
    into tuples and prints each key-value pair as a tuple.

    Parameters:
    my_dict (dict): A dictionary where keys are country names and values are populations.

    Returns:
    None
    """
    for pair in zip(my_dict.keys(), my_dict.values()):
        print("Country and population:", pair)

# print("Call the 'use_zip_with_lists' function")
# print('------------------------------------------------')
# use_zip_with_lists(countries, population)
# print("\nCall the 'use_zip_with_dict' function")
# print('------------------------------------------------')
# use_zip_with_dict(country_dict)


# -------------------------------------------------
# Task 2 — Usage of enumerate function
# enumerate returns tuples (index, value) (Downey, 2014, p.119)

def use_enumerate_with_list(my_list):
    """
    Loops over a list using the built-in enumerate function and prints
    tuples containing the index and the corresponding item from the list.

    Parameters:
    my_list (list): A list of elements (e.g., country names).

    Returns:
    None
    """
    for item in enumerate(my_list):
        print("Index and country:", item)


def use_enumerate_with_dict(my_dict):
    """
    Loops over a dictionary using the built-in enumerate function and prints
    tuples containing the index and the dictionary key.

    Parameters:
    my_dict (dict): A dictionary where keys are elements (e.g., country names).

    Returns:
    None
    """
    for item in enumerate(my_dict):
        print("Index and key:", item)

# print("Call the 'use_enumerate_with_list' function")
# print('------------------------------------------------')
# use_enumerate_with_list(countries)
# print("\nCall the 'use_enumerate_with_dict' function")
# print('------------------------------------------------')
# use_enumerate_with_dict(country_dict)


# -------------------------------------------------
# Task 3 — Usage of items method
# items returns tuples (key, value) (Downey, 2014, p.120, Section 12.6)

def use_items_with_dict(my_dict):
    """
    Loops over a dictionary using the items() method and prints tuples
    containing each key and its corresponding value.

    Parameters:
    my_dict (dict): A dictionary where keys are elements (e.g., country names)
                    and values are their corresponding values (e.g., populations).

    Returns:
    None
    """
    for pair in my_dict.items():
        print("Key and value:", pair)


def use_items_with_lists(keys, values):
    """
    Combines two lists into a temporary dictionary using zip, then loops
    over the dictionary using items() to print tuples of key-value pairs.

    Parameters:
    keys (list): A list of keys (e.g., country names).
    values (list): A list of values corresponding to each key (e.g., populations).

    Returns:
    None
    """
    temp_dict = dict(zip(keys, values))
    for pair in temp_dict.items():
        print("Key and value:", pair)


print("Call the 'use_items_with_dict' function")
print('------------------------------------------------')
use_items_with_dict(country_dict)
print("\nCall the 'use_items_with_lists' function")
print('------------------------------------------------')
use_items_with_lists(countries, population)


# -------------------------------------------------
# Explanation:
"""
Tuples are very useful when working with loops in Python. Many loop functions such as zip, enumerate, and items return tuples automatically. This allows us to work with multiple values at the same time inside one loop.

The zip function combines two lists together and returns tuples. Each tuple contains one element from each list. This makes it easy to loop over two lists at the same time without using indexes (Downey, 2014, p.118, Section 12.5).

The enumerate function also returns tuples. Each tuple contains the index and the value. This is useful when we need both the position and the element inside the loop. It makes the code easier to read and understand (Downey, 2014, p.119).

The items method is used with dictionaries. It returns tuples where the first value is the key and the second value is the dictionary value. This allows us to loop through dictionary data in a simple and clear way without calling keys and values separately (Downey, 2014, p.120, Section 12.6).

Using tuples with zip, enumerate, and items makes the code shorter, cleaner, and easier to maintain. These functions help us write better loops when working with lists and dictionaries.
"""


# -------------------------------------------------
# Discussion Question: According to Downey, why is a reverse lookup much slower than a forward lookup?

# -------------------------------------------------
# References

"""
Downey, A. (2014). Think Python: How to think like a computer scientist.
"""