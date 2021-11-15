from datetime import datetime

eq_spacer = "=========="

def format_menu(s):
    return f'{eq_spacer} {s} {eq_spacer}'

def print_obj_list(l: list):
    for i, el in enumerate(l, start=1):
        print(f"{i}. {el}")

def select_obj_from_list(l: list, obj_type):
    print_obj_list(l)
    sel = input(f"Select {obj_type} from list:")
    try:
        sel = int(sel)
        if sel < (len(l) + 1):
            return l[sel-1]
        else:
            return -1
    except:
        print("invalid entry. Cancelling...")

def get_datetime() -> datetime:
    year = input("Enter year: ")
    month = input("Enter month:")
    day = input("Enter day: ")
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        print("invalid entry")
        return None

    try:
        return datetime(year, month, day)
    except ValueError:
        print("date out of bounds")
        return None