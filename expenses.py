from datetime import date

CATEGORIES = {"food", "transport", "data", "other"}


class Expense:
    def __init__(self, amount, category, note="", when=None):
        if amount <= 0 or amount != amount or amount == float("inf"):
            raise ValueError("Amount must be a positive number")
        if category not in CATEGORIES:
            raise ValueError(f"Category must be one of {sorted(CATEGORIES)}")
        if when:
            try:
                date.fromisoformat(when)
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
        self.amount = amount
        self.category = category
        self.note = note
        self.when = when or date.today().isoformat()

    def to_dict(self):
        return {"amount": self.amount, "category": self.category,
                "note": self.note, "when": self.when}

    def __str__(self):
        return f"{self.when}  {self.category:<10} {self.amount:>10,.2f}  {self.note}"


def sort_by_date(items):
    return sorted(items, key=lambda e: e.when)

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