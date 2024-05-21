
import sys
sys.path.append('.\\lib\modules\product\model')
sys.path.append('.\\lib\modules\product\controller')
sys.path.append('.\\lib\\ui')
sys.path.append(".\\lib\core")
from app_controller import AppController

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QHBoxLayout, QFrame
from PyQt5 import QtCore

from product_controller import ProductController


from product_view import Ui_product_tab
from product_card import Ui_product_card
from product_model import ProductModel

class ProductScreen (QWidget):
    def __init__(self):
        super().__init__()
        self.mode = 0
        self.controller = ProductController()
        self.controller.signalSelectProduct.connect(self.showDetail)
        self.appController = AppController()

        self.ui = Ui_product_tab()
        self.ui.setupUi(self)
        self.viewProduct()
        self.ui.button_add.clicked.connect(self.goToAdd)
        self.ui.button_save.clicked.connect(self.save)
        self.ui.button_cancel.clicked.connect(self.cancel)
        self.ui.button_edit.clicked.connect(self.gotoEditCurrentItem)
        self.ui.button_delete.clicked.connect(self.delete)


    def viewProduct(self):
        self.clearLayout(self.ui.gridLayout)
        row = 0
        if (len(self.controller.listProducts) > 0):
            for i in range(len(self.controller.listProducts)):
                staffCard = ProductCard(self.controller.listProducts[i], self.controller)
                if (i % 3 == 0):                 
                    self.ui.gridLayout.addWidget(staffCard, row, 0, 1, 1)
                elif (i % 3 == 1):                 
                    self.ui.gridLayout.addWidget(staffCard, row, 1, 1, 1)
                else:
                    self.ui.gridLayout.addWidget(staffCard, row, 2, 1, 1)
                    row += 1
    def clearLayout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    def gotoDetail(self):
        if (self.ui.stackedWidget.currentIndex() == 1):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()-1)
    def goToAdd(self):
        self.gotoEditForm()
        self.mode = 0
    def gotoEditForm(self):
        if (self.ui.stackedWidget.currentIndex() == 0):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()+1)
    def showDetail(self,product):
        self.gotoDetail()
        self.ui.name_ct.setText(product.product_name)
        self.ui.price_ct.setText(str(product.product_price))
        self.ui.des_ct.setText(product.product_description)
    def gotoEditCurrentItem(self):
        self.mode = 1
        self.prepareEdit()
        self.gotoEditForm()
    def prepareEdit(self):
        if (self.controller.selectedProduct != None):
            self.setInput(self.controller.selectedProduct)
    def setInput(self, product):
        self.ui.name_field.setText(product.product_name)
        self.ui.price_field.setText(str(product.product_price))
        self.ui.des_field.setText(product.product_description)
    def refresh(self):
        self.clearLayout(self.ui.gridLayout)
        self.controller.fetchListProducts()
        self.viewProduct()
        self.appController.refreshHomeStat()
    def save(self):
        result = False
        if (self.mode == 0):
            prod_id = self.createNewProdId()
            product = ProductModel(product_id=prod_id,
                                   product_name=self.ui.name_field.text(),
                                   product_price=self.ui.price_field.text(),
                                   product_description=self.ui.des_field.text())
            result = self.controller.createProduct(product)
        elif (self.mode == 1):
            product = ProductModel(product_id=self.controller.selectedProduct.product_id,
                                   product_name=self.ui.name_field.text(),
                                   product_price=self.ui.price_field.text(),
                                   product_description=self.ui.des_field.text())
            result = self.controller.updateProduct(product)
        if (result):
            self.clearInput()
            self.refresh()
    def clearInput(self):
        self.ui.name_field.clear()
        self.ui.price_field.clear()
        self.ui.des_field.clear()
    def cancel(self):
        self.clearInput()
        if (self.mode == 1):
            self.gotoDetail()
    def delete(self):
        self.dialog = CustomDialog(self)
        if self.dialog.exec():
            self.controller.deleteProduct(self.controller.selectedProduct.product_id)
            self.refresh()
            self.goToAdd()
    def createNewProdId(self):
        id = 0
        for e in self.controller.listProducts:
            if e.product_id >= id:
                id = e.product_id + 1
        return id

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
        self.controller.setProduct(self.data)

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