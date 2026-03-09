#Discussion Forum Unit 6

# region Task 1. Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.

# To demonstrate how equivalent and identical work, let's first create two string objects a and b and assign them the same value 'a'.
# The demonstrate_equivalent_and_identical_for_values() function does this. Moreover, it returns the result of the "is" operation,
# which checks whether two variables refer to the same object (identity).

def demonstrate_equivalent_and_identical_for_values():
    a = "a"
    b = "a"
    print("Demonstrating equivalent and identical values for strings.")
    print("a is b; is identical: ", a is b)
    print("a == b; is equivalent ", a == b)


# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
Demonstrating equivalent and identical values for strings.
a is b; is identical:  True
a == b; is equivalent  True
"""

# Explanation
"""
In this example both comparisons return True. The == operator checks whether two objects have the same value (equivalence), while the "is" operator checks whether two variables refer to the same object (identity). In some cases Python may reuse the same string object internally, which is why "a is b" can return True for strings with the same value.
"""


# Now we will introduce both checks (is and '==') for lists.
def demonstrate_equivalent_and_identical_for_lists():
    a = ['a']
    b = ['a']

    print("\nDemonstrating equivalent and identical values for lists.")
    print("a is b; is identical: ", a is b)
    print("a == b; is equivalent ", a == b)


# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py

Demonstrating equivalent and identical values for lists.
a is b; is identical:  False
a == b; is equivalent  True
"""

# Explanation
"""The experiment shows that although both lists contain the same element and are therefore equivalent (the '==' comparison returns True), they are not identical (the 'is' operator returns False). This is because two separate list objects were created in memory, even though they contain the same elements.
"""


demonstrate_equivalent_and_identical_for_values()
demonstrate_equivalent_and_identical_for_lists()

# endregion

# region Task 2. Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

"""
To explain how objects, references, and aliasing relate to one another, we first note that in Python everything is an object.
Variables do not store the objects themselves but rather references to those objects.

For example, a string such as "a" is also an object. When variables a and b are assigned the same string value,
Python may internally reuse the same object, but this behavior should not be relied upon for identity comparisons.

Strings are immutable, which means their content cannot be changed after creation. If we want to modify a string,
Python must create a new object instead of changing the original one (Downey, 2015, p.96, Section 10.10).
"""
def demonstrate_object_reference_for_immutables():
    name1 = "Alan"
    name2 = "Alan"
    name3 = name1

    name1[1] = "d"
    name1[3] = "m"

    print("name1=", name1)
    print("name2=", name2)
    print("name3=", name3)

# We will automatically leave this commented to avoide new error previews.
# demonstrate_object_reference_for_immutables()

# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
Traceback (most recent call last):
  File "/Users/sociofriend/CS_1101-01_AY2026-T3/Discussion_Forum_Unit_6.py", line 81, in <module>
    demonstrate_object_reference_for_immutables()
  File "/Users/sociofriend/CS_1101-01_AY2026-T3/Discussion_Forum_Unit_6.py", line 74, in demonstrate_object_reference_for_immutables
    name1[1] = "d"
TypeError: 'str' object does not support item assignment
"""

# Explanation
"""
When trying to modify the characters of name1, Python raises a TypeError because strings are immutable. This means that once a string object is created, its content cannot be changed. Instead, Python must create a new string object with the desired modifications.
"""

def demonstrate_object_reference_for_immutables_by_creating_new_objects():
    name1 = "Alan"
    name2 = "Alan"
    name3 = name1

    name1 = name1[:1] + "d" + name1[2:]
    name1 = name1[:3] + "m" + name1[4:]

    print("name1=", name1)
    print("name2=", name2)
    print("name3=", name3)


# demonstrate_object_reference_for_immutables_by_creating_new_objects()

# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
name1= Adam
name2= Alan
name3= Alan
"""

# Explanation
"""
These examples demonstrate how object references work with immutable objects like strings in Python. When we modify the value of name1, Python creates a new string object and the variable name1 now refers to this new object. The variables name2 and name3 still refer to the original string object.
"""


# Finally, let's demonstrate how object references work with mutable objects like lists in Python.
def demonstrate_object_reference_for_mutable_objects():
    names1 = ["Alan", "Jenny"]
    names2 = names1

    names1.append("Lilit")
    names2.extend(["John", "Jasmin"])

    print("names1 =", names1)
    print("names2 =", names2)
    print("names1 is names2", names1 is names2)
    print("names1 == names2", names1 == names2)

demonstrate_object_reference_for_mutable_objects()

# Output
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
names1 = ['Alan', 'Jenny', 'Lilit', 'John', 'Jasmin']
names2 = ['Alan', 'Jenny', 'Lilit', 'John', 'Jasmin']
names1 is names2 True
names1 == names2 True
"""

# Explanation
"""
This example demonstrates aliasing. The variable names2 is assigned the same list object as names1. Therefore both variables refer to the same object in memory. When the list is modified through either variable, the change is visible through the other variable as well. When two variables refer to the same object, they are called aliases (Downey, 2015, p.97, section 10.10, para. 4).
"""

# endregion

# region Task 3.  Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references.

# the initial list which will be passed as an argument
list_argument = ['John', 'Doe']

# function which will receive a list as an argument, modify and return it
def function_to_modify_list(list_to_modify):
    list_to_modify += ['an appended item at the end of the list']
    return list_to_modify

# assign the returned list to a new variable
list_returned = function_to_modify_list(list_argument)

# print function result // return list
print("returned list", list_returned)
# print initial list
print("initial list", list_argument)

# compare if the returned and initial lists are identical
print("initial and returned lists are identical:", list_argument is list_returned)

# compare if the returned and initial lists are equivalent
print("initial and returned lists are equivalent:", list_argument == list_returned)


# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
returned list ['John', 'Doe', 'an appended item at the end of the list', 'an appended item at the end of the list']
initial list ['John', 'Doe', 'an appended item at the end of the list', 'an appended item at the end of the list']
initial and returned lists are identical: True
initial and returned lists are equivalent: True
"""

# Explanation:
"""
In this example we first created a list which is passed to function_to_modify_list as an argument. Inside the function, the parameter list_to_modify refers to the same list object as list_argument. The list is modified using the augmented operator '+=' which adds a new element to the existing list object. Because lists are mutable, the modification affects the original list object as well. Therefore the returned list and the original list_argument refer to the same object (they are identical), and consequently they are also equivalent (Downey, 2015, p.93, section 10.7, para. 3).
"""

# endregion

# Discussion Question: When you work with some data flow, where data is passed from one UI component to another one, in which cases you would prefer working with the same memory object, and in which cases you would copy the list?


# References
# Downey, A. (2015). Think Python: How to think like a computer scientist. pp. 89-98