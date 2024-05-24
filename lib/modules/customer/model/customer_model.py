class CustomerModel:

    def __init__(self, customer_id, customer_name, customer_phone, customer_email, customer_address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_email = customer_email
        self.customer_address = customer_address

    @staticmethod
    def from_row(row):
        return CustomerModel(row[0], row[1], row[2], row[3], row[4])
