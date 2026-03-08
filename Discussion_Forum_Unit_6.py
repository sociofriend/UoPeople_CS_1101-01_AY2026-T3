#Discussion Forum Unit 6

"""
Task 1. Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.

Task 2. Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

Task 3. Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references.
"""


# Task 1. Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.

# To demonstrate how equivalent and identical work for value types and reference types, let's first create value type objects a and b and both assign 'a' value. The demonstrate_equivalent_for_values() function does this. Moreover, it returns the result of is operation, which checks two objects to be identical.
def demonstrate_equivalent_and_identical_for_values():
    a = "a"
    b = "a"
    print("Demonstrating equivalent and identical values for strings.")
    print("a is b; is identical: ", a is b)
    print("a == b; is equivalent ", a == b)
#Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
Demonstrating equivalent and identical values for strings.
a is b; is identical:  True
a == b; is equivalent  True
"""
# We clearly see that, in the case of strings, the 'is' keyword returns true, as a and b both refer to 'a' value. We get the same result if we compare a and b with '=='.

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

# The experiment shows that when we just assign the same list to different variables, although they are equivalent ('==' comparison returns True), however, they are not identical ('is' keyword returns False). This is because lists are mutable objects and are stored in different memory locations even if they have the same content.

# demonstrate_equivalent_and_identical_for_values()
# demonstrate_equivalent_and_identical_for_lists()

# Task 2. Using your own Python list examples, explain how objects, references, and aliasing relate to one another.
"""
 We will use the same example from task 1 to explain how objects, references and aliasing relate to one another. Here we should first differentiate between 'value' and 'object'. 'a' is a value, and ['a'] is an object which includes 'a' value. When we assign the same 'a' value to a and b variables, they both refer to the same string, but they do not refer to the same memory location (Downey, 2015, p.96, Section 10.10). As strings are immutable, we may not do something like this: a[4] = 'b', to change the value to which a refers, we will need to reassign ti another value, hence the reference itself will be changed.
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

# demonstrate_object_reference_for_immutables()
# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
Traceback (most recent call last):
  File "/Users/sociofriend/CS_1101-01_AY2026-T3/Discussion_Forum_Unit_6.py", line 81, in <module>
    demonstrate_object_reference_for_immutables()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/sociofriend/CS_1101-01_AY2026-T3/Discussion_Forum_Unit_6.py", line 74, in demonstrate_object_reference_for_immutables
    name1[1] = "d"
    ~~~~~^^^
TypeError: 'str' object does not support item assignment
"""
# When trying to mutate the name1 variable's characters, we get a TypeError because strings are immutable in Python. This means that once a string is created, its content cannot be changed. Instead, if you want to modify a string, you need to create a new string with the desired changes.

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
#Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
name1= Adam
name2= Alan
name3= Alan
"""
#These examples demonstrate how object references work with immutable objects like strings in Python. When you try to modify an immutable object, Python creates a new object with the desired changes instead of modifying the original object.

#Finally, let's demonstrate how object references work with mutable objects like lists in Python.

def demonstrate_object_reference_for_mutable_objects():
    names1 = ["Alan", "Jenny"]
    names2 = names1

    names1.append("Lilit")
    names2.extend(["John", "Jasmin"])

    print("names1 =", names1)
    print("names2 =", names2)
    print("names1 is names2", names1 is names2)
    print("names1 == names2", names1 == names2)

# demonstrate_object_reference_for_mutable_objects()

# Output
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
names1 = ['Alan', 'Jenny', 'Lilit', 'John', 'Jasmin']
names2 = ['Alan', 'Jenny', 'Lilit', 'John', 'Jasmin']
names1 is names2 True
names1 == names2 True
"""
# And here we go: the output of demonstrate_object_reference_for_mutable_objects() function demonstrates that when two variables refer to the same mutable object, modifying one variable affects the other variable as well. And, when comparing the two variables using the == operator, they are considered equal because they contain the same elements. When both variables keep reference/point to the same memory object, we say that they are aliases (Downey, 2015, p.97, section 10.10, para. 4).

# Task 3.  Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references.

list_argument = ['John', 'Doe']

def function_to_modify_list(list_to_modify):
    list_to_modify += ['an appended item at the end of the list']
    return list_to_modify

list_returned = function_to_modify_list(list_argument)

print(function_to_modify_list(list_argument))
print(list_argument)
print("initial and returned lists are identical:", list_argument is list_returned)
print("initial and returned lists are equivalent:", list_argument == list_returned)


# Output:
"""
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_6.py
['John', 'Doe', 'an appended item at the end of the list', 'an appended item at the end of the list']
['John', 'Doe', 'an appended item at the end of the list', 'an appended item at the end of the list']
initial and returned lists are identical: True
initial and returned lists are equivalent: True
"""
#In this example we initially created a list which is passed to function_to_modify_list as an argument. In the body of the function, we appended a new item which was added to the end of the list. The function then returns the modified list. The list modification was implemented with the augmented operator '+=' (Downey, 2015, p.93, section 10.7, para. 3). When we print both the initial list that was passed as an argument and the list returned by the function, we see that they are identical, hence also equivalent.


# Discussion Question: When you work with some data flow, where data is passed from one UI component to another one, in which cases you would prefer working with the same memory object, and in which cases you would copy the list?

#References
# Downey, A. (2015). Think Python: How to think like a computer scientist. pp. 89-98