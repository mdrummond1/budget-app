from misc_functions import format_menu
from Database import *

class Budget:
    def __init__(self, row):
        self.__budget_id = row[0]
        self.__budget_start_date = row[1]
        self.__budget_end_date = row[2]
        self.__total_income = row[3]
        self.__total_liability = row[4]
        self.__net_amount = row[5]

    def __str__(self) -> str:
        return f"id: {self.__budget_id} start date: {self.__budget_start_date} end date: {self.__budget_end_date} income: {self.__total_income} liability: {self.__total_liability} net: {self.__net_amount}"

def view_all_budgets(db: Database):
    print("viewing all budgets")
    db.connect()
    rows = db.SelectQuery("SELECT * FROM BUDGETS")
    budgets = []
    for row in rows:
        budgets.append(Budget(row))

    for budget in budgets:
        print(budget)

def view_selected_budget(db: Database):
    print("viewing selected budget")

def add_new_budget(db: Database):
    print(f"adding new budget")

def modify_budget(db: Database):
    print(f"changing budget with id")

def show_budgets_menu(db: Database):
    
    sel = 0
    while sel != 5:
        print(format_menu("BUDGETS"))
        print("1. Show all budgets")
        print("2. Show selected budget")
        print("3. Add new budget")
        print("4. Modify budget")
        print("5. return to main menu")
    
        sel = int(input('Enter Selection: '))
        if sel == 1:
            view_all_budgets(db)
        elif sel == 2:
            view_selected_budget(db)
        elif sel == 3:
            add_new_budget(db)
        elif sel == 4:
            modify_budget(db)
        elif sel == 5:
            break
        else:
            print("Invalid Option")
        sel = 0

    
