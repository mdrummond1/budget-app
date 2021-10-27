from misc_functions import format_menu
from Database import Database


class Category:
    def __init__(self, row) -> None:
        self.category_id = row[0]
        self.category_type = row[1]
        self.category_name = row[2]
        self.budgeted_amount = row[3]
        self.actual_total = row[4]
        self.amount_difference = row[5]


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
    for b in budgets:
        print(b)

    budget_id = int(input("Select budget id for new category"))


    types = db.__select_query__("SELECT category_type FROM category_types")
    for i, t in enumerate(types):
        print(f"{i}. {t}")

    cat_type = int(input("select category type: "))
    #put in some error handling herer

    cat_name = input("Category Name:")
    budgeted_amount = input("Budgeted amount for category:")

    res = db.__change_query__('INSERT INTO categories(category_type, budget_id, category_name, budgeted_amount VALUES((%s), (%s), (%s), (%s))', cat_type, budget_id, cat_name, budgeted_amount)

def modify_category(db: Database):
    print(f"changing category with id")

def delete_category(db: Database):
    print(f"deleting category with id")
