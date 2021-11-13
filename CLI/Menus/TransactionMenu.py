from Database import Database
from Tables import Transaction, VendorType, Vendor
from .MainMenu import format_menu
from MenuFunctions import print_obj_list, select_obj_from_list, get_datetime
from Menus.CategoryMenu import view_selected_category

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
        #elif sel == 4:
        #    modify_transaction(db)
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
#        vendor_name = input("Enter vendor name: ")
#        vendor_web_address = input("Enter vendor web address (Enter for none): ")
    pass

def add_new_vendor_type(db: Database) -> VendorType:
    type_name = input("enter vendor category: ")
    db.AddVendorType(type_name)

def add_new_transaction(db: Database):
    #vendor_type -> vendor -> transaction
    selected_type: VendorType.VendorType = None
    selected_vendor: Vendor.Vendor = None

    #vendor_type
    types = db.GetVendorTypes()
    if len(types) <= 0:
        print("need to add a vendor category first")
        add_new_vendor_type(db)
        selected_type = db.GetVendorTypes()[0]
    else:
        selected_type = select_obj_from_list(types, 'vendor category')

    #vendor
    vendors = db.GetVendors()
    if len(vendors) <= 0:
        print("need to add a vendor first")
        add_new_vendor(db)
        selected_vendor = db.GetVendors()[0]
    else:
        selected_vendor = select_obj_from_list(vendors, "vendors") 
    
    #transaction
    amt = input("Enter transaction amount: ")

    purchase_date = None 
    while purchase_date is None:
        purchase_date = get_datetime() 

    selected_category = view_selected_category(db)

    memo = input("Enter memo (Press Enter for empty): ")
    trans_info = [0, selected_type.vendor_type_id, selected_category.category_id, selected_vendor.vendor_id, amt, purchase_date, memo]

    try:
        db.AddTransaction(Transaction(trans_info))
    except Exception as e:
        print("Error adding transaction")
        print(e)

#def modify_transaction(db: Database):
#    print(f"changing transaction with id:")

def delete_transaction(db: Database):
    print(f"deleting transaction with id:")