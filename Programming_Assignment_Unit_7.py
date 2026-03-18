# Programming Assignment Unit 7

"""
In a program, a dictionary contains lists of students and their courses. The teacher is interested to have a dictionary that has the courses as key and the students enrolled in each course as values. Each key has three different values.
To address this requirement, write a function to invert the dictionary and implement a solution that satisfies the teacher’s need. In particular, the function will need to turn each of the list items into separate keys in the inverted dictionary. Also provide a technical explanation for the code and its output in minimum 200 words.
Sample input:
{
    'Stud1: ['CS1101', 'CS2402', 'CS2001'],
    'Stud2: ['CS2402’,’CS2001’,’CS1102’]
    }
Inverted Output:
{
‘CS1101’: [‘Stud1’],
‘CS2402’:['Stud1'',’Stud2’],
‘CS2001’: ['Stud1’,’Stud2’]
‘CS 1102’[‘Stud2’]
}
"""

# The initial dictionary with string-keys and list-values.
initial_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402','CS2001','CS1102']
}


# The function inverts the given dictionary from {"student_name": ["cours1", "course2"]} logic into {"course1":["student_name"], "course2":["student_name"]} logic, thus changing the logical relationship within the dictionary data. For instance, if the initial dictionary represents the list of courses each student takes, the inverted dictionary shows the list of students per each course. In the case of the initial list, the students are unique within the list, while multiple students may have the same course in their lists. The inverted dictionary introduced courses for its lists: courses are unique, while the same student may be included in multiple courses' lists.
def invert_dict(initial_dictionary):

    # We create an empty dict as a local variable to collect new data here.
    inverted_dict = {}

    # Use items() method of dictionary type to yield the pairs of the given argument.
    # Use (student, courses) tuple to retrieve the key and value if the pair.
    for student, courses in initial_dictionary.items():

        # We know that the values of the initial dictionary are lists, hence we will traverse through the items of the list with a for loop.
        for course in courses:

            # We assume that the items of the lists (courses) shall become the unique keys for the inverted dictionary, hence we check for each list's each course whether it is not in the list with 'not in' keywords.
            if course not in inverted_dict:

                # If the course is not in the list, we declare a new pair for the inverted dictionary with the course as a key and a list with a single value (singleton)
                inverted_dict[course] = [student]
                # In case the course is already in the keys of the new dict, we assume that it already has a valid list as a value, and we just append the new student name to it.
            else:

                # As we are sure that the students' names in the initial dictionary are unique, we do not double-check here whether the list already contains the current name.
                inverted_dict[course].append(student)

    # When the loop ends, we return the inverted dictionary.
    return inverted_dict


# Function runs a for loop through the items of the given list and prints the key and the value separated with a colon on a new line.
def beautiful_print(d):
    for key, value in d.items():
        print(key, " : ", value)

beautiful_print(invert_dict(initial_dict))

# Technical explanation

"""
To invert the initial dictionary from a student–course relationship into a course–student relationship, this assignment uses the items() built-in method of the dictionary type. A dictionary in Python is a mapping from keys to values, where each key is connected to one value, and this connection is called a key-value pair (Downey, 2014, p. 103, section 11.1, para. 2). In this program, the keys of the original dictionary are student names, and the values are lists of courses. The items() method allows the program to read both the key and the value at the same time by returning tuples from the dictionary (Downey, 2014, p. 120, section 12.6, para. 1). In the loop, the pair is stored in two variables called student and courses.

Inside the invert_dict() function, a new empty dictionary is created to store the inverted data. The program uses a for loop to go through every pair in the original dictionary. Since the value of each pair is a list, a second loop is required to go through every course inside that list.

For each course, the program checks whether the course already exists as a key in the new dictionary using the in operator (Downey, 2014, p. 76, section 8.9, para. 1). The in operator can check whether a key exists in a dictionary, which is an efficient operation because dictionaries use a hash table structure (Downey, 2014, p. 104, section 11.1, para. -1). If the course is not yet in the dictionary, a new key is created and the student name is placed inside a list. If the course already exists, the program appends the student name to the existing list. This technique is similar to dictionary inversion examples where lists are used as values to store multiple keys (Downey, 2014, p. 107, section 11.5, para. 2).

After all loops finish, the function returns the inverted dictionary, which shows each course with the list of students enrolled in it.
"""