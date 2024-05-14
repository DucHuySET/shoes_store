
import sys
sys.path.append('.\\lib\modules\home\controller')
sys.path.append('.\\lib\modules\home\\view')
sys.path.append('.\\lib\modules\staff\\view')
sys.path.append('.\\lib\modules\product\\view')
sys.path.append('.\\lib\modules\invoice\\view')
sys.path.append('.\\lib\\ui')
sys.path.append(".\\lib\core")

from home_view import Ui_HomeScreen as view
from home_controller import HomeController as controller
from staff_screen import StaffScreen
from product_screen import ProductScreen
from app_controller import AppController
from invoice_screen import InvoiceScreen


from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from PyQt5 import QtCore


class HomeScreen(QMainWindow):
    def __init__(self, isAdmin, stackScr) -> None:
        self.stackScr = stackScr
        self.isAdmin = isAdmin
        super().__init__()
        self.ui = view()
        self.ui.setupUi(self)
        self.controller = controller()
        self.product_view = ProductScreen()
        self.ui.product_horizontalLayout.addWidget(self.product_view)
        self.invoiceView = InvoiceScreen()
        self.ui.horizontalLayout_2.addWidget(self.invoiceView)
        self.ui.actionLogout.triggered.connect(self.logout)

        if (isAdmin):
            _translate = QtCore.QCoreApplication.translate
            self.staff_tab = StaffScreen()
            self.ui.tabWidget.addTab(self.staff_tab, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.staff_tab), _translate("HomeScreen", "Nhân viên"))
    def logout(self):
        self.stackScr.setCurrentIndex(self.stackScr.currentIndex()-1)
        appController = AppController()
        appController.user = None
        self.stackScr.removeWidget(self)

        