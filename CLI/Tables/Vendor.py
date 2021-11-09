import Database

class Vendor:
    def __init__(self, row: list):
        self.vendor_id = row[0]
        self.vendor_type = row[1]
        self.name = row[2]
        self.web_address = row[3]

    def __str__(self) -> str:
        return f"id: {self.vendor_id} vendor_type: {self.vendor_type} name: {self.name} web address: {self.web_address}"
