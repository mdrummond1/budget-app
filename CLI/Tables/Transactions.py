

class Transaction:
    def __init__(self, row) -> None:
        self.amount = row[0]
        self.category_id = row[1]
        self.date_purchased = row[2]
        self.memo = row[3]
        self.transaction_id = row[4]
        self.transaction_type = row[5]
        self.vendor_id = row[6]

