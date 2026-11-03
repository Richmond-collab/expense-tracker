# Expense Tracker CLI

A command-line app for recording and understanding your spending. It runs in the terminal with a text menu and saves your data to a JSON file, so your expenses are still there the next time you run it.

Built as the Month 1 project for my Python course.

## Features

- Add an expense (amount, category, note, date)
- List all expenses sorted by date
- Delete an expense by its number
- Summary: total spent, total per category, and biggest expense
- Filter by category or by month
- Data saved to `expenses.json` and loaded on start (works if the file is missing)
- Input validation: no negative amounts, unknown categories rejected, invalid dates rejected, no crashes on bad input

Categories: `food`, `transport`, `data`, `other`

## How to run

Requires Python 3.8 or newer. No external libraries are needed.

```bash
git clone https://github.com/Richmond-collab/expense-tracker.git
cd expense-tracker
python main.py
```

Optional: use a virtual environment first.

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux / Git Bash: venv/Scripts/activate
```

`expenses.json` is created automatically the first time you add an expense.

## Sample session

```
=== Expense Tracker ===
1. Add expense
2. List expenses
3. Delete expense
4. Summary
5. Filter
6. Quit
Choose an option: 1
Amount: 2500
Category ['data', 'food', 'other', 'transport']: food
Note: lunch
Date (YYYY-MM-DD, blank for today): 2026-10-03
Expense added.

Choose an option: 2
1. 2026-10-03  food         2,500.00  lunch
2. 2026-10-05  transport    1,200.00  bus fare

Choose an option: 4

Total spent: 3,700.00
By category:
  food          2,500.00
  transport     1,200.00
Biggest expense: 2026-10-03  food         2,500.00  lunch

Choose an option: 1
Amount: -50
Category ['data', 'food', 'other', 'transport']: food
Note: test
Date (YYYY-MM-DD, blank for today):
Could not add expense: Amount must be a positive number
```

## Project structure

```
expense-tracker/
  main.py            # menu loop and user input only
  expenses.py        # Expense class + add/delete/filter/summary functions
  storage.py         # load_expenses(path) / save_expenses(path, items)
  expenses.json      # created at run time (ignored by Git)
  README.md
  requirements.txt
  .gitignore
```

The menu code in `main.py` never touches the file directly. It calls functions in `storage.py` and `expenses.py`, which keeps each part simple and easy to change.

## Git workflow

Work was planned as GitHub Issues, built on separate feature branches, and merged through Pull Requests, with the program working after every merge.

## Author

Richmond