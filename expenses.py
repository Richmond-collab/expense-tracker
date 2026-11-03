from datetime import date

CATEGORIES = {"food", "transport", "data", "other"}


class Expense:
    def __init__(self, amount, category, note="", when=None):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if category not in CATEGORIES:
            raise ValueError(f"Category must be one of {sorted(CATEGORIES)}")
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

        def filter_by_category(items, category):
          return [e for e in items if e.category == category]


def filter_by_month(items, month):
    # month is a string like "2026-10"
    return [e for e in items if e.when.startswith(month)]