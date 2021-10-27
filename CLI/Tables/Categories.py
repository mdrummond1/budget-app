

class Category:
    def __init__(self, row) -> None:
        self.category_id = row[0]
        self.category_type = row[1]
        self.category_name = row[2]
        self.budgeted_amount = row[3]
        self.actual_total = row[4]
        self.amount_difference = row[5]


