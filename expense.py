import json
from datetime import datetime

EXPENSE_FILE = "expenses.json"

def load_expenses():
    
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):

    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food, Transport, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d")  # Auto timestamp

    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "date": date})
    
    save_expenses(expenses)
    print("Expense added successfully!\n")

def view_summary():
    
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total_spent = sum(exp["amount"] for exp in expenses)
    category_summary = {}

    for exp in expenses:
        category_summary[exp["category"]] = category_summary.get(exp["category"], 0) + exp["amount"]

    print(f"Total spent: ${total_spent:.2f}")
    print("Spending by category:")
    for category, amount in category_summary.items():
        print(f"  {category}: ${amount:.2f}")
    print()

def spending_over_time():
    
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    time_based_summary = {}

    for exp in expenses:
        date = exp["date"]
        time_based_summary[date] = time_based_summary.get(date, 0) + exp["amount"]

    print("Spending over time:")
    for date, amount in sorted(time_based_summary.items()):
        print(f"{date}: ${amount:.2f}")
    print()

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View Spending Over Time")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            spending_over_time()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

	  	