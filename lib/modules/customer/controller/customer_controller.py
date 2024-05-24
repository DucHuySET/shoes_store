
import sys
sys.path.append('.\\lib\modules\customer\model')
sys.path.append('.\\lib\modules\customer\\repository')

from customer_repository import CustomerRepository
from customer_model import CustomerModel

from PyQt5.QtCore import QObject, pyqtSignal

class CustomerController(QObject):
    signalSelectCustomer = pyqtSignal(object) 
    def __init__(self) -> None:
        super().__init__()
        self.selectedCustomer = None
        self.repository = CustomerRepository()
        self.fetchlistCustomer()
    
    def fetchlistCustomer(self):
        self.listCustomer = self.repository.get_all_customers()
        
    def setCustomer(self, customer):
        if self.selectedCustomer != customer:
            self.selectedCustomer = customer
            self.signalSelectCustomer.emit(self.selectedCustomer)
    
    def createCustomer(self, customer):
        try:
            self.repository.create_customer(customer)
            return True
        except:
            return False
    
    def updateCustomer(self, customer):
        try:
            self.repository.update_customer(customer)
            return True
        except:
            return False
    
    def deleteCustomer(self, customer_id):
        try:
            self.repository.delete_customer_by_id(customer_id)
            return True
        except:
            return False
