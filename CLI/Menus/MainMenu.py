from MenuFunctions import format_menu


class Menu:
    def __init__(self, title, options):
        self.title: str = title
        self.options: dict = options

def show_main_menu():
    print(format_menu("MAIN MENU"))
    print('1. Budgets')
    print('2. Categories')
    print('3. Transactions')
    print('4. Exit')

    return int(input("Enter Selection: "))




# MenuOptions = {
#     'MAIN MENU': {
#         'Budgets': [1, budgets_menu],
#         'Categories': [2, categories_menu],
#         'Transactions': [3, transactions_menu],
#         'Exit': [4, lambda: print("Exiting")]
#         },

#     'Budgets': {
#         'View All': [1, view_all_budgets],
#         'View Selected': [2, view_selected_budget],
#         'New': [3, add_new_budget],
#         'Modify': [4, modify_budget],
#         'Main Menu': [5, show_main_menu]
#         },

#     'Categories': {
#         'View All': [1, view_all_categories],
#         'View Selected': [2, view_selected_category],
#         'New': [3, add_new_category],

#         'Modify': [4, modify_category],
#         'Delete': [5, delete_category],
#         'Main Menu': [6, main_menu]
#         },

#     'Transactions': {
#         'View': [1, view_all_transactions],
#         'New': [2,  add_new_transaction],
#         'Modify': [3, modify_transaction],
#         'Delete': [4, delete_transaction],
#         'Main Menu': [5, main_menu]
#     }
# }

# def get_user_selection(menu: Menu):
#     print(format_menu(menu.title.upper()))
    
#     for i, opt in enumerate(menu.options, start=1):
#         print(f"{i}. {opt}")
    
#     sel = int(input("Make Selection: "))
#     func = None

#     for m, vals in menu.options.items():
#         if vals[0] == sel:
#             func = vals[1]
#             menu = Menu(m, MenuOptions[m])
    
#     if menu is None:
#         menu = Menu('MAIN MENU', MenuOptions['MAIN MENU'])

#     if func is None:
#         func = lambda: print("invalid selection")

#     return func  
