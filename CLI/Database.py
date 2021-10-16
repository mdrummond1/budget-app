import psycopg2

class Database:
    def __init__(self, name, host, user, pword):
        self.__name = name
        self.__host = host
        self.__user = user
        self.__pword = pword
        self.__connection = None
        self.__cur = None

    def connect(self):
        if self.__connection is None:
            self.__connection = psycopg2.connect(self.__conn_string())
            self.__cur = self.__connection.cursor()
    
    def close(self):
        if self.__connection is not None:
            self.__cur.close()
            self.__cur = None
            self.__connection.close()
            self.__connection = None


    def SelectQuery(self, s):
        self.connect()
        cur.execute(s)
        rows = cur.fetchall()
        return rows
    
    def ChangeQuery(self, s, obj):
        self.connect()
        cur.execute(s, obj)
        conn.commit()

    def __conn_string(self):
        return f"dbname={self.__name} host={self.__host} user={self.__user} password={self.__pword}"

    
 
 
user} password={self.__pword}"

    
 
 
