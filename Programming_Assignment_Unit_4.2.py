# Part 2. Implement self-budgeting function for portfolio

class BudgetCalculator:
    def __init__(self, incomes, costs):
        self.incomes = incomes
        self.costs = costs

    def calculate_balance(self):
        total_income = sum(self.incomes)
        total_costs = sum(self.costs)   # already negative
        balance = total_income + total_costs
        return balance

    def display_balance(self):
        balance = self.calculate_balance()
        print(f"\nTotal income: {sum(self.incomes):.2f}")
        print(f"Total costs: {abs(sum(self.costs)):.2f}")
        print(f"Balance: {balance:.2f}")


# ---------- Input Logic ----------

def get_list(prompt, make_negative=False):
    while True:
        user_input = input(prompt)

        if not user_input.strip():
            print("Input cannot be empty. Please try again.")
            continue

        try:
            values = [float(value.strip()) for value in user_input.split(",")]

            # Prevent negative incomes
            if not make_negative and any(v < 0 for v in values):
                print("Income values cannot be negative. Please try again.")
                continue

            # Convert costs to negative numbers
            if make_negative:
                values = [-abs(v) for v in values]

            return values

        except ValueError:
            print("Invalid input detected. Please enter only numbers separated by commas.")


def get_income():
    return get_list(
        "Enter incomes separated by commas (e.g. 1000,2000,1500): "
    )


def get_costs():
    return get_list(
        "Enter costs separated by commas (e.g. 500,1200,300): ",
        make_negative=True
    )


# ---------- Main Program ----------

def main():
    incomes = get_income()
    costs = get_costs()

    calculator = BudgetCalculator(incomes, costs)
    calculator.display_balance()


if __name__ == "__main__":
    main()