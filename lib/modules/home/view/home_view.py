# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/ui/home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(1024, 640)
        HomeScreen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(HomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
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
        self.frame = QtWidgets.QFrame(self.dash_board)
        self.frame.setMinimumSize(QtCore.QSize(50, 50))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.reve_ct = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.reve_ct.setFont(font)
        self.reve_ct.setText("")
        self.reve_ct.setObjectName("reve_ct")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reve_ct)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.invoic_ct = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.invoic_ct.setFont(font)
        self.invoic_ct.setText("")
        self.invoic_ct.setObjectName("invoic_ct")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.invoic_ct)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.prod_ct = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.prod_ct.setFont(font)
        self.prod_ct.setText("")
        self.prod_ct.setObjectName("prod_ct")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prod_ct)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.revenue_chart = QtWidgets.QFrame(self.dash_board)
        self.revenue_chart.setMinimumSize(QtCore.QSize(50, 50))
        self.revenue_chart.setStyleSheet("background-color: rgb(165, 204, 255);")
        self.revenue_chart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.revenue_chart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.revenue_chart.setObjectName("revenue_chart")
        self.horizontalLayout.addWidget(self.revenue_chart)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(self.dash_board)
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
        self.menubar = QtWidgets.QMenuBar(HomeScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        HomeScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeScreen)
        self.statusbar.setObjectName("statusbar")
        HomeScreen.setStatusBar(self.statusbar)
        self.actionLogout = QtWidgets.QAction(HomeScreen)
        self.actionLogout.setObjectName("actionLogout")
        self.menuAccount.addAction(self.actionLogout)
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi(HomeScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "MainWindow"))
        self.label.setText(_translate("HomeScreen", "Doanh thu"))
        self.label_3.setText(_translate("HomeScreen", "Đơn hàng"))
        self.label_5.setText(_translate("HomeScreen", "Sản phẩm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dash_board), _translate("HomeScreen", "Dash Board"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.product), _translate("HomeScreen", "Sản phẩm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.invoice), _translate("HomeScreen", "Đơn hàng"))
        self.menuAccount.setTitle(_translate("HomeScreen", "Account"))
        self.actionLogout.setText(_translate("HomeScreen", "Logout"))
