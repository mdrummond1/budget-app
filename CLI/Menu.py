from Table import *

def main_menu():
    print("showing main menu")

def budgets_menu():
    print(format_menu("BUDGETS"))

def categories_menu():
    print(format_menu("CATEGORIES"))

def transactions_menu():
    print(format_menu("TRANSACTIONS"))

def view_all_budgets():
    print("viewing all budgets")

def view_selected_budget(id: int):
    print("viewing selected budget")

def add_new_budget(budg):
    print(f"adding new budget {budg}")

def modify_budget(id: int, budg):
    print(f"changing budget with id: {id} to {budg}")

def view_all_categories():
    print("showing all categories")

def view_selected_category(id: int):
    print(f"showing category with id: {id}")

def add_new_category(cat):
    print(f"adding new category: {cat}")

def modify_category(id: int, cat):
    print(f"changing category with id: {id} to {cat}")

def delete_category(id: int):
    print(f"deleting category with id: {id}")

def view_all_transactions():
    print(f"viewing all transactions")

def add_new_transaction(trans):
    print(f"adding new transaction: {trans}")

def modify_transaction(id: int, trans):
    print(f"changing transaction with id: {id} to {trans}")

def delete_transaction(id: int):
    print(f"deleting transaction with id: {id}")

MenuOptions = {
    'MAIN MENU': {
        'Budgets': [1, budgets_menu],
        'Categories': [2, categories_menu],
        'Transactions': [3, transactions_menu],
        },
    'Budgets': {
        'View All': [1, view_all_budgets],
        'View Selected': [2, view_selected_budget],
        'New': [3, add_new_budget],
        'Modify': [4, modify_budget],
        'Main Menu': [5, main_menu]
        },
    'Categories': {
        'View All': [1, view_all_categories],
        'View Selected': [2, view_selected_category],
        'New': [3, add_new_category],
        'Modify': [4, modify_category],
        'Delete': [5, delete_category],
        'Main Menu': [6, main_menu]
        },
    'Transactions': {
        'View': [1, view_all_transactions],
        'New': [2,  add_new_transaction],
        'Modify': [3, modify_transaction],
        'Delete': [4, delete_transaction],
        'Main Menu': [5, main_menu]
    }
}


class Menu:
    def __init__(self, title, options):
        self.title: str = title
        self.options: dict[str] = options

eq_spacer = "=========="


def format_menu(s):
    return f'{eq_spacer} {s} {eq_spacer}'

def get_user_selection(menu: Menu):
    #TODO: change this to use a menu object and pull options from it
    print(format_menu(menu.title.upper()))
    
    for i, opt in enumerate(menu.options):
        print(f"{i}. {opt}")
    
    sel = int(input("Make Selection: "))
    for val in menu.options.values():
        if val[0] == sel:
            return val[1]

# def get_sub_menu(selection):
#     if selection == '1':
#         return budgets_menu
#     elif selection == '2':
#         return categories_menu
#     elif selection == '3':
#         return transactions_menu
#     else:
#         s = ""
#         if selection ==  '4':
#             s = "Exiting"
#         else:
#             s = "Invalid option!"
#         return lambda: print(s)


    