from os import X_OK
from misc_functions import format_menu
from Database import *
from .Categories import *
import datetime

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
    rows = db.SelectQuery("SELECT * FROM budgets")
    budgets = [Budget(row) for row in rows]

    for b in budgets:
        print(b)

def view_selected_budget(db: Database):
    view_all_budgets(db)

    sel = int(input("Enter selected id: "))

    rows = db.SelectQuery("SELECT * FROM budgets WHERE budget_id = (%s)", sel)
    if len(rows) >= 1:
        budget = Budget(rows[0])
        print(budget)
    else:
        print("no budget with that id")

    return budget


def add_new_budget(db: Database):
    budget = None
    start_year = int(input("Enter year: "))
    start_month = int(input("Enter month: "))
    start_day = int(input("Enter day: "))
    
    try:
        start_date = datetime.date(start_year, start_month, start_day)
    except ValueError:
        print("Invalid date entered")
        return

    try:
        db.ChangeQuery("INSERT INTO budgets(budget_start_date) VALUES((%s))", start_date)
        print("Budget added successfully!")
    
        rows = db.SelectQuery("SELECT * FROM budgets")
        budget = Budget(rows[-1])
        print(budget)
    except Exception as e:
        print("Failed to add new budget")
        print(e)

def view_budget_categories(db: Database):
    budget = view_selected_budget(db)
    res = db.SelectQuery("SELECT * FROM categories c WHERE c.budget_id = (%s)", budget.__budget_id)
    categories = [Category(row) for row in res]

    for cat in categories:
        print(cat)

def show_budgets_menu(db: Database):
    
    sel = 0
    while sel != 5:
        print(format_menu("BUDGETS"))
        print("1. Show all budgets")
        print("2. Show selected budget")
        print("3. Add new budget")
        print("4. Show all categories for budget")
        print("5. return to main menu")
    
        sel = int(input('Enter Selection: '))
        if sel == 1:
            view_all_budgets(db)
        elif sel == 2:
            view_selected_budget(db)
        elif sel == 3:
            add_new_budget(db)
        elif sel == 4:
            view_budget_categories(db)
        elif sel == 5:
            break
        else:
            print("Invalid Option")
        sel = 0

    
