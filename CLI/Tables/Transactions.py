from misc_functions import format_menu
from Database import *

class Transaction:
    def __init__(self, row) -> None:
        self.__transaction_id = row[0]
        self.__transaction_type_id = row[1]
        self.__transaction_amount = row[2]
        self.__category = row[3]
        self.__vendor_id = row[4]


def show_transactions_menu(db: Database):

    sel = 0

    while sel != 6:
        print(format_menu("TRANSACTIONS"))
        print('1. View All Transactions')
        print('2. View Selected Transaction')
        print('3. Add New Transaction')
        print('4. Modify Transaction')
        print('5. Delete Transaction')
        print('6. Main Menu')
    
        sel = int(input("Enter Selection: "))
        if sel == 1:
            view_all_transactions(db)
        elif sel == 2:
            view_selected_transaction(db)
        elif sel == 3:
            add_new_transaction(db)
        elif sel == 4:
            modify_transaction(db)
        elif sel == 5:
            delete_transaction(db)
        elif sel == 6:
            break
        else:
            print("Invalid Option")
        
        sel = 0

def view_all_transactions(db: Database):
    print(f"viewing all transactions")

def view_selected_transaction(db: Database):
    print(f"viewing selected transaction")

def add_new_transaction(db: Database):
    print(f"adding new transaction")

def modify_transaction(db: Database):
    print(f"changing transaction with id:")

def delete_transaction(db: Database):
    print(f"deleting transaction with id:")
