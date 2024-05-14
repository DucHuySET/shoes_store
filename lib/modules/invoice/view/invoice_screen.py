
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
from prod_line_detail import Ui_prod_line_detail

import datetime

class InvoiceScreen (QWidget):
    def __init__(self):
        super().__init__()
        self.controller = InvoiceController()
        self.controller.signalSelectInvoice.connect(self.setInvoiceDetailView)
        self.controller.signalAddProd.connect(self.viewListInvoiceDetailEdit)

        self.ui = Ui_invoice()
        self.ui.setupUi(self)
        self.viewProduct()
        self.viewInvoice()
        self.setStaffList()
        self.ui.button_add.clicked.connect(self.gotoCreateForm)
        self.ui.button_save.clicked.connect(self.save)
        self.ui.button_cancel.clicked.connect(self.cancel)
        self.ui.button_edit.clicked.connect(self.changeToEditMode)
        self.ui.button_delete.clicked.connect(self.delete)
        self.ui.button_refresh.clicked.connect(self.refresh)
    def setStaffList(self):
        if (len(self.controller.staffCtrl.listStaff) > 0):
            for i in range(len(self.controller.staffCtrl.listStaff)):
                self.ui.combo_staff.addItem(self.controller.staffCtrl.listStaff[i].staff_name)
    def viewInvoice(self):
        if (len(self.controller.listInvoiceFull) > 0):
            for i in range(len(self.controller.listInvoiceFull)):
                invoiceCard = InvoiceCard(self.controller.listInvoiceFull[i].invoice_model, self.controller)
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
    def gotoCreateForm(self):
        self.gotoEditForm()
        self.controller.isEditMode = False
        self.clearInput()
        self.ui.checkBox.setChecked(False)
    def gotoEditForm(self):
        if (self.ui.stackedWidget.currentIndex() == 0):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()+1)
        
    def addProd(self, invoiceDetail):
        prodLine = ProdLine(invoiceDetail, self.controller)
        self.ui.list_prod_edit.addWidget(prodLine)
    def viewListInvoiceDetailEdit(self):
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
        self.gotoDetail()
    def clearInput(self):
        self.ui.combo_staff.setCurrentIndex(0)
        self.ui.combo_pay.setCurrentIndex(0)
        self.controller.listInvoiceDetail.clear()
        self.ui.total_field.clear()
        self.viewListInvoiceDetailEdit()
    def save(self):
        now = datetime.datetime.now()
        staffIndex = self.ui.combo_staff.currentIndex()
        invoice_id_new = self.createNewInvoiceId()
        invoiceModel = InvoiceModel(invoice_id=self.controller.invoice_id,
                                     customer_id= "0",
                                    staff_id=self.controller.staffCtrl.listStaff[staffIndex].staff_id,
                                    payments=self.ui.combo_pay.currentText(), 
                                    total=int(self.ui.total_field.text()),
                                    date_= now.strftime("%Y-%m-%d %H:%M:%S"))
        invoiceFull = InvoiceFull(invoice_model=invoiceModel, list_invoice_detail=self.controller.listInvoiceDetail)
        result = False
        if (self.controller.isEditMode):
            invoiceFull.invoice_model.invoice_id = self.controller.selectedInvoice.invoice_id
            for i in range(len(invoiceFull.list_detail)):
                invoiceFull.list_detail[i].invoice_id = invoiceFull.invoice_model.invoice_id
            result = self.controller.updateInvoice(invoiceFull)
        else:
            invoiceFull.invoice_model.invoice_id = invoice_id_new
            for i in range(len(invoiceFull.list_detail)):
                invoiceFull.list_detail[i].invoice_id = invoiceFull.invoice_model.invoice_id
            result = self.controller.createInvoice(invoiceFull)
        if (result):
            self.clearInput()
            self.refresh()
    def createNewInvoiceId(self):
        id = 0
        for e in self.controller.listInvoiceFull:
            if e.invoice_model.invoice_id >= id:
                id = e.invoice_model.invoice_id + 1
        return id

    def changeToEditMode(self):
        if (self.controller.selectedInvoice != None):
            self.ui.checkBox.setChecked(True)
            self.controller.isEditMode = True
            self.setInvoiceDetailEdit()
            self.gotoEditForm()
    def setInvoiceDetailEdit(self):
        # self.ui.name_field.set
        indexStaff = 0
        for i in range(len(self.controller.staffCtrl.listStaff)):
            if (self.controller.staffCtrl.listStaff[i].staff_id == self.controller.selectedInvoice.staff_id):
                indexStaff = i
                break
        self.ui.combo_staff.setCurrentIndex(indexStaff)
        self.ui.combo_pay.setCurrentText(self.controller.selectedInvoice.payments)
        self.controller.fetchListInvoiceDetail()
        self.viewListInvoiceDetailEdit()
    def setInvoiceDetailView(self):
        self.gotoDetail()
        self.clearLayout(self.ui.detailPage_listProd)
        invoice_model = self.controller.selectedInvoice
        self.ui.cus_ct.setText(invoice_model.customer_id)
        staff_name = ""
        for e in self.controller.staffCtrl.listStaff:
            if e.staff_id == invoice_model.staff_id:
                staff_name = e.staff_name
        self.ui.staff_ct.setText(staff_name)
        self.ui.pay_ct.setText(invoice_model.payments)
        self.ui.total_ct.setText(str(invoice_model.total))
        self.controller.fetchListInvoiceDetail()
        for e in self.controller.listInvoiceDetail:
            prod_line_detail = ProdLineDetail(e, self.controller)
            self.ui.detailPage_listProd.addWidget(prod_line_detail)

    def delete(self):
        self.dialog = CustomDialog(self)
        if self.dialog.exec():
            if (self.controller.selectedInvoice != None):
                result = self.controller.deleteInvoice(self.controller.selectedInvoice.invoice_id)
                if (result):
                    self.refresh()
                    self.gotoCreateForm()
    def refresh(self):
        self.controller.productCtrl.repository.reconnect()
        self.controller.fetchListInvoices()
        self.controller.fetchListProduct()
        self.viewInvoice()
        self.viewProduct()
    


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
        self.ui.prod_quant.valueChanged.connect(self.handleChangeSpin)
        
        price = self.product.product_price
        self.ui.result.setText(str(int(self.data.quantity) * int(price))) 
    def handleChangeSpin(self):
        self.data.quantity = self.ui.prod_quant.value()
        self.controller.handleChangeSpinBox(self.data.invoice_id, self.data.product_id, self.data.quantity)
class ProdLineDetail(QWidget):
    def __init__(self, invoiceDetail, controller) -> None:
        self.data = invoiceDetail
        self.product = None
        self.controller = controller
        super().__init__()
        self.ui = Ui_prod_line_detail()
        self.ui.setupUi(self)
        for e in self.controller.productCtrl.listProducts:
            if (e.product_id == self.data.product_id):
                self.product = e
        self.ui.prod_name.setText(self.product.product_name)
        self.ui.prod_quant.setText(str(self.data.quantity))
        
        price = self.product.product_price
        self.ui.result.setText(str(int(self.data.quantity) * int(price))) 

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Dialog")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Bạn có chắc chắn muốn xóa ?")
        message.setMinimumSize(QtCore.QSize(150, 80))
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)