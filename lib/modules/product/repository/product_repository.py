import sys
sys.path.append('.\\lib\modules\product\model')
sys.path.append('.\\lib\core')
from database_config import DatabaseConfig
from product_model import ProductModel
import mysql.connector as connector

class ProductRepository:
    def __init__(self):
        self.db = connector.connect(
            host=DatabaseConfig().host,
            port=DatabaseConfig().port,
            user=DatabaseConfig().user,
            password=DatabaseConfig().password,
            database=DatabaseConfig().database
        )
        self.cursor = self.db.cursor()

    def getAllProducts(self):
        selectQuery = "SELECT * FROM PRODUCT"
        self.cursor.execute(selectQuery)
        listData = self.cursor.fetchall()
        listProducts = []
        for e in listData:
            product = ProductModel.from_row(e)
            listProducts.append(product)
        return listProducts

    def updateProduct(self, product):
        query = "UPDATE PRODUCT SET ProductName = %s, ProductDescription = %s, ProductPrice = %s WHERE ProductId = %s"
        values = (product.product_name, product.product_description, product.product_price, product.product_id)
        self.cursor.execute(query, values)
        self.db.commit()

    def createProduct(self, product):
        query = "INSERT INTO PRODUCT (ProductId, ProductName, ProductDescription, ProductPrice) VALUES (%s, %s, %s, %s)"
        values = (product.product_id, product.product_name, product.product_description, product.product_price)
        self.cursor.execute(query, values)
        self.db.commit()

    def deleteById(self, product_id):
        query = "DELETE FROM PRODUCT WHERE ProductId = %s"
        self.cursor.execute(query, (product_id,))
        self.db.commit()
    def getNameById(self, product_id):
        query = "SELECT ProductName FROM product where ProductId = %s;"
        self.cursor.execute(query, (product_id,))
        nameList = self.cursor.fetchone()
        return nameList[0]
    def reconnect(self):
        self.db.reconnect()
