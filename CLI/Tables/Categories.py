from misc_functions import format_menu

class Category:
    def __init__(self, row) -> None:
        self.__category = row[0]
        self.__category_type_id = row[1]
        self.__category_name = row[2]



def show_categories_menu():
    print(format_menu("CATEGORIES"))
    print('1. View All Categories')
    print('2. View Selected Categorie')
    print('3. Add New Category')
    print('4. Modify Category')
    print('5. Delete Category')
    print('6. Main Menu')

    sel = 0
    while sel != 6:
        sel = int(input("Enter Selection:"))
            
        if sel == 1:
            view_all_categories()
        elif sel == 2:
            view_selected_category()
        elif sel == 3:
            add_new_category()
        elif sel == 4:
            modify_category()
        elif sel == 5:
            delete_category()
        elif sel == 6:
            break
        else:
            print("Invalid Option!")

        sel = 0 

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
