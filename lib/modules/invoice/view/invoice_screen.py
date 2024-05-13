
import sys
sys.path.append('.\lib\modules\invoice\model')
sys.path.append('.\lib\modules\invoice\controller')
sys.path.append('.\lib\\ui')

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QHBoxLayout, QFrame
from PyQt5 import QtCore

from invoice_controller import InvoiceController
from invoice_view import Ui_invoice
from product_card import Ui_product_card
from invoice_full import InvoiceFull
from invoice_card import Ui_invoice_card
from prod_line import Ui_prod_line
from invoice_model import InvoiceModel
from invoice_full import InvoiceFull
from invoice_detail_model import InvoiceDetailModel

import datetime

class InvoiceScreen (QWidget):
    def __init__(self):
        super().__init__()
        self.controller = InvoiceController()
        self.controller.signalSelectInvoice.connect(self.setInvoice)
        self.controller.signalAddProd.connect(self.viewListInvoiceDetail)

        self.ui = Ui_invoice()
        self.ui.setupUi(self)
        self.viewProduct()
        self.viewInvoice()
        self.setStaffList()
        self.ui.button_add.clicked.connect(self.gotoEditForm)
        self.ui.button_save.clicked.connect(self.save)
        self.ui.button_cancel.clicked.connect(self.cancel)
        self.ui.button_edit.clicked.connect(self.changeToEditMode)
        self.ui.button_delete.clicked.connect(self.delete)
    def setStaffList(self):
        if (len(self.controller.staffCtrl.listStaff) > 0):
            for i in range(len(self.controller.staffCtrl.listStaff)):
                self.ui.combo_staff.addItem(self.controller.staffCtrl.listStaff[i].staff_name)
    def viewInvoice(self):
        if (len(self.controller.listInvoices) > 0):
            for i in range(len(self.controller.listInvoices)):
                invoiceCard = InvoiceCard(self.controller.listInvoices[i].invoice_model, self.controller)
                self.ui.gridLayout.addWidget(invoiceCard, i, 0, 1, 1)
    def viewProduct(self):
        row = 0
        if (len(self.controller.listProduct) > 0):
            for i in range(len(self.controller.listProduct)):
                staffCard = ProductCard(self.controller.listProduct[i], self.controller)
                self.ui.gridLayout_2.addWidget(staffCard, i, 0, 1, 1)
    def gotoDetail(self):
        if (self.ui.stackedWidget.currentIndex() == 1):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()-1)
    def gotoEditForm(self):
        if (self.ui.stackedWidget.currentIndex() == 0):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()+1)
        self.clearInput()
        self.ui.checkBox.setChecked(False)
    def addProd(self, invoiceDetail):
        prodLine = ProdLine(invoiceDetail, self.controller)
        self.ui.list_prod_edit.addWidget(prodLine)
    def viewListInvoiceDetail(self):
        self.clearLayout(self.ui.list_prod_edit)
        if (len(self.controller.listInvoiceDetail) > 0):
            for i in range(len(self.controller.listInvoiceDetail)):
                invoiceCard = ProdLine(self.controller.listInvoiceDetail[i], self.controller)
                self.ui.list_prod_edit.addWidget(invoiceCard)
            total = 0
            for ele in self.controller.listInvoiceDetail:
                product = None
                for e in self.controller.productCtrl.listProducts:
                    if (e.product_id == ele.product_id):
                        product = e
                total += product.product_price * ele.quantity
            self.ui.total_field.setText(str(total))
        
    def clearLayout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    def cancel(self):
        self.clearInput()
    def clearInput(self):
        self.ui.combo_staff.setCurrentIndex(0)
        self.ui.combo_pay.setCurrentIndex(0)
        self.controller.listInvoiceDetail.clear()
        self.ui.total_field.clear()
        self.viewListInvoiceDetail()
    def save(self):
        now = datetime.datetime.now()
        staffIndex = self.ui.combo_staff.currentIndex()
        invoice_id_new = str(len(self.controller.listInvoices)+1)
        invoiceModel = InvoiceModel(invoice_id=self.controller.invoiceId,
                                     customer_id= "0",
                                    staff_id=self.controller.staffCtrl.listStaff[staffIndex].staff_id,
                                    payments=self.ui.combo_pay.currentText(), 
                                    total=self.ui.total_field.text(),
                                    date_= now.strftime("%Y-%m-%d %H:%M:%S"))
        invoiceFull = InvoiceFull(invoice_model=invoiceModel, list_invoice_detail=self.controller.listInvoiceDetail)
        if (self.mode == 0):
            invoiceModel.invoice_id = invoice_id_new
            result = self.controller.createInvoice(invoiceFull)
            if (result):
                self.clearInput()

    def changeToEditMode(self):
        self.ui.checkBox.setChecked(True)
    def setInvoice(self):
        # self.ui.name_field.set
        indexStaff = 0
        for i in range(len(self.controller.staffCtrl.listStaff)):
            if (self.controller.staffCtrl.listStaff[i].staff_id == self.controller.selectedInvoice.staff_id):
                indexStaff = i
                break
        self.ui.combo_staff.setCurrentIndex(indexStaff)

    def delete(self):
        self.controller.deleteInvoice(self.controller.selectedInvoice.invoice_id)
    


class ProductCard(QWidget):
    def __init__(self, data, controller):
        self.data = data
        self.controller = controller
        super().__init__()
        self.ui = Ui_product_card()
        self.ui.setupUi(self)
        self.ui.name_content.setText(self.data.product_name)
        self.ui.price_content.setText(str(self.data.product_price))
        self.ui.descript_content.setText(self.data.product_description)
        self.ui.pushButton.clicked.connect(self.selectProduct)
    
    def selectProduct(self):
        self.controller.addProduct(self.data)
class InvoiceCard(QWidget):
    def __init__(self, data, controller):
        self.data = data
        self.controller = controller
        super().__init__()
        self.ui = Ui_invoice_card()
        self.ui.setupUi(self)
        self.ui.cus_ct.setText(self.data.customer_id)
        staffName = self.controller.repository.getStaffbyId(self.data.staff_id)
        self.ui.staff_ct.setText(staffName[0])
        self.ui.total_ct.setText(str(self.data.total))
        self.ui.payment_ct.setText(self.data.payments)
        self.ui.time_ct.setText(str(self.data.date_))
        self.ui.pushButton.clicked.connect(self.selectInvoice)
    
    def selectInvoice(self):
        self.controller.setInvoice(self.data)
class ProdLine(QWidget):
    def __init__(self, invoiceDetail, controller) -> None:
        self.data = invoiceDetail
        self.controller = controller
        self.product = None
        super().__init__()
        self.ui = Ui_prod_line()
        self.ui.setupUi(self)
        for e in self.controller.productCtrl.listProducts:
            if (e.product_id == self.data.product_id):
                self.product = e
        # prodName = self.controller.productCtrl.repository.getNameById(self.data.product_id)
        self.ui.prod_name.setText(self.product.product_name)
        self.ui.prod_quant.setValue(self.data.quantity)
        
        price = self.product.product_price
        self.ui.result.setText(str(int(self.data.quantity) * int(price))) 