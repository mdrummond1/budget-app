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
        print('4. Modify Category')
        print('5. Delete Category')
        print('6. Main Menu')

        sel = int(input("Enter Selection:"))
            
        if sel == 1:
            view_all_categories(db)
        elif sel == 2:
            view_selected_category(db)
        elif sel == 3:
            add_new_category(db)
        elif sel == 4:
            modify_category(db)
        elif sel == 5:
            delete_category(db)
        elif sel == 6:
            break
        else:
            print("Invalid Option!")

        sel = 0

def view_all_categories(db: Database):
    categories  = [Category(row) for row in  db.__select_query__("SELECT * FROM categories")]
    for cat in categories:
        print(cat)

def view_selected_category(db: Database) -> Category:
    view_all_categories(db)
    sel = int(input("Select ID of category"))

    cat = db.__select_query__("SELECT * FROM categories c WHERE c.category_id = (%s)", sel)

    if len(cat) >=1:
        print(cat)
        return cat
    else:
        print("No category found")


def add_new_category(db: Database):
    budgets = [Budget(row) for row in db.__select_query__("SELECT * FROM budgets")]
    for budg in budgets:
        print(budg)

    budget_id = int(input("Select budget id for new category: "))


    types = db.__select_query__("SELECT category_type FROM category_types")
    for i, t in enumerate(types, start=1):
        print(f"{i}. {t[0]}")#returned as tuple with 1-element

    cat_type = int(input("select category type: "))
    #put in some error handling here

    cat_name = input("Category Name:")
    budgeted_amount = input("Budgeted amount for category: ")
    try:
        db.__change_query__('INSERT INTO categories(category_type, budget_id, category_name, budgeted_amount) VALUES(%s, %s, %s, %s)', cat_type, budget_id, cat_name, budgeted_amount)
    except Exception as e:
        print("failed to add new category")
        print(e)

def modify_category(db: Database):
    print(f"changing category with id")

def delete_category(db: Database):
    print(f"deleting category with id")

