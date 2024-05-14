
import sys
sys.path.append('.\\lib\modules\product\model')
sys.path.append('.\\lib\modules\product\\repository')

from product_repository import ProductRepository
from product_model import ProductModel

from PyQt5.QtCore import QObject, pyqtSignal

class ProductController(QObject):
    signalSelectProduct = pyqtSignal(object) 
    def __init__(self) -> None:
        super().__init__()
        self.selectedProduct = None
        self.repository = ProductRepository()
        self.fetchListProducts()
    
    def fetchListProducts(self):
        self.listProducts = self.repository.getAllProducts()
        
    def setProduct(self, product):
        if self.selectedProduct != product:
            self.selectedProduct = product
            self.signalSelectProduct.emit(self.selectedProduct)
    
    def createProduct(self, product):
        try:
            self.repository.createProduct(product)
            return True
        except:
            return False
    
    def updateProduct(self, product):
        try:
            self.repository.updateProduct(product)
            return True
        except:
            return False
    
    def deleteProduct(self, product_id):
        try:
            self.repository.deleteById(product_id)
            return True
        except:
            return False
