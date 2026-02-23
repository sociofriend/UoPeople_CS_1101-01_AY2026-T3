from xxlimited_35 import Str


# =========================================================
# Example 1: Define a function that takes an argument.
#            Call the function.
#            Identify what code is the argument and what code is the parameter.
# =========================================================

def function_with_argument(first_argument, example_number, message):
    type_of_argument = type(first_argument)
    print(
        f"Example {example_number}: Function with {type_of_argument} type of argument:",
        first_argument,
    )
    print(f"Special message: {message}")


function_with_argument("my_custom_argument", 1, "Default message")

"""
Example 1: Function with arguments.

The name of the function is `function_with_argument`.
The function originally has three parameters:
- first_argument
- example_number
- message

A parameter is a name used inside a function to refer to the value passed as an argument (Downey, 2015, 3.13, p. 26, para.2).
An argument is a value provided to a function when the function is called (Downey, 2015, 3.13, p. 26, para.4).

Notes:
- The function definition starts with the `def` keyword (Downey, 2015, 3.4, p. 19, para.4).
- The function body is a sequence of statements inside a function definition (Downey, 2015, 3.13, p. 26, para.1), and it is indented by 4 spaces (Downey, 2015, 3.4, p. 19, para.6).
- A local variable is a variable defined inside a function (Downey, 2015, 3.13, p. 26, para.5). In this function it stores the type of the first argument.

Example call:
    function_with_argument("my_custom_argument", 1, "Default message")

Output:
    Example 1: Function with <class 'str'> type of argument: my_custom_argument
    Special message: Default message
"""


# =========================================================
# Example 2: Different kinds of arguments
# =========================================================

# Value argument
function_with_argument(
    "flower",
    2.1,
    "Value argument example.\n"
)

# Variable argument
variable_as_an_argument = 12345678
function_with_argument(
    variable_as_an_argument,
    2.2,
    "Variable argument example.\n"
)

# Expression argument
function_with_argument(
    1 + 1 - 2,
    2.3,
    "Expression argument example\n"
)

"""
Example 2: Calling the function with different kinds of arguments.

The same function from Example 1 is called three times.
Each call uses a different kind of argument for the first parameter.

Types of arguments:

1. Value argument:
   - A value written directly in the function call.
   - Example: "flower"

2. Variable argument:
   - A variable that stores a value.
   - Example: variable_as_an_argument

3. Expression argument:
   - A calculation that Python evaluates first.
   - Example: 1 + 1 - 2

Notes:
- A value is one of the basic things a program works with, like a letter or a number(Downey, 2015, 1.5, p. 4, para.1).
- Python does not require setting types in function blueprints because it is a dynamically typed language. Python decides the type at runtime. (Bhalla, 2025)


Output:
    Example 2.1: Function with <class 'str'> type of argument: flower
    Special message: Value argument example.

    Example 2.2: Function with <class 'int'> type of argument: 12345678
    Special message: Variable argument example.

    Example 2.3: Function with <class 'int'> type of argument: 0
    Special message: Expression argument example
"""


# =========================================================
# Example 3: Local variable scope
# =========================================================

def function_with_local_variable():
    local_variable = "I am local"
    print(f"Local variable inside function: {local_variable}")


function_with_local_variable()

try:
    print(f"Local variable outside function: {local_variable}")
except NameError as e:
    print(f"Error: {e}")

"""
Example 3: Function with a local variable.

The variable `local_variable` is created inside the function.
This makes it a local variable.

Notes:
- A variable created inside a function belongs to the local scope of that function, and can only be used inside that function. They cannot be accessed outside the function(W3Schools, n.d., para.4).

Output:
    Local variable inside function: I am local
    Error: name 'local_variable' is not defined
"""


# =========================================================
# Example 4: Function parameter scope
# =========================================================

def function_with_parameter_with_unique_name(parameter_name: str):
    print(f"Parameter unique name inside function: {parameter_name}")


function_with_parameter_with_unique_name("unique_parameter")

try:
    print(f"Parameter name outside function: {parameter_name}")
except NameError as e:
    print(f"Error: {e}")

"""
Example 4: Function parameter scope.

The function has a parameter named `parameter_name`.
Function parameters behave like local variables.

Notes:
- Parameters exist only inside the function.
- They cannot be used outside the function body (see explanation above).

Output:
    Parameter unique name inside function: unique_parameter
    Error: name 'parameter_name' is not defined
"""


# =========================================================
# Example 5: Global vs local variables with the same name
# =========================================================

variable = "I am global"

def function_with_same_name_variable():
    variable = "I am local"
    print(f"Variable inside function: {variable}")


print(f"Variable before function call: {variable}")

function_with_same_name_variable()

print(f"Variable after function call: {variable}")

"""
Example 5: Global and local variables with the same name.

Two variables share the same name `variable`:
- One is global (outside the function, global scope).
- One is local (inside the function local scope).

Notes:
- A variable created in the main body of the Python code is a global variable and belongs to the global scope(W3Schools, n.d., Global Scope, para.1).
- The local variable does not affect the global variable.
- Python treats them as separate variables.
- And when we use the same name for the local and global variables, the local variable takes priority inside the function's scope (W3Schools, n.d., Naming Variables, para.1).

Output:
    Variable before function call: I am global
    Variable inside function: I am local
    Variable after function call: I am global
"""


#References
# Downey, A. (2015). Think Python: How to think like a computer scientist. pp. 9-26
# Bhalla H. (2025). Why Python is Called Dynamically Typed?. GeeksForGeeks. https://www.geeksforgeeks.org/python/why-python-is-called-dynamically-typed/
# W3Schools. (n.d.). Python Scope. W3Schools. Retrieved on Feb. 8th, 2026 from https://www.w3schools.com/python/python_scope.asp