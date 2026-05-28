import datetime
from modules.utils import line , get_standard_time
from modules.file_handler import save_data , load_data

def add_data():

    expenses=load_data()

    while True:
        line()
        print("1. Add Expense")
        print("2. Back to Menu")
        choice = input("\nEnter your choice 1 or 2 : ")
        
        if choice == "1":
            try:
                now=datetime.datetime.now()
                dtime=now.strftime("%d-%m-%Y_%H-%M-%S")

                category = input("Enter category like (Food/Travel/Rent etc..): ").title()
                amount = float(input("Enter amount: "))
                date=get_standard_time()
                added_data = {"user_date":date, "category": category, "amount": amount , "timestamp":dtime}
                expenses.append(added_data)
                print("\nData added successfully !")
                line()
                print(f"{added_data['user_date']} {added_data['category']:<8} {added_data['amount']:>10.2f} added on {dtime}")
                save_data(expenses)
            except ValueError:
                print("Invalid amount. Enter numbers only.")
        elif choice not in ("1","2"):
            print("\nInvalid option please enter 1 or 2 ")
        elif choice == "2":
            break

def show_expenses():
    expenses = load_data()
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\nTHE DATA OF EXPENSES")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['user_date']} {expense['category']:<20} ₹{expense['amount']:>10.2f} added on {expense['timestamp']}")       


def show_total():
    expenses=load_data()
    if len(expenses)==0:
        print("No data !")
    else:

        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['category']:<20} ₹{expense['amount']:>10.2f}")

    line()

    total=sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses : {len(expenses)} ")
    print(f"Total amount   : {total}")

    line()
        
def update_data():
    now = datetime.datetime.now()
    dtime = now.strftime("%Y-%m-%d_%H-%M")
    expenses=load_data()
    try:

        user_input=int(input("Enter the number you want to update:"))
        index=user_input-1
        if 0<=index <len(expenses):
            print(f"\n Current: {expenses[index]['category']} - ₹{expenses[index]['amount']}")
            line()
            category = input("Enter category like (Food/Travel/Rent etc..): ").title()
            amount=float(input("Enter the amount: "))
            user_date=get_standard_time()
            expenses[index]["category"] = category
            expenses[index]["amount"] = amount
            expenses[index]["user_date"]=user_date
            expenses[index]["timestamp"] = dtime
            print(f"{index}. {user_date}    {category}    ₹{amount} updated on {dtime}")
            print("Data updated ...")
            save_data(expenses)
        else:
            print("No existing data found to update")
        return
    except ValueError:

        print("Invalid amount. Enter numbers only.")

def delete_expense():

    expenses=load_data()

    if len(expenses) == 0:
        print(" No expenses to delete!")
        return

    try:

        user_input=int(input("Enter the expense serial number to delete :"))
        index=user_input-1
        if 0<=index<len(expenses):
            to_delete=expenses.pop(index)
            print(f"Deleted: {to_delete['category']} - ₹{to_delete['amount']}")
            save_data(expenses)
        else:
            print(f"The number was wrong enter in between 1 to {len(expenses)}")

    except ValueError:

        print("Try to enter numbers")

        return 

def edit_data():

    expenses=load_data()

    print("The expenses list to edit")
    for i, expense in enumerate(expenses, 1):
        
        print(f"{i}. {expense['user_date']} {expense['category']:<15} ₹{expense['amount']:>10.2f}")

    while True:

        line()
        print("Choose from three options")
        print("1.To update")
        print("2.To delete")
        print("3.To stop editing")
        line()

        user_choice=input("Enter a option 1 , 2 or 3 :")

        if user_choice=="1":
            update_data()
        elif user_choice=="2":
            delete_expense()
        elif user_choice=="3":
            break
        else:
            print("Invalid! Please enter 1 or 2 ...")