"""Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:
"""

class Category:
    def __init__(self, category, ledger=None):
        self.ledger = ledger if ledger is not None else []
        self.category = category

    def __str__(self):
        # Title centered with asterisks
        title = self.category.center(30, "*")  

        # Ledger entries formatted properly
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]  # Truncate to 23 chars
            amount = f"{entry['amount']:7.2f}"  # Format amount with 2 decimal places, right-aligned
            items += f"{description:<23}{amount}\n"  

        # Total balance
        total = f"Total: {self.get_balance():.2f}"

        # Return the formatted string
        return f"{title}\n{items}{total}"

    

    def deposit(self, amount, description=''):
        """A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
        """
        self.ledger.append({'amount': amount, 'description': description})
        
        return self.ledger
    

    def withdraw(self, amount, description=''):
        """A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
        """
        if self.get_balance() >= amount:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
        

    def get_balance(self):
        """A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        """
        return sum(entry['amount'] for entry in self.ledger)
    

    def transfer(self, amount, category):
        """A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'. The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'. If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """
        if self.get_balance() >= amount:
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
    
    
    def check_funds(self, amount):
        """A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
        """
        if self.get_balance() < amount:
            return False
        return True


def create_spend_chart(categories):
    # Title of the chart
    title = "Percentage spent by category\n"

    # Step 1: Calculate total spending
    total_spent = sum(
        sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0)
        for category in categories
    )

    # Step 2: Compute each category's spending percentage (rounded down to nearest 10)
    spending_percentages = [
        int((sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0) / total_spent) * 100 // 10) * 10
        for category in categories
    ]

    # Step 3: Build the percentage bars
    chart = title
    for percentage in range(100, -1, -10):
        line = f"{percentage:>3}| "  # Right-aligned numbers (3 spaces) + '| '
        for value in spending_percentages:
            line += "o  " if value >= percentage else "   "
        chart += line + "\n"  # Maintain uniform spacing

    # Step 4: Add the horizontal line
    chart += "    " + "-" * ((len(categories) * 3) + 1) + "\n"

    # Step 5: Format category names vertically
    category_names = [category.category for category in categories]
    max_length = max(len(name) for name in category_names)
    padded_names = [name.ljust(max_length) for name in category_names]

    for i in range(max_length):
        name_line = "     "  # Five spaces for alignment
        for name in padded_names:
            name_line += name[i] + "  "  # Letter + two spaces
        chart += name_line.rstrip() + "  \n"  # Ensure consistent line length

    return chart


# Step 2: Create category objects
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Step 3: Add transactions (withdrawals represent expenses)
food.deposit(1000, "Initial deposit")
food.withdraw(300, "Groceries")
food.withdraw(200, "Restaurant")

clothing.deposit(500, "Initial deposit")
clothing.withdraw(150, "Shirt")
clothing.withdraw(100, "Shoes")

auto.deposit(1000, "Initial deposit")
auto.withdraw(400, "Gas")

# Step 4: Call the function
chart = create_spend_chart([food, clothing, auto])
print(chart)

print('\n')
print(food)
print('\n')
print(clothing)
print('\n')
print(auto)

