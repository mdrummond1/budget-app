eq_spacer = "=========="

def format_menu(s):
    return f'{eq_spacer} {s} {eq_spacer}'

def print_obj_list(l: list):
    for i, el in enumerate(l, start=1):
        print(f"{i}. {el[0]}")