from datetime import date

from expenses import Expense, CATEGORIES, sort_by_date
from storage import load_expenses, save_expenses

DATA_FILE = "expenses.json"


def parse_date(value):
    if not value:
        return None
    try:
        date.fromisoformat(value)
    except ValueError as err:
        raise ValueError(f"Invalid date '{value}': {err}")
    return value


def add_expense(items):
    try:
        amount = float(input("Amount: "))
        category = input(f"Category {sorted(CATEGORIES)}: ").strip().lower()
        note = input("Note: ")
        when = parse_date(input("Date (YYYY-MM-DD, blank for today): ").strip())
        items.append(Expense(amount, category, note, when))
        print("Expense added.")
    except ValueError as err:
        print(f"Could not add expense: {err}")


def list_expenses(items):
    if not items:
        print("No expenses yet.")
        return
    for number, e in enumerate(sort_by_date(items), start=1):
        print(f"{number}. {e}")


def main():
    items = load_expenses(DATA_FILE)
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(items)
        elif choice == "2":
            list_expenses(items)
        elif choice == "3":
            save_expenses(DATA_FILE, items)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
