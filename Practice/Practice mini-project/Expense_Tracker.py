import os

expenses = []

#Step-1 :- if file doesn't exist
if not os.path.exists("expenses.txt"):
    open("expenses.txt","w").close()

#Step 2:- load existing expenses from file
with open("expenses.txt","r") as file:
    for line in file:
        line = line.strip()
        if line:
            category,amount = line.split(",")
            expenses.append({
                "category" : category,
                "amount" : float(amount)
            })

#creatig a function for save file
def save_expenses():
    with open("expenses.txt","w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")

#creating add expenses
def add_expenses():
    try:
        category = input("Enter the expense category = ")

        amount = float(input("Enter the Amount = ₹"))
    
    except Exception as e:
        print(e)
    
    expenses.append({
        'category' : category,
        'amount' : amount
    })

    save_expenses()
    print("Expenses Added Successfully!....")

#View the expenses
def view_expenses():
    if not expenses:
        print("No Expense Record!...")
    
    print("----Expenses----")
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}.{expense['category']} - ₹{expense['amount']:.2f}")
    print()


def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ₹{total:.2f}")


def delete_expenses():
    if not expenses:
        print("No Expense Record!...")
    
    print("----Expenses----")
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}.{expense['category']} - ₹{expense['amount']:.2f}")
    print()

    index = int(input("Which expenses do you want to delete? = "))

    if 1 <= index <= len(expenses):
        removed = expenses.pop(index-1)
        print(f"Expense Deleted Successfully : {removed['category']} - ₹{removed['amount']:.2f}")
    else:
        print("Invalid Index number!..please enter a valid index number")
    save_expenses()


choice= "y"
while choice!="n":
    print("=========Expense Tracker=========")
    print("1.Add Expenses")
    print("2.View Expenses")
    print("3.Total Expenses")
    print("4.Delete Expenses")
    print("5.Exit")

    ch = input("Enter Your Choice = ")

    if ch=="1":
        add_expenses()
    elif ch=="2":
        view_expenses()
    elif ch=="3":
        total_expenses()
    elif ch=="4":
        delete_expenses()
    elif ch=="5":
        print("Good Day!...")
    else:
        print("Invalid number")
    
    choice = input("Do you want to continue? (yes/no) = ")

    if choice=='n':
        print("See you tomorrow....")