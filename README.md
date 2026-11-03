# Expense Tracker

A simple command-line expense tracker. Add expenses with an amount, category, note, and date, then list them sorted by date. Data is saved to `expenses.json` so it persists between runs.

## How to run

```bash
# (Optional) create and activate a virtualenv
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
# source venv/bin/activate    # macOS/Linux

python main.py
```

No external dependencies are required — this uses only the Python standard library.

## Features

- Add an expense (amount, category, note, optional date)
- List all expenses sorted by date
- Persistent storage via `expenses.json` (loads on start, saves on quit)
- Input validation: positive amounts, valid categories, `YYYY-MM-DD` dates
- Graceful exit on `Ctrl+C` or `Ctrl+D`

## Sample session

```
=== Expense Tracker ===
1. Add expense
2. List expenses
3. Quit
Choose an option: 1
Amount: 12.50
Category ['data', 'food', 'other', 'transport']: food
Note: Lunch
Date (YYYY-MM-DD, blank for today): 2026-11-01
Expense added.

=== Expense Tracker ===
1. Add expense
2. List expenses
3. Quit
Choose an option: 1
Amount: 8.00
Category ['data', 'food', 'other', 'transport']: transport
Note: Bus fare
Date (YYYY-MM-DD, blank for today):
Expense added.

=== Expense Tracker ===
1. Add expense
2. List expenses
3. Quit
Choose an option: 2
1. 2026-11-01  food         12.50  Lunch
2. 2026-11-03  transport      8.00  Bus fare

=== Expense Tracker ===
1. Add expense
2. List expenses
3. Quit
Choose an option: 3
Goodbye!
```

Bad input is handled without crashing:

```
Choose an option: 1
Amount: -5
Could not add expense: Amount must be a positive number
```

## Project structure

```
expense-tracker/
├── main.py          # CLI menu and entry point
├── expenses.py      # Expense model, categories, sort_by_date
├── storage.py       # load_expenses / save_expenses (JSON)
├── expenses.json    # persisted expense data (created on first run)
├── requirements.txt # no external dependencies
├── .gitignore       # venv, __pycache__, expenses.json
└── README.md
```

## requirements.txt

This project uses no outside libraries. `requirements.txt` is intentionally empty (or contains only a comment):

```
# No external dependencies
```
