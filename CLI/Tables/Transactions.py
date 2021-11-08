

class Transaction:
    def __init__(self, row) -> None:
        self.transaction_id = row[0]
        self.transaction_type = row[1]
        self.category_id = row[2]
        self.vendor_id = row[3]
        self.amount = row[4]
        self.date_purchased = row[5]
        self.memo = row[6]

    def __str__(self) -> str:
        return f"id: {self.transaction_id} amount: {self.amount} category id: {self.category_id} date purchased: {self.date_purchased} type: {self.transaction_type} vendor: {self.vendor_id} memo: {self.memo}"