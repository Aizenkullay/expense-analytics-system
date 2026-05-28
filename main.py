from modules.expense_manager import *
from modules.analytics import *
from modules.utils import line

while True:

    line()

    print("EXPENSE ANALYTICS SYSTEM")

    line()

    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Summary")
    print("4. Edit Expense")
    print("5. Analysis")
    print("6. Monthly Analysis")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_data()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        edit_data()

    elif choice == "5":
        analysis()

    elif choice == "6":
        monthly_analysis()

    elif choice == "7":
        break