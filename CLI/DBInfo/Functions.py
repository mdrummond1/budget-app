import json
from os.path import exists

def try_read_login_file(s: str):
    if exists(s):
        with open(s, 'r') as fp:
            content = fp.read(-1)
            d = json.loads(content)   
            return True, d     
    else:
        return False, None

def collect_login_info():
    conn = {}
    conn['dbname'] = input("Enter database name: ") 
    conn['host'] = input("Enter Host address: ")
    conn['user'] = input("Enter username: ")
    conn['pword'] = input("Enter password: ")
    return conn

def try_save_login_file(file, d: dict):
    try:
        encoded_string = json.dumps(d).encode('ascii')
        with open(file, "w") as fp:
            fp.write(encoded_string)
        return True
        
    except:
        print('failed to save login info')
        return False
