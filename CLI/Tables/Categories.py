from misc_functions import format_menu

class Category:
    def __init__(self, row) -> None:
        self.__category = row[0]
        self.__category_type_id = row[1]
        self.__category_name = row[2]



def show_categories_menu():
    print(format_menu("CATEGORIES"))

def view_all_categories():
    print("showing all categories")

def view_selected_category():
    print(f"showing category with id: ")

def add_new_category():
    print(f"adding new category:")

def modify_category():
    print(f"changing category with id")

def delete_category():
    print(f"deleting category with id")
