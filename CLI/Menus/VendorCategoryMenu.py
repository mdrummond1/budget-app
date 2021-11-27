from os import execlp
from Database import Database
from Tables.VendorType import VendorType
from MenuFunctions import force_user_number_selection, format_menu, try_user_number_selection

def show_vendor_category_menu(db: Database):
    print(format_menu("VENDOR CATEGORIES"))

    sel: int = 0
    
    while sel != 5:
        print("1. Show All Vendor Categories")
        print("2. Show Selected Vendor Category")
        print("3. Add New Vendor Category")
        print("4. Delete Vendor Category")
        print("5. Vendors Menu")

        sel = force_user_number_selection()

        if sel == 1:
            view_all_vendor_categories(db) 
        elif sel == 2:
            view_selected_vendor_category(db)
        elif sel == 3:
            add_new_vendor_category(db)
        elif sel == 4:
            delete_vendor_type(db)
        elif sel == 5:
            break
        else:
           print("invalid option")


def view_all_vendor_categories(db: Database):
    vendor_types: list = db.GetVendorTypes()
    for t in vendor_types:
        print(t)

def view_selected_vendor_category(db: Database) -> VendorType:
    view_all_vendor_categories(db)
    selected_id = try_user_number_selection("Enter id of vendor category")
    if selected_id == -1:
        return 

    selected_vendor_type = db.GetVendorTypeById(selected_id)
    if selected_vendor_type is None:
        print("No vendor type founds with that id")
        return

    print(selected_vendor_type)
    return selected_vendor_type
    
def add_new_vendor_category(db: Database):
    vend_cat = input("Enter Vendor Category: ")
    
    try:
        db.AddVendorType(vend_cat)
        print("Vendor Category successfully added!")
    except Exception as e:
        print("Adding vendor category failed")
        print(e)

def delete_vendor_type(db: Database):
    selected_vendor_category: VendorType = view_selected_vendor_category(db)
    if selected_vendor_category is None:
        print("no vendor category with that id")
        print("Cancelling...")
        return
    
    try:
        db.DeleteVendorCategory(selected_vendor_category.vendor_type_id)
        print("Delete successful!")
    except Exception as e:
        print("delete failed")
        print(e)