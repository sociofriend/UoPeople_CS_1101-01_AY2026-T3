# Discussion Forum Unit 8

# region Part 1
"""
Describe how catching exceptions can help with file errors. Write a Python example that implements exception handling for any one of the file errors. Your code should use, try: except: blocks. Clearly mention the exception name in except block that you would handle. Include the code and output in your post along with necessary explanation.
"""

"""
Introduction

When working with files in Python, errors may happen for different reasons. 
For example, a file may not exist, the program may not have permission to open it, 
or the given path may refer to a directory instead of a file. If exceptions are not handled, 
the program will stop with an error message. 
Catching exceptions using try and except blocks allows the program to continue running 
and display a clear message about the problem.

In this example, exception handling is used to safely open files. 
The program catches FileNotFoundError, IsADirectoryError, PermissionError, OSError, and a general Exception. 
The os module is also used to check file paths before opening the file.
"""

import os


def practice_error_handling_for_files(file_name):
    try:
        print("Trying:", file_name)

        # check if path exists
        if not os.path.exists(file_name):
            print("Path does not exist")

        # try opening file
        fin = open(file_name, 'r')
        print("File opened successfully")

        fin.close()

    except FileNotFoundError as e:
        print("FileNotFoundError:", e)

    except IsADirectoryError as e:
        print("IsADirectoryError:", e)

    except PermissionError as e:
        print("PermissionError:", e)

    except OSError as e:
        print("OSError:", e)

    except Exception as e:
        print("Other error:", e)


# Case 1 — file does not exist
practice_error_handling_for_files("no_name")

# Case 2 — current file
practice_error_handling_for_files("Discussion_Forum_Unit_8.py")

# Case 3 — directory instead of file
practice_error_handling_for_files(".")

# Case 4 — root directory (may cause permission error on some systems)
practice_error_handling_for_files("/root")

"""
Output:
➜  CS_1101-01_AY2026-T3 git:(main) ✗ python Discussion_Forum_Unit_8.py
Trying: no_name
Path does not exist
FileNotFoundError: [Errno 2] No such file or directory: 'no_name'
Trying: Discussion_Forum_Unit_8.py
File opened successfully
Trying: .
IsADirectoryError: [Errno 21] Is a directory: '.'
Trying: /root
Path does not exist
FileNotFoundError: [Errno 2] No such file or directory: '/root'

"""

"""
Summary

 This example shows how catching exceptions helps prevent the program from crashing when file errors occur. 
 By using try and except blocks, different types of errors can be handled separately, 
 and the program can print clear messages explaining the problem. 
 This makes the program safer and easier to debug when working with files.
"""
# endregion

# region Part 2
"""
Describe how you might deal with a file error if you were writing a large production program. These descriptions should be general ideas in English, not actual Python code.
"""

"""
Explanation: When writing a large production program, I would try to follow common programming concepts like DRY 
(don't repeat yourself), KISS (keep it super simple) or SOLID and ZEN. I would consider implementing an ErrorHandler service 
which would be responsible for catching the errors and behaving in a pre-defined way.
 A sub service might be a FileErrorHandler service, which would be awair of all known error types regarding the workaround 
 with the files. This kind of approach would  help to centralize file-related operations' management and resource allocation.  
"""
# endregion