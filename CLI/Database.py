from datetime import datetime
import psycopg2
from Constants import Category_Types
from Tables.Vendor import Vendor
from Tables.Budgets import Budget
from Tables.Categories import Category
from Tables.Transactions import Transaction
from Tables.VendorType import VendorType

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
            except Exception as e:
                print("Connection failed")
                print(e)

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
        self.__change_query__('INSERT INTO transactions(amount, category_id, date_purchased, memo, transaction_type) VALUES(%s, %s, %s, %s, %s)', trans.amount, trans.category_id, trans.date_purchased, trans.memo, trans.transaction_type)
    
    def GetVendors(self) -> list:
        return [Vendor(row) for row in self.__select_query__('SELECT * FROM vendors')]

    def GetVendorFromId(self, vend_id) -> Vendor:
        rows = self.__select_query__('SELECT * FROM vendors WHERE vendor_id = %s', vend_id)
        if len(rows) > 0:
            return Vendor(rows[0])

    def AddVendor(self, vendor: Vendor) -> None:
        self.__change_query__('INSERT INTO vendors(vendor_type, name, web_address) VALUES(%(vendor_type)s, %(name)s, %(web_address)s)', vendor.vendor_type, vendor.name, vendor.web_address)

    def UpdateVendorName(self, id: int, new_name: str) -> None:
        self.__change_query__('UPDATE vendors SET name = %s WHERE vendor_id = ', new_name, id)

    def UpdateVendorType(self, vendor_id: int, vendor_cat_id: int) -> None:
        self.__change_query__('UPDATE vendors SET vendor_type = %s WHERE vendor_id = %s', vendor_cat_id, vendor_id)
    
    def GetVendorTypes(self) -> list:
        return [VendorType(row) for row in self.__select_query__('SELECT * FROM vendor_types')]

    def GetVendorTypeByTypeName(self, type_name) -> VendorType:
        rows = self.__select_query__('SELECT * FROM vendor_types WHERE vendor_type_id = %s', type_name)
        if len(rows) > 0:
            return VendorType(rows[0])

    def AddVendorType(self, type_name: str):
        self.__change_query__('INSERT INTO vendor_types(vendor_type) VALUES(%s)', type_name)

    def DeleteVendorCategory(self, id: int):
        self.__change_query__('DELETE FROM vendor_types WHERE vendor_type_id = %s', id)