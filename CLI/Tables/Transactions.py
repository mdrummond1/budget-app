from misc_functions import format_menu

class Transaction:
    def __init__(self, row) -> None:
        self.__transaction_id = row[0]
        self.__transaction_type_id = row[1]
        self.__transaction_amount = row[2]
        self.__category = row[3]
        self.__vendor_id = row[4]


def show_transactions_menu():
    print(format_menu("TRANSACTIONS"))

def view_all_transactions():
    print(f"viewing all transactions")

def add_new_transaction():
    print(f"adding new transaction")

def modify_transaction():
    print(f"changing transaction with id:")

def delete_transaction():
    print(f"deleting transaction with id:")
