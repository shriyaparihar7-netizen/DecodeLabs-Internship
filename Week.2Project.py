expenses = []

savings = int(input("Enter your current savings: "))

while True:
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. View Current Savings")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter what you spent on: ")
        amount = int(input("Enter Expense Amount: "))

        expenses.append([item, amount])
        savings = savings - amount

        print("Expense Added Successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added.")
        else:
            print("\nYour Expenses:")
            for expense in expenses:
                print("Item:", expense[0], "| Amount:", expense[1])

    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense[1]

        print("Total Expense =", total)

    elif choice == "4":
        print("Current Savings =", savings)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")