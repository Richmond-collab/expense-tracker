from expenses import Expense, CATEGORIES, sort_by_date


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


main()