import psycopg2
from Tables import Budget
from Tables import Category
from Tables import Transaction

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

    def __execute_query__(self, s, *args):
        self.connect()
        self.__cur.execute(s, args)

    def __select_query__(self, s, *args) -> list:
        try:
            self.__execute_query__(s, args)
            rows = self.__cur.fetchall()
            return rows

        except Exception as e:
            print(e)
    
    def __change_query__(self, s, *args) -> None:
        try:
            self.__execute_query__(s, args)
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            print(e)

    def __conn_string(self) -> str:
        return f"dbname={self.__name} host={self.__host} user={self.__user} password={self.__pword}"

    def GetBudgets(self) -> list:
        return [Budget(row) for row in self.__select_query__('SELECT * FROM budgets')]

    def AddBudget(self, budget: Budget) -> None:
        self.__change_query__('INSERT INTO budgets(budget_start_date) VALUES(%(budget_start_date)s)', budget.__dict)

    def GetCategories(self) -> list:
        return [Category(row) for row in self.__select_query__('SELECT * FROM categories')]

    def AddCategory(self, cat: Category) -> None:
        self.__change_query__('INSERT INTO categories(category_type, category_name, budgeted_amount) VALUES((%(category_type)s, %(category_name)s, %(budgeted_amount)s)', cat.__dict__)

    def GetTransactions(self) -> list:
        return [Transaction(row) for row in self.__select_query__('SELECT * FROM transactions')]

    def AddTransaction(self, trans: Transaction) -> None:
        self.__change_query__('INSERT INTO transactions(amount, category_id, date_purchased, memo, transaction_type) VALUES(%(amount)s, %(category_id)s, %(date_purchased)s, %(memo)s, %(transaction_type)s)')
