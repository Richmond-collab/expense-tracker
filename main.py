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


def list_expenses(items):
    if not items:
        print("No expenses yet.")
        return
    for number, e in enumerate(sort_by_date(items), start=1):
        print(f"{number}. {e}")


def main():
    items = []
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


def filter_menu(items):
    print("1. By category")
    print("2. By month")
    choice = input("Filter by: ").strip()

    if choice == "1":
        category = input(f"Category {sorted(CATEGORIES)}: ").strip().lower()
        if category not in CATEGORIES:
            print("Unknown category.")
            return
        results = filter_by_category(items, category)
    elif choice == "2":
        month = input("Month (YYYY-MM): ").strip()
        if len(month) != 7 or month[4] != "-":
            print("Please use the format YYYY-MM, e.g. 2026-10.")
            return
        results = filter_by_month(items, month)
    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching expenses.")
        return
    for number, e in enumerate(sort_by_date(results), start=1):
        print(f"{number}. {e}")
main()