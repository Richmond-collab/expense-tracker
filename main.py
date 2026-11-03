from json.tool import main
from random import choice

from expenses import Expense, CATEGORIES, sort_by_date
from storage import load_expenses, save_expenses

DATA_FILE = "expenses.json"


def add_expense(items):
    try:
        amount = float(input("Amount: "))
        category = input(f"Category {sorted(CATEGORIES)}: ").strip().lower()
        note = input("Note: ")
        when = input("Date (YYYY-MM-DD, blank for today): ").strip() or None
        items.append(Expense(amount, category, note, when))
        print("Expense added.")
    except ValueError as err:
        print(f"Could not add expense: {err}")


def main():
    items = load_expenses(DATA_FILE)
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Delete expense")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(items)
        elif choice == "2":
            list_expenses(items)
        elif choice == "3":
            delete_expense_menu(items)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()