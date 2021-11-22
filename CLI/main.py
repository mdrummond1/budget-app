import Constants as c
import Database as db
from Menus import *
from DBInfo import try_read_login_file, collect_login_info, try_save_login_file
from MenuFunctions import force_user_number_selection
from os import name

if name == 'nt':
    env = "D:/Programming/projects/budget-app/CLI/DBInfo/config.json"
else:
    env = "./DBInfo/config.json"

def main():
    file_found, c.Connection = try_read_login_file(env)
    if file_found:
        print("login file found")
        print(f"logging in as user \'{c.Connection['user']}\'")
    else:
        print("no login info found. \nPlease enter")
        c.Connection = collect_login_info()
        try_save_login_file(env, c.Connection)
    d = db.Database(*c.Connection.values())
    d.connect()
    if d.connected:

        sel = 0
        while sel != 5:
            sel = show_main_menu()
            if sel == 1:
                show_budgets_menu(d)
            elif sel == 2:
                show_categories_menu(d)
            elif sel == 3:
                show_transactions_menu(d)
            elif sel == 4:
                show_reports_menu(d)
            elif sel == 5:
                break
            else:
                print("Invalid option!")
        
if __name__ == "__main__":
    main()