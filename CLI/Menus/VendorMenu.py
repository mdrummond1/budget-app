from Database import Database
from MenuFunctions import format_menu, force_user_number_selection
from .VendorCategoryMenu import show_vendor_category_menu


def show_vendor_menu(db: Database):
    sel = 0

    while sel != 6:
        print(format_menu("VENDORS"))
        print('1. View All Vendors')
        print('2. View Selected Vendor')
        print('3. Add New Vendor')
        print('4. Remove Vendor')
        print('5. Vendor Category Menu')
        print('6. Main Menu')

        sel = force_user_number_selection()

        if sel == 1:
            view_all_vendors(db)
        elif sel == 2:
            view_selected_vendor(db)
        elif sel == 3:
            add_new_vendor(db)
        elif sel == 4:
            remove_vendor(db)
        elif sel == 5:
            show_vendor_category_menu(db)
        elif sel == 6:
            break


def view_all_vendors(db: Database):
    print("showing vendor types")

def view_selected_vendor(db: Database):
    print("showing selected vendor")

def view_all_vendor_types(db: Database):
    print("showing all vendor types")

def add_new_vendor(db: Database) -> Vendor:
    vendor_name: str = input("Enter vendor name: ")
    vendor_web_address:str = input("Enter vendor web address (Enter for none): ")
    selected_type: VendorType = None

    types: list['VendorType'] = db.GetVendorTypes()

    if len(types) <= 0:
        print("no vendor types found. Need to add one.")
        add_new_vendor_type(db)
    else:
        selected_type = select_obj_from_list(types, 'vendor types')

    if selected_type is None:
        print("no vendor category selected.")
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

def remove_vendor(db: Database):
