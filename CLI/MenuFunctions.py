from datetime import datetime

eq_spacer = "=========="

def format_menu(s):
    return f'{eq_spacer} {s} {eq_spacer}'

def print_obj_list(l: list):
    for i, el in enumerate(l, start=1):
        print(f"{i}. {el}")

def select_obj_from_list(l: list, obj_type) -> object:
    print_obj_list(l)
    sel = force_user_number_selection(f"Select {obj_type} from list:")

    try:
        if sel < (len(l) + 1):
            return l[sel-1]
        else:
            return -1
    except:
        print("invalid entry. Cancelling...")

def get_datetime() -> datetime:
    year = force_user_number_selection("Enter year (yyyy): ")
    month = force_user_number_selection("Enter month (mm):")
    day = force_user_number_selection("Enter day (dd): ")

    try:
        return datetime(year, month, day)
    except ValueError:
        print("date out of bounds")
        return None

def try_user_number_selection(label: str = 'Enter Selection: ') -> int:
    sel = input(label)
    try:
        sel = int(sel)
        return sel
    except:
        print("invalid entry! Must be a number")
        return -1

def force_user_number_selection(label: str = 'Enter Selection: ') -> int:
    sel = -1
    while sel == -1:
        sel = try_user_number_selection(label)

    return sel