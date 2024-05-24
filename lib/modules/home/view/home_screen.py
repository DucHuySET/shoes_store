
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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class HomeScreen(QMainWindow):
    def __init__(self, isAdmin, stackScr) -> None:
        super().__init__()
        self.stackScr = stackScr
        self.isAdmin = isAdmin
        self.appController = AppController()
        self.ui = view()
        self.ui.setupUi(self)
        self.controller = controller()
        self.product_view = ProductScreen()
        self.ui.product_horizontalLayout.addWidget(self.product_view)
        self.invoiceView = InvoiceScreen()
        self.ui.horizontalLayout_2.addWidget(self.invoiceView)
        self.ui.actionLogout.triggered.connect(self.logout)
        self.appController.signalRefreshStat.connect(self.showDataFromAppCtrl)

        if (isAdmin):
            _translate = QtCore.QCoreApplication.translate
            self.staff_tab = StaffScreen()
            self.ui.tabWidget.addTab(self.staff_tab, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.staff_tab), _translate("HomeScreen", "Nhân viên"))
        self.ui.tabWidget.setCurrentIndex(0)
        self.showData()
    def showData(self):
        self.appController.fetchData()
        self.setUpChart()
        self.plotData()
        self.setStatistic()
    def showDataFromAppCtrl(self, result):
        print(result)
        self.appController.fetchData()
        self.setUpChart()
        self.plotData()
        self.setStatistic()
    def setStatistic(self):
        self.ui.reve_ct.setText(str(self.appController.total_reve))
        self.ui.invoic_ct.setText(str(self.appController.total_invoice))
        self.ui.prod_ct.setText(str(self.appController.total_prod))
    def setUpChart(self):
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.ui.revenue_chart.setLayout(layout)
    def plotData(self):
        self.canvas.axes.plot(self.appController.list_month, self.appController.revenue_by_month)
        self.canvas.axes.xaxis.set_major_locator(self.appController.fixed_locator)
        self.canvas.draw()
    def logout(self):
        self.stackScr.setCurrentIndex(self.stackScr.currentIndex()-1)
        appController = AppController()
        appController.user = None
        self.stackScr.removeWidget(self)

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel("Tháng")
        self.axes.set_ylabel("Doanh thu")
        super(MplCanvas, self).__init__(fig)
        