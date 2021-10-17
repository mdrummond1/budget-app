Connection = {
   'dbname': 'budgeting',
   'host': '192.168.1.107',
   'user': 'app',
   'pword': 'pass123'
}

TableNames = {
    'Budgets': 'budgets',
    'Categories': 'categories',
    'Category_Types': 'category_types',
    'Transaction_Types': 'transaction_types',
    'Transactions': 'transactions',
    'Vendor_Types': 'vendor_types',
    'Vendors': 'vendors'
}

Transaction_Types = {
    'Credit': ['CREDIT', 1],
    'Debit': ['DEBIT', 2]
}

Category_Types = {
    'Income': ['INCOME', 1],
    'Fixed_Expense': ['FIXED_EXPENSE', 2],
    'Variable_Expense': ['VARIABLE_EXPENSE', 3]
}

Vendor_Types = []# to be filled later

Queries = {
    'Select': 'SELECT',
    'Update': 'UPDATE',
    'Insert': 'INSERT',
    'Delete': 'DELETE',
}



