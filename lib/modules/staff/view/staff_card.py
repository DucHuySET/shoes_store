# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/ui/staff_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_staff_card(object):
    def setupUi(self, staff_card):
        staff_card.setObjectName("staff_card")
        staff_card.resize(400, 250)
        staff_card.setMinimumSize(QtCore.QSize(100, 150))
        staff_card.setMaximumSize(QtCore.QSize(400, 250))
        staff_card.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(staff_card)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(staff_card)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_row = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_row.setFont(font)
        self.name_row.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_row.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_row.setObjectName("name_row")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.name_row)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_label = QtWidgets.QLabel(self.name_row)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.name_content = QtWidgets.QLabel(self.name_row)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_content.sizePolicy().hasHeightForWidth())
        self.name_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setKerning(True)
        self.name_content.setFont(font)
        self.name_content.setText("")
        self.name_content.setObjectName("name_content")
        self.horizontalLayout.addWidget(self.name_content)
        self.verticalLayout_2.addWidget(self.name_row)
        self.addr = QtWidgets.QFrame(self.frame)
        self.addr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addr.setObjectName("addr")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.addr)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addr_label = QtWidgets.QLabel(self.addr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addr_label.sizePolicy().hasHeightForWidth())
        self.addr_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.addr_label.setFont(font)
        self.addr_label.setObjectName("addr_label")
        self.horizontalLayout_3.addWidget(self.addr_label)
        self.addr_content = QtWidgets.QLabel(self.addr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addr_content.sizePolicy().hasHeightForWidth())
        self.addr_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.addr_content.setFont(font)
        self.addr_content.setText("")
        self.addr_content.setObjectName("addr_content")
        self.horizontalLayout_3.addWidget(self.addr_content)
        self.verticalLayout_2.addWidget(self.addr)
        self.phone = QtWidgets.QFrame(self.frame)
        self.phone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phone.setObjectName("phone")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.phone)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.phone_label = QtWidgets.QLabel(self.phone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_label.sizePolicy().hasHeightForWidth())
        self.phone_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.horizontalLayout_2.addWidget(self.phone_label)
        self.phone_content = QtWidgets.QLabel(self.phone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_content.sizePolicy().hasHeightForWidth())
        self.phone_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.phone_content.setFont(font)
        self.phone_content.setText("")
        self.phone_content.setObjectName("phone_content")
        self.horizontalLayout_2.addWidget(self.phone_content)
        self.verticalLayout_2.addWidget(self.phone)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(205, 253, 255);\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(staff_card)
        QtCore.QMetaObject.connectSlotsByName(staff_card)

    def retranslateUi(self, staff_card):
        _translate = QtCore.QCoreApplication.translate
        staff_card.setWindowTitle(_translate("staff_card", "Form"))
        self.name_label.setText(_translate("staff_card", "Họ và tên:"))
        self.addr_label.setText(_translate("staff_card", "Địa chỉ:"))
        self.phone_label.setText(_translate("staff_card", "Số điện thoại:"))
        self.pushButton.setText(_translate("staff_card", "Chọn"))