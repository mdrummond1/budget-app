import psycopg2 as pg
import Constants as c
import Table as t
import Database as db
import json
import base64
from os.path import exists
from Menu import *


env = "/etc/.budgeting/dblogin"


def try_read_login_file(s, d):
    if exists(s):
        with open(s, 'rb') as fp:        
            decoded_string = base64.b64decode(fp.read(-1))
            d = json.loads(decoded_string)   
            return True     
    else:
        return False

def collect_login_info():
    conn = {}
    conn['dbname'] = input("Enter database name:")
    conn['host'] = input("Enter Host address:")
    conn['user'] = input("Enter username:")
    conn['pword'] = input("Enter password:")
    return conn

def try_save_login_file(file, dict):
    try:
        encoded_string = json.dumps(dict).encode('ascii')
        encoded_string = base64.b64encode(encoded_string)
        with open(file, "wb") as fp:
            fp.write(encoded_string)
        return True
        
    except:
        print('failed to save login info')
        return False

d = {'Budgets': [1, lambda x1, x2: x1 + x2]}




if try_read_login_file(env, c.Connection):
    print("login file found")
    print(f"logging in as user \'{c.Connection['user']}\'")
else:
    print("no login info found. \nPlease enter")
    c.Connection = collect_login_info()
    try_save_login_file(env, c.Connection)
    
d = db.Database(*c.Connection.values())
d.connect()
submenu = '0'

while submenu != '4':
    submenu = get_user_selection()
    menu_function = Menu.get_sub_menu(submenu)
    menu_function()