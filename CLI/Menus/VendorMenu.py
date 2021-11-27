from Database import Database
from MenuFunctions import format_menu, force_user_number_selection, select_obj_from_list
from .VendorCategoryMenu import show_vendor_category_menu, add_new_vendor_category, view_selected_vendor_category
from Tables.VendorType import VendorType
from Tables.Vendor import Vendor

def show_vendor_menu(db: Database):
    sel = 0

    while sel != 6:
        print(format_menu("VENDORS"))
        print('1. View All Vendors')
        print('2. View Selected Vendor')
        print('3. Add New Vendor')
        print('4. Vendor Category Menu')
        print('5. Change Vendor Name')
        print('6. Change Vendor Category')
        print('7. Change Vendor Web Address')
        print('8. Main Menu')

        sel = force_user_number_selection()

        if sel == 1:
            view_all_vendors(db)
        elif sel == 2:
            view_selected_vendor(db)
        elif sel == 3:
            add_new_vendor(db)
        elif sel == 4:
            show_vendor_category_menu(db)
        elif sel == 5:
            update_vendor_name(db)
        elif sel == 6:
            update_vendor_type(db)
        elif sel == 7:
            update_vendor_web_address(db)
        elif sel == 8:
            break


def view_all_vendors(db: Database):
    vendors = db.GetVendors()
    for vendor in vendors:
        print(vendor)

def view_selected_vendor(db: Database):
    view_all_vendors(db)

    selected_vendor_id = force_user_number_selection("Select Vendor: ")
    vendor = db.GetVendorFromId(selected_vendor_id)
    if vendor is None:
        print("No vendor found")
        return

    print(vendor)
    return vendor

def add_new_vendor(db: Database) -> Vendor:
    vendor_name: str = input("Enter vendor name: ")
    vendor_web_address: str = input("Enter vendor web address (Enter for none): ")
    selected_type: VendorType = view_selected_vendor_category(db)

    if selected_type is None:
        print("no vendor category selected or none available.")
        print("Cancelling...")
        return

    vendor_info = [0, selected_type.vendor_type_id, vendor_name, vendor_web_address]
    vendor = Vendor(vendor_info)

    try:
        db.AddVendor(vendor)
        print("vendor added successfully")
    except Exception as e:
        print("add vendor failed.")
        print(e)

def update_vendor_name(db: Database):
    vendor = view_selected_vendor(db)
    new_name = input("Enter new vendor name: ")

    try:
        db.update_vendor_name(new_name)
    except Exception as e:
        print("failed to update vendor name!")
        print(e)

def update_vendor_type(db: Database):
    selected_vendor: Vendor = view_selected_vendor(db)
    selected_category: VendorType = view_selected_vendor_category(db)
    if selected_category is None:
        print("no vendor category selected or none available.")
        print("Cancelling...")
        return

    try:
        db.UpdateVendorType(selected_vendor.vendor_id, selected_category.id) 
        print("vendor update successful!")
    except Exception as e:
        print("updating vendor type failed")
        print(e)

def update_vendor_web_address(db: Database):
    selected_vendor: Vendor = view_selected_vendor(db)
    if selected_vendor is None:
        print("no vendor selected or nont available.")
        print("Cancelling...")
        return
    
    new_web_address: str = input("Enter new web address: ")

    try:
        db.UpdateVendorWebAddress(selected_vendor.vendor_id, new_web_address)
        print("vendor update successful!")
    except Exception as e:
        print("updating vendor web address failed")
        print(e)