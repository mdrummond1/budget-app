from MenuFunctions import get_datetime
from Tables import Budget, Category, Transaction
from Database import Database
from .MainMenu import format_menu
import datetime

def view_all_budgets(db: Database):
    print("viewing all budgets")
    db.connect()
    rows = db.__select_query__("SELECT * FROM budgets")
    budgets = [Budget(row) for row in rows]

    for b in budgets:
        print(b)

def view_selected_budget(db: Database) -> Budget:
    view_all_budgets(db)

    sel = int(input("Enter selected id: "))
    rows = db.__select_query__("SELECT * FROM budgets WHERE budget_id = (%s)", sel)
    if len(rows) >= 1:
        budget = Budget(rows[0])
        print(budget)
        return budget
    else:
        print("no budget with that id")

def add_new_budget(db: Database):
    start_date = None 
    while start_date is None:
        start_date = get_datetime()

    try:
        db.AddBudget(start_date)
        print("Budget added successfully!")
        view_all_budgets(db)
    except Exception as e:
        print("Failed to add new budget")
        print(e)

def view_budget_categories(db: Database):
    budget = view_selected_budget(db)
    print("SELECTED:")

    res = db.__select_query__("SELECT * FROM categories c WHERE c.budget_id = (%s)", budget.budget_id)
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