import Constants as c
from Tables import *
import Database as db
from Menus import *
from DBInfo import try_read_login_file, collect_login_info, try_save_login_file

env = "/etc/.budgeting/dblogin"
def main():
    if try_read_login_file(env, c.Connection):
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
        while sel != 4:
            sel = show_main_menu()
            if sel == 1:
                show_budgets_menu(d)
            elif sel == 2:
                show_categories_menu(d)
            elif sel == 3:
                show_transactions_menu(d)
            elif sel == 4:
                break
            else:
                print("Invalid option!")
        
if __name__ == "__main__":
    main()