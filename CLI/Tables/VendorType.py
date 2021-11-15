class VendorType:
    def __init__(self, row: list):
        self.vendor_type_id = row[0]
        self.vendor_type = row[1]

    def __str__(self):
        return f"id: {self.vendor_type_id} vendor category: {self.vendor_type}"
