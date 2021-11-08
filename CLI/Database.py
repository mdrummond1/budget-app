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
        self.__execute_query__(s, args)
        rows = self.__cur.fetchall()
        return rows
    
    def __change_query__(self, s, *args) -> None:
        try:
            self.__execute_query__(s, *args)
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise

    def __conn_string(self) -> str:
        return f"dbname={self.__name} host={self.__host} user={self.__user} password={self.__pword}"

    def GetBudgets(self) -> list:
        return [Budget(row) for row in self.__select_query__('SELECT * FROM budgets')]

    def GetCategoriesFromBudgetId(self, budget_id: int):
        rows = self.__select_query__('SELECT * FROM categories c WHERE c.budget_id = (%s)', budget_id)
        if len(rows) > 0:
            return Budget(rows[0]) 

    def AddBudget(self, start_date: datetime) -> None:
        self.__change_query__('INSERT INTO budgets(budget_start_date) VALUES(%s)', start_date)

    def GetCategoryTypes(self) -> list:
        return [t for t in self.__select_query__('SELECT category_type FROM category_types')]
    
    def GetCategories(self) -> list:
        return [Category(row) for row in self.__select_query__('SELECT * FROM categories')]
    
    def GetCategoryFromId(self, cat_id) -> Category:
        rows = self.__select_query__('SELECT * FROM categories WHERE category_id = %s', cat_id) 
        if len(rows) > 0:
            return Category(rows[0])

    def AddCategory(self, budget_id, cat_type: int, cat_name: str, budgeted_amount: str) -> None:
        self.__change_query__('INSERT INTO categories(budget_id, category_type, category_name, budgeted_amount) VALUES(%s, %s, %s, %s)', budget_id, cat_type, cat_name, budgeted_amount)
    
    def ModifyCategoryAmount(self, cat_id, new_amount):
        self.__change_query__('UPDATE categories SET budgeted_amount = %s WHERE category_id = %s', new_amount, cat_id)

    def ModifyCategoryName(self, cat_id, new_name):
        self.__change_query__('UPDATE categories SET category_name = %s WHERE category_id = %s', new_name, cat_id)

    def DeleteCategory(self, cat_id) -> None:
        self.__change_query__('DELETE FROM categories WHERE category_id = %s', cat_id)

    def GetTransactionsFromCategoryId(self, category_id: int) -> list:
        return [Transaction(row) for row in self.__select_query__('SELECT * FROM transactions t WHERE t.category_id = (%s)', category_id)]

    def GetTransactions(self) -> list:
        return [Transaction(row) for row in self.__select_query__('SELECT * FROM transactions')]
    
    def GetTransactionFromId(self, trans_id: int):
        rows = self.__select_query__('SELECT * FROM transactions WHERE transaction_id = %s', trans_id)
        if len(rows) > 0:
            return Transaction(rows[0])

    def AddTransaction(self, trans: Transaction) -> None:
        self.__change_query__('INSERT INTO transactions(amount, budget_id, category_id, date_purchased, memo, transaction_type) VALUES(%(amount)s, %(category_id)s, %(date_purchased)s, %(memo)s, %(transaction_type)s)', trans.__dict__)
