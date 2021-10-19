import psycopg2

class Database:
    def __init__(self, name, host, user, pword):
        self.__name = name
        self.__host = host
        self.__user = user
        self.__pword = pword
        self.__connection = None
        self.__cur = None
        self.connected = False

    def connect(self):
        if self.__connection is None:
            try:
                self.__connection = psycopg2.connect(self.__conn_string())
                self.__cur = self.__connection.cursor()
                print("Successfully connected")
                self.connected = True
            except:
                print("Connection failed")

    
    def close(self):
        if self.__connection is not None:
            self.__cur.close()
            self.__cur = None
            self.__connection.close()
            self.__connection = None
            self.connected = False


    def SelectQuery(self, s, *args):
        self.connect()
        self.__cur.execute(s, args)
        rows = self.__cur.fetchall()
        return rows
    
    def ChangeQuery(self, s, *args):
        self.connect()
        self.__cur.execute(s, args)
        self.__connection.commit()

    def __conn_string(self):
        return f"dbname={self.__name} host={self.__host} user={self.__user} password={self.__pword}"

