class InvoiceModel:
    def __init__(self, invoice_id, customer_id, staff_id, payments, date_, total):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.staff_id = staff_id
        self.payments = payments
        self.date_ = date_
        self.total = total

    @staticmethod
    def from_row(row):
        return InvoiceModel(row[0], row[1], row[2], row[3], row[4], row[5])
