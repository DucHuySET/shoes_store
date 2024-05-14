
import sys
sys.path.append('.\\lib\modules\invoice\\repository')
sys.path.append('.\\lib\modules\invoice\\model')
sys.path.append('.\\lib\modules\product\controller')
sys.path.append('.\\lib\modules\staff\controller')

from invoice_repository import InvoiceRepository
from invoice_model import InvoiceModel
from product_controller import ProductController
from staff_controller import StaffController
from invoice_detail_model import InvoiceDetailModel

from PyQt5.QtCore import QObject, pyqtSignal

class InvoiceController(QObject):
    signalSelectInvoice = pyqtSignal(object)
    signalAddProd = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.selectedInvoice = None
        self.listInvoiceDetail = []
        self.isEditMode = False
        
        self.repository = InvoiceRepository()
        self.productCtrl = ProductController()
        self.staffCtrl = StaffController()
        self.fetchListInvoices()
        self.fetchListProduct()
        self.invoice_id = len(self.listInvoiceFull) + 1

    def fetchListInvoices(self):
        self.listInvoiceFull = self.repository.getAllInvoices()
    def fetchListProduct(self):
        self.listProduct = self.productCtrl.repository.getAllProducts()
    def fetchListInvoiceDetail(self):
        self.listInvoiceDetail = self.repository.getInvoiceDetail(self.selectedInvoice.invoice_id)

    def setInvoice(self, invoice):
        if self.selectedInvoice != invoice:
            self.selectedInvoice = invoice
            self.signalSelectInvoice.emit(self.selectedInvoice)
    def addProduct(self, prod):
        check = False
        for e in self.listInvoiceDetail:
            if e.product_id == prod.product_id:
                check = True
                break
        if (check):
            for i in range(len(self.listInvoiceDetail)):
                if self.listInvoiceDetail[i].product_id == prod.product_id:
                    self.listInvoiceDetail[i].quantity += 1
                    break
        else:
            if (self.isEditMode):
                invoiceDetail = InvoiceDetailModel(product_id=prod.product_id, invoice_id=self.selectedInvoice.invoice_id, quantity=1)
                self.listInvoiceDetail.append(invoiceDetail)
            else:
                invoiceDetail = InvoiceDetailModel(product_id=prod.product_id, invoice_id=self.invoice_id, quantity=1)
                self.listInvoiceDetail.append(invoiceDetail)
            
        self.signalAddProd.emit()
        

    def createInvoice(self, invoiceFull):
        try:
            self.repository.createInvoice(invoiceFull.invoice_model)
            for e in invoiceFull.list_detail:
                self.repository.createInvoiceDetail(e)
            return True
        except:
            return False

    def updateInvoice(self, invoiceFull):
        try:
            self.repository.updateInvoice(invoiceFull.invoice_model)
            self.repository.deleteInvoiceDetailById(invoiceFull.invoice_model.invoice_id)
            for e in invoiceFull.list_detail:
                self.repository.createInvoiceDetail(e)
            return True
        except:
            return False

    def deleteInvoice(self, invoice_id):
        try:
            self.repository.deleteInvoiceById(invoice_id)
            self.repository.deleteInvoiceDetailById(invoice_id)
            return True
        except:
            return False
    def handleChangeSpinBox(self, invoice_id, product_id, quantity):
        for i in range(len(self.listInvoiceDetail)):
            if (self.listInvoiceDetail[i].invoice_id == invoice_id and self.listInvoiceDetail[i].product_id == product_id):
                self.listInvoiceDetail[i].quantity = quantity
        self.signalAddProd.emit()
