# Form implementation generated from reading ui file 'd:\CTARG_Project\Python\may_1\lib\ui\home.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(1024, 640)
        HomeScreen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=HomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.dash_board = QtWidgets.QWidget()
        self.dash_board.setObjectName("dash_board")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dash_board)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.dash_board)
        self.frame.setMinimumSize(QtCore.QSize(50, 50))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.dash_board)
        self.frame_2.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_2.setStyleSheet("background-color: rgb(165, 204, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(parent=self.dash_board)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.dash_board, "")
        self.product = QtWidgets.QWidget()
        self.product.setObjectName("product")
        self.product_horizontalLayout = QtWidgets.QHBoxLayout(self.product)
        self.product_horizontalLayout.setObjectName("product_horizontalLayout")
        self.tabWidget.addTab(self.product, "")
        self.invoice = QtWidgets.QWidget()
        self.invoice.setObjectName("invoice")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.invoice)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget.addTab(self.invoice, "")
        self.verticalLayout.addWidget(self.tabWidget)
        HomeScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=HomeScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(parent=self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        HomeScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=HomeScreen)
        self.statusbar.setObjectName("statusbar")
        HomeScreen.setStatusBar(self.statusbar)
        self.actionLogout = QtGui.QAction(parent=HomeScreen)
        self.actionLogout.setObjectName("actionLogout")
        self.menuAccount.addAction(self.actionLogout)
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi(HomeScreen)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dash_board), _translate("HomeScreen", "Dash Board"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.product), _translate("HomeScreen", "Sản phẩm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.invoice), _translate("HomeScreen", "Đơn hàng"))
        self.menuAccount.setTitle(_translate("HomeScreen", "Account"))
        self.actionLogout.setText(_translate("HomeScreen", "Logout"))