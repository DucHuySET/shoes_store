class InvoiceDetailModel:
    def __init__(self, product_id, invoice_id, quantity):
        self.product_id = product_id
        self.invoice_id = invoice_id
        self.quantity = quantity

    @staticmethod
    def from_row(row):
        return InvoiceDetailModel(row[0], row[1], row[2])
