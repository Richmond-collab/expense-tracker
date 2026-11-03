import json
import os

from expenses import Expense


def load_expenses(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read saved data, starting empty.")
        return []
    return [Expense(d["amount"], d["category"], d["note"], d["when"]) for d in data]


def save_expenses(path, items):
    with open(path, "w") as f:
        json.dump([e.to_dict() for e in items], f, indent=2)