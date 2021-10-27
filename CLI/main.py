import Constants as c
from Tables import *
import Database as db
import json
import base64
from os.path import exists
from Menus import *


env = "/etc/.budgeting/dblogin"

def try_read_login_file(s, d):
    if exists(s):
        with open(s, 'r') as fp:        
            decoded_string = base64.b64decode(fp.read(-1))
            d = json.loads(decoded_string)   
            return True     
    else:
        return False

def collect_login_info():
    conn = {}
    conn['dbname'] = input("Enter database name: ") 
    conn['host'] = input("Enter Host address: ")
    conn['user'] = input("Enter username: ")
    conn['pword'] = input("Enter password: ")
    return conn

def try_save_login_file(file, dict):
    try:
        encoded_string = json.dumps(dict).encode('ascii')
        encoded_string = base64.b64encode(encoded_string)
        with open(file, "w") as fp:
            fp.write(encoded_string)
        return True
        
    except:
        print('failed to save login info')
        return False


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

    #menus = [Menu(title, opt) for title, opt in MenuOptions.items()]
    # selected_function = None
    # selected_menu = Menu('MAIN MENU', MenuOptions['MAIN MENU'])

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
        
