class ProductModel:
    def __init__(self, product_id, product_name, product_description, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price

    @staticmethod
    def from_row(row):
        return ProductModel(row[0], row[1], row[2], row[3])
