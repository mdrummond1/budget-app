

class Category:
    def __init__(self, row) -> None:
        self.category_id = row[0]
        self.category_type = row[1]
        self.budget_id = row[2]
        self.category_name = row[3]
        self.budgeted_amount = row[4]
        self.actual_total = row[5]
        self.amount_difference = row[6]

    def __str__(self) -> str:
        return f"id: {self.category_id} type: {self.category_type} budget_id: {self.budget_id} name: {self.category_name} budgeted amount: {self.budgeted_amount} actual total: {self.actual_total} amount difference: {self.amount_difference}"