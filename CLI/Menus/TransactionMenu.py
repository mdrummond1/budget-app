from Database import Database
from Tables import Transaction, VendorType, Vendor
from .MainMenu import format_menu
from MenuFunctions import print_obj_list

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
    transactions = db.GetTransactions()
    for trans in transactions:
        print(trans)

def view_selected_transaction(db: Database):
    view_all_transactions(db)
    sel = int(input("Select ID of transaction: "))

    transaction = db.GetTransactionFromId(sel)
    if transaction is None:
        print("ID not found. Cancelling...")
        return
    print(transaction)

def add_new_vendor(db: Database) -> Vendor:
    pass

def add_new_vendor_type(db: Database) -> VendorType:
    pass

def add_new_transaction(db: Database):
    vendors = db.getvendors()
    selected_type = None

    if len(vendors) <= 0:
        print("need to add a vendor first")
        types = db.GetVendorTypes()
        
        if len(types) <= 0:
            print("need to add a vendor category first")
            type_name = input("enter vendor category: ")
            db.AddVendorType(type_name)
            selected_type = db.GetVendorTypeByTypeName(type_name)
        else:
            print_obj_list(types)
            selected_type = types[input("Enter number of selected type: ")]
        
        vendor_name = input("Enter vendor name: ")
        vendor_web_address = input("Enter vendor web address (Enter for none): ")
        

    else:
        print_obj_list(vendors)
        selected_vendor = vendors[input("Enter number of selected vendor: ")]
        


def modify_transaction(db: Database):
    print(f"changing transaction with id:")

def delete_transaction(db: Database):
    print(f"deleting transaction with id:")