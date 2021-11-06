import base64
import json
from os.path import exists

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
