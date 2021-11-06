from datetime import datetime
import psycopg2
from Constants import Category_Types
from Tables import Budget, Category, Transaction

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
            self.__execute_query__(s, *args)
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            print(e)

    def __conn_string(self) -> str:
        return f"dbname={self.__name} host={self.__host} user={self.__user} password={self.__pword}"

    def GetBudgets(self) -> list:
        return [Budget(row) for row in self.__select_query__('SELECT * FROM budgets')]

    def GetCategoriesFromBudgetId(self, budget_id: int):
        return [Category(row) for row in self.__select_query__('SELECT * FROM categories c WHERE c.budget_id = (%s)', budget_id)]

    #def GetTransactionsFromBudgetId(self, budget_id: int):
    #    return [Transaction(row) for row in self.__select_query__('SELECT * FROM transactions t')]
   
    def AddBudget(self, start_date: datetime) -> None:
        self.__change_query__('INSERT INTO budgets(budget_start_date) VALUES(%s)', start_date)

    def GetCategoryTypes(self) -> list:
        return [t for t in self.__select_query__('SELECT category_type FROM category_types')]
    
    def GetCategories(self) -> list:
        return [Category(row) for row in self.__select_query__('SELECT * FROM categories')]

    def AddCategory(self, budget_id, cat_type: int, cat_name: str, budgeted_amount: str) -> None:
        self.__change_query__('INSERT INTO categories(budget_id, category_type, category_name, budgeted_amount) VALUES(%s, %s, %s, %s)', budget_id, cat_type, cat_name, budgeted_amount)
    
    def UpdateCategory(self, cat: Category):
        self.__change_query__('UPDATE categories SET category_type = %(category_type)s, category_name = %(category_name)s, budgeted_amount = %(budgeted_amount)s WHERE category_id = %(category_id)s', cat.__dict__)
    
    def GetTransactionsFromCategoryId(self, category_id: int):
        return [Transaction(row) for row in self.__select_query__('SELECT * FROM transactions t WHERE t.category_id = (%s)', category_id)]

    def GetTransactions(self) -> list:
        return [Transaction(row) for row in self.__select_query__('SELECT * FROM transactions')]

    def AddTransaction(self, trans: Transaction) -> None:
        self.__change_query__('INSERT INTO transactions(amount, budget_id, category_id, date_purchased, memo, transaction_type) VALUES(%(amount)s, %(category_id)s, %(date_purchased)s, %(memo)s, %(transaction_type)s)', trans.__dict__)
