from os import execlp
from Database import Database
from Tables import Category, Budget
from .MainMenu import format_menu

#category functions
def show_categories_menu(db: Database):

    sel = 0
    while sel != 6:
        print(format_menu("CATEGORIES"))
        print('1. View All Categories')
        print('2. View Selected Categories')
        print('3. Add New Category')
        print('4. Change Category Budgeted Amount')
        print('5. Change Category Name')
        print('6. Delete Category')
        print('7. Main Menu')

        sel = int(input("Enter Selection: "))
            
        if sel == 1:
            view_all_categories(db)
        elif sel == 2:
            view_selected_category(db)
        elif sel == 3:
            add_new_category(db)
        elif sel == 4:
            change_budgeted_amount(db)
        elif sel == 5:
            change_category_name(db)
        elif sel == 6:
            delete_category(db)
        elif sel == 7:
            break
        else:
            print("Invalid Option!")

        sel = 0

def view_all_categories(db: Database):
    categories  = db.GetCategories()
    for cat in categories:
        print(cat)

def view_selected_category(db: Database) -> Category:
    view_all_categories(db)
    sel = int(input("Select ID of category: "))

    category = db.GetCategoryFromId(sel)
    if category is not None:
        print(category)
        return category
    else:
        print("no category with that id")

def add_new_category(db: Database):
    budgets = [Budget(row) for row in db.__select_query__("SELECT * FROM budgets")]
    for budg in budgets:
        print(budg)

    budget_id = int(input("Select budget id for new category: "))

    types = db.GetCategoryTypes()
    
    for i, t in enumerate(types, start=1):
        print(f"{i}. {t[0]}")#returned as tuple with 1-element

    cat_type = int(input("select category type: "))
    #put in some error handling here

    cat_name = input("Category Name:")
    budgeted_amount = input("Budgeted amount for category: ")
    
    try:
        db.AddCategory(budget_id, cat_type, cat_name, budgeted_amount)
        print("Category successfully added!")
    except Exception as e:
        print("failed to add new category")
        print(e)

def change_budgeted_amount(db: Database):
    category = view_selected_category(db)
    if category is None:
        print('Cancelling change...')
    new_amount = input("enter new budgeted amount: ")
    db.ModifyCategoryAmount(category.category_id, new_amount)

def change_category_name(db: Database):
    category = view_selected_category(db)
    if category is None:
        print('Cancelling change')

    new_name = input("Enter new category name: ")
    db.ModifyCategoryName(category.category_id, new_name)
    
def delete_category(db: Database):
    category = view_selected_category(db)
    if category is None:
        print('Cancelling change...')
    try: 
        db.DeleteCategory(category.category_id)
    except Exception as e:
        print("problem deleting category")
        print(e)
