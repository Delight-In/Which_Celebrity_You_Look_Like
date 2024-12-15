class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = input("Enter the date (YYYY-MM-DD): ")

    def __str__(self):
        return f"{self.date} - {self.description}: ${self.amount} ({self.category})"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully!")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n--- Expenses ---")
        for expense in self.expenses:
            print(expense)

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the expense amount: $"))
            description = input("Enter a description for the expense: ")
            category = input("Enter the expense category (e.g., Food, Entertainment, etc.): ")
            expense = Expense(amount, description, category)
            tracker.add_expense(expense)

        elif choice == '2':
            tracker.show_expenses()

        elif choice == '3':
            tracker.total_expenses()

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
