# Form implementation generated from reading ui file 'd:\CTARG_Project\Python\may_1\lib\ui\prod_line.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_prod_line(object):
    def setupUi(self, prod_line):
        prod_line.setObjectName("prod_line")
        prod_line.resize(400, 64)
        prod_line.setMinimumSize(QtCore.QSize(20, 25))
        self.horizontalLayout = QtWidgets.QHBoxLayout(prod_line)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prod_name = QtWidgets.QLabel(parent=prod_line)
        self.prod_name.setText("")
        self.prod_name.setWordWrap(True)
        self.prod_name.setObjectName("prod_name")
        self.horizontalLayout.addWidget(self.prod_name)
        self.prod_quant = QtWidgets.QSpinBox(parent=prod_line)
        self.prod_quant.setProperty("value", 1)
        self.prod_quant.setObjectName("prod_quant")
        self.horizontalLayout.addWidget(self.prod_quant)
        self.result = QtWidgets.QLabel(parent=prod_line)
        self.result.setMinimumSize(QtCore.QSize(20, 25))
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.result.setObjectName("result")
        self.horizontalLayout.addWidget(self.result)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(prod_line)
        QtCore.QMetaObject.connectSlotsByName(prod_line)

    def retranslateUi(self, prod_line):
        _translate = QtCore.QCoreApplication.translate
        prod_line.setWindowTitle(_translate("prod_line", "Form"))