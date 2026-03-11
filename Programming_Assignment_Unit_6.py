# Programming Assignment Unit 6

# region (a). Consider that you are working as Data Analyst in an organization. The HR department needs you to carry out following operation on existing list of 10 employees name (you can assume 10 names in a list here).
# Task 1. Split the list into two sub-list namely subList1 and subList2, each containing 5 names.
def divide_list(any_list):
    try:
        subList1 = any_list[:5]
        subList2 = any_list[5:]
        return subList1, subList2
    except Exception as e:
        print(e)
        return None


# Task 2. A new employee (assume the name “Kriti Brown”) joins, and you must add that name in subList2.
def add_new_employee_to_list(name, names):
    try:
        names.append(name)
    except Exception as e:
        print(e)


# Task 3. Remove the second employee's name from subList1.
def remove_name_at(index, names):
    try:
        if len(names) > index:
            names.pop(index)
        else:
            print("Index out of range")
    except Exception as e:
        print(e)


# Task 4. Merge both the lists.
def merge_lists(list1, list2):
    try:
        merged_list = list1 + list2
        return merged_list
    except TypeError as type_error:
        print("TypeError occurred during list merge:", type_error)
        return None

# Task 5. Assume there is another list salaryList that stores salary of these employees. Give a rise of 4% to every employee and update the salaryList.

def raise_salaries_by_percent(number, salary_list):
    try:
        for index in range(len(salary_list)):
            salary_list[index] += salary_list[index] * number / 100
    except TypeError as type_error:
        print("TypeError occurred during salary calculation:", type_error)
        return None
    except ZeroDivisionError as zero_division_error:
        print("ZeroDivisionError occurred during salary calculation:", zero_division_error)
        return None
    except ValueError as value_error:
        print("ValueError occurred during salary calculation:", value_error)
        return None
    except Exception as error:
        print("Error occurred during salary calculation:", error)
        return None


# Task 6. Sort the SalaryList and show top 3 salaries.

def provide_top_salaries(number, list_of_salaries):
    try:
        if len(list_of_salaries) < number:
            print("Not enough salaries to display top", number)
            return None

        top_salaries_list = []
        sorted_salaries = sorted(list_of_salaries)

        initial_index = -1
        count = number

        while count > 0:
            top_salaries_list.append(sorted_salaries[initial_index])
            count -= 1
            initial_index -= 1
        return top_salaries_list

    except Exception as error:
        print(error)
        return None

# Execute

def execute_a():
    # create sublists
    print("- - - - - - - - - - - - - - - -")
    print("# TASK 1. Divide initial list into sub-lists.")
    global_list = ['John', 'Maria', 'Liam', 'Sofia', 'Noah', 'Emma', 'Lucas', 'Ava', 'Kenji', 'Amira']
    print("Initial list: ", global_list)
    subList1, subList2 = divide_list(global_list)
    print("subList1:", subList1)
    print("subList2:", subList2)
    print("- - - - - - - - - - - - - - - -")

    # add Kriti Brown to the end of subList2
    name = "Kriti Brown"
    print(f"\n# TASK 2. Add new employee {name} to the list.")
    print("Initial list:", subList2)

    add_new_employee_to_list(name, subList2)
    print("Modified list:", subList2)
    print("- - - - - - - - - - - - - - - -")

    # remove 2nd item of subList1
    index = 1
    print(f"\n# TASK 3. Remove from the list at index: {index}")
    print("Initial list:", subList1)
    remove_name_at(index, subList1)
    print("Modified list:", subList1)
    print("- - - - - - - - - - - - - - - -")

    # merge two lists
    print(f"\n# TASK 4. Merge lists: \n{subList1} \nand \n{subList2}")
    merged_list = merge_lists(subList1, subList2)
    print("\nMerged list:", merged_list)

    # raise salaries by 4 percent
    global_salary_list = [1000, 8000, 4000, 8540, 2000, 3420, 1230, 9000, 9090, 1090, 2900]
    print("\n# TASK 5. Raise salaries by 4% for employees.")
    print("Initial list of salaries:", global_salary_list)
    percent = 4
    raise_salaries_by_percent(percent, global_salary_list)
    print("Modified list of salaries:", global_salary_list)
    print("- - - - - - - - - - - - - - - -")

    # get top 3 salaries
    number_of_top_salaries = 3
    print(f"\n# TASK 6. Provide {number_of_top_salaries} top salaries from the list:\n{global_salary_list}")

    top_salaries_list = provide_top_salaries(number_of_top_salaries, global_salary_list)
    print(f"\n{number_of_top_salaries} top salaries from the list:\n{top_salaries_list}")
    print("- - - - - - - - - - - - - - - -")

# endregion

# region (b).
# 1) Design a program such that it converts a sentence into wordlist.
# 2) Reverse the wordlist then.

# Task 1. Converts a sentence into wordlist
def convert_sentence_to_wordlist(sentence):
    try:
        words_list = sentence.split()
        return words_list
    except Exception as error:
        print("An error occurred during sentence processing:", error)

# Task 2. Reverse the wordlist then
def reverse(words_list):
    try:
        reversed_list = []
        for index in range(len(words_list) - 1, -1, -1):
            reversed_list.append(words_list[index])
        return reversed_list
    except Exception as error:
        print("An error occurred during reverse of the list:", error)

def execute_b():
    original_sentence = "Today is a good day."
    print("Initial sentence:", original_sentence)
    converted_list = convert_sentence_to_wordlist(original_sentence)
    print("Converted list of words: ", converted_list)
    reversed_list = reverse(converted_list)
    print("Reversed list of words: ", reversed_list)
# endregion

execute_a()
execute_b()

