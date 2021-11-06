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
    print('4. Reports')
    print('5. Exit')

    return int(input("Enter Selection: "))