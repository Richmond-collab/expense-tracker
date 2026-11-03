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