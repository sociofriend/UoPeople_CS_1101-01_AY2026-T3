# region Part 1: calculate hypotenuse of a right triangle

# First, let's create a function as it is:
def calc_hypotenuse_of_right_angle(a, b):
    print(f"Sides are {a} and {b}")
# Then let's call it:
calc_hypotenuse_of_right_angle(3, 4)

## The output clearly demonstrates that the precondition is not violated, and the arguments are printed successfully.
## Now we can proceed to satisfy the post-condition, for which we will define the formula of calculating the hypotenuse.
## "The hypotenuse of a right triangle is always the side opposite the right angle. It is the longest side in a right triangle. The formula for calculation is as follows: c = √(a² + b²) (Mattecentrum, n.d., para. 3).
# In python, we can use the math.sqrt() function to calculate the square root. Python’s math.sqrt() function requires a positive value; hence we are sure that our hypotenuse will be positive(TradingCode, 2022, Precise square root: math.sqrt(), para. 1).

import math

def calc_hypotenuse_of_right_angle(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    print(f"Hypotenuse is {hypotenuse}")

calc_hypotenuse_of_right_angle(3, 4)
calc_hypotenuse_of_right_angle(1, 2)
calc_hypotenuse_of_right_angle(26.9, 4.3)

# endregion

# region Part 2. Implement self-budgeting function for portfolio

# Let's create a function, which will allow the user to add all incomes and costs of the month and get the balance
# First, define the function:
def self_budgeting(income, costs):
    print(f"Total income: {income} and Total costs: {costs}")

self_budgeting(1000, 3000)

def self_budgeting(income, costs):
    sum_income = sum(income)
    sum_costs = sum(costs)
    balance = sum_income - sum_costs
    print(f"Balance is {balance:.2f}")


# Now we need to test the function against pre-condition violation:
# self_budgeting(1000, 3000)

def get_list(prompt, make_negative=False):
    while True:
        user_input = input(prompt)
        # check for empty input

        if not user_input.strip():
            print("Input cannot be empty. Please try again.")
            continue

        try:
            values = [float(value.strip()) for value in user_input.split(",")]
            # prevent negative incomes
            if not make_negative and any(v < 0 for v in values):
                print("Income values cannot be negative. Please try again.")
                continue
            # convert costs to negative numbers if required
            if make_negative:
                values = [-abs(v) for v in values]
            return values

        except ValueError:
            print("Invalid input detected. Please enter only numbers separated by commas.")


def get_income():
    arr = get_list(
        "Enter incomes separated by commas (e.g. 1000,2000,1500): "
    )
    print(arr)
    return arr


def get_costs():
    arr = get_list(
        "Enter costs separated by commas (e.g. 500,1200,300): ",
        make_negative=True
    )
    print(arr)
    return arr


self_budgeting([1, 1, 1], [2, 2, 2])
# endregion

"""
References

Mattecentrum.(n.d.).The Pythagorean Theorem. https://www.mathplanet.com/education/pre-algebra/right-triangles-and-algebra/the-pythagorean-theorem
TradingCode.(2022).How to calculate the square root in Python?.TradingCode.https://www.tradingcode.net/python/math/square-root/
"""