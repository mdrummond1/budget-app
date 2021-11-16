from datetime import datetime
from Database import Database
from Tables.Transactions import Transaction
from Tables.VendorType import VendorType
from Tables.Vendor import Vendor
from Tables.Categories import Category
from .MainMenu import format_menu
from MenuFunctions import force_user_number_selection, select_obj_from_list, get_datetime, try_user_number_selection
from .CategoryMenu import view_selected_category
from .VendorMenu import show_vendor_menu

def show_transactions_menu(db: Database):

    sel = 0

    while sel != 6:
        print(format_menu("TRANSACTIONS"))
        print('1. View All Transactions')
        print('2. View Selected Transaction')
        print('3. Add New Transaction')
        print('4. Delete Transaction')
        print('5. Vendor Menu')
        print('6. Main Menu')

        sel = force_user_number_selection()
        
        if sel == 1:
            view_all_transactions(db)
        elif sel == 2:
            view_selected_transaction(db)
        elif sel == 3:
            add_new_transaction(db)
        elif sel == 4:
            delete_transaction(db)
        elif sel == 5:
            show_vendor_menu(db)
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
    selected_transaction = force_user_number_selection("Select ID of transaction: ")

    transaction = db.GetTransactionFromId(selected_transaction)
    if transaction is None:
        print("ID not found. Cancelling...")
        return

    print(transaction)

    return selected_transaction

def add_new_vendor_type(db: Database) -> VendorType:
    type_name = input("enter vendor category: ")
    try:
        db.AddVendorType(type_name)
        print("vendor category added successfully!")
    except Exception as e:
        print("add vendor category failed")
        print(e)
    

def add_new_transaction(db: Database):
    #vendor_type -> vendor -> transaction
    selected_type: int = None
    selected_vendor: int = None

    #vendor_type
    types = db.GetVendorTypes()
    if len(types) <= 0:
        print("need to add a vendor category first")
        add_new_vendor_type(db)
        selected_type = db.GetVendorTypes()[0]
    else:
        selected_type: VendorType = None
        while selected_type is None or selected_type == -1:
            selected_type = select_obj_from_list(types, 'vendor category')
            print("invalid entry")

    #vendor
    vendors = db.GetVendors()
    if len(vendors) <= 0:
        print("need to add a vendor first")
        add_new_vendor(db)
        selected_vendor = db.GetVendors()[0]
    else:
        selected_vendor: Vendor = None
        while selected_vendor is None or selected_vendor == -1:
            selected_vendor = select_obj_from_list(vendors, "vendors") 
    
    #transaction
    amt: str = input("Enter transaction amount: ")

    purchase_date: datetime = None 
    while purchase_date is None:
        purchase_date = get_datetime() 

    selected_category: Category = view_selected_category(db)

    memo = input("Enter memo (Press Enter for empty): ")
    trans_info = [0, selected_type.vendor_type_id, selected_category.category_id, selected_vendor.vendor_id, amt, purchase_date, memo]

    try:
        db.AddTransaction(Transaction(trans_info))
    except Exception as e:
        print("Error adding transaction")
        print(e)

def delete_transaction(db: Database):
    print(f"deleting transaction with id:")