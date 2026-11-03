def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Add expense (coming soon)")
        elif choice == "2":
            print("List expenses (coming soon)")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()