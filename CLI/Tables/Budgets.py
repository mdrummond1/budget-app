
class Budget:
    def __init__(self, row):
        self.budget_id = row[0]
        self.budget_start_date = row[1]
        self.budget_end_date = row[2]
        self.total_income = row[3]
        self.total_liability = row[4]
        self.net_amount = row[5]

    def __str__(self) -> str:
        return f"id: {self.budget_id} start date: {self.budget_start_date} end date: {self.budget_end_date} income: {self.total_income} liability: {self.total_liability} net: {self.net_amount}"
