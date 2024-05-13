# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/ui/invoice.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_invoice(object):
    def setupUi(self, invoice):
        invoice.setObjectName("invoice")
        invoice.resize(1008, 547)
        self.horizontalLayout = QtWidgets.QHBoxLayout(invoice)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_product = QtWidgets.QFrame(invoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_product.sizePolicy().hasHeightForWidth())
        self.list_product.setSizePolicy(sizePolicy)
        self.list_product.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(218, 221, 225);")
        self.list_product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_product.setObjectName("list_product")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.list_product)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_staff_label = QtWidgets.QLabel(self.list_product)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.list_staff_label.sizePolicy().hasHeightForWidth())
        self.list_staff_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_staff_label.setFont(font)
        self.list_staff_label.setObjectName("list_staff_label")
        self.verticalLayout_3.addWidget(self.list_staff_label)
        self.line = QtWidgets.QFrame(self.list_product)
        font = QtGui.QFont()
        font.setPointSize(4)
        self.line.setFont(font)
        self.line.setStyleSheet("border-color: rgb(103, 103, 103);\n"
"background-color: rgb(79, 79, 79);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(self.list_product)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 320, 463))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.list_product)
        self.edit_view = QtWidgets.QFrame(invoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_view.sizePolicy().hasHeightForWidth())
        self.edit_view.setSizePolicy(sizePolicy)
        self.edit_view.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(218, 221, 225);")
        self.edit_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_view.setObjectName("edit_view")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.edit_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.edit_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_add = QtWidgets.QPushButton(self.widget_2)
        self.button_add.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.button_add.setObjectName("button_add")
        self.horizontalLayout_3.addWidget(self.button_add)
        self.button_edit = QtWidgets.QPushButton(self.widget_2)
        self.button_edit.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_edit.setFont(font)
        self.button_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.button_edit.setObjectName("button_edit")
        self.horizontalLayout_3.addWidget(self.button_edit)
        self.button_delete = QtWidgets.QPushButton(self.widget_2)
        self.button_delete.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout_3.addWidget(self.button_delete)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.edit_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.detail_page = QtWidgets.QWidget()
        self.detail_page.setObjectName("detail_page")
        self.frame_6 = QtWidgets.QFrame(self.detail_page)
        self.frame_6.setGeometry(QtCore.QRect(0, -10, 282, 404))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.detail_name = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_name.setFont(font)
        self.detail_name.setText("")
        self.detail_name.setObjectName("detail_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.detail_name)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.detail_add = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_add.setFont(font)
        self.detail_add.setText("")
        self.detail_add.setObjectName("detail_add")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.detail_add)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.detail_phone = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_phone.setFont(font)
        self.detail_phone.setText("")
        self.detail_phone.setObjectName("detail_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.detail_phone)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.detail_banknum = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_banknum.setFont(font)
        self.detail_banknum.setText("")
        self.detail_banknum.setObjectName("detail_banknum")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.detail_banknum)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.detail_bankname = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_bankname.setFont(font)
        self.detail_bankname.setText("")
        self.detail_bankname.setObjectName("detail_bankname")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.detail_bankname)
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.detail_status = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_status.setFont(font)
        self.detail_status.setText("")
        self.detail_status.setObjectName("detail_status")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.detail_status)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.detail_admin = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.detail_admin.setFont(font)
        self.detail_admin.setText("")
        self.detail_admin.setObjectName("detail_admin")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.detail_admin)
        self.stackedWidget.addWidget(self.detail_page)
        self.edit_page = QtWidgets.QWidget()
        self.edit_page.setObjectName("edit_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.edit_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.field1_name = QtWidgets.QFrame(self.edit_page)
        self.field1_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field1_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field1_name.setObjectName("field1_name")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.field1_name)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_label = QtWidgets.QLabel(self.field1_name)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.horizontalLayout_2.setStretch(0, 1)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.field1_name)
        self.name_field = QtWidgets.QLineEdit(self.edit_page)
        self.name_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_field.setObjectName("name_field")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_field)
        self.address_label = QtWidgets.QLabel(self.edit_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.role_label = QtWidgets.QLabel(self.edit_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.role_label.setFont(font)
        self.role_label.setObjectName("role_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.role_label)
        self.phone_label = QtWidgets.QLabel(self.edit_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.phone_label)
        self.total_field = QtWidgets.QLineEdit(self.edit_page)
        self.total_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.total_field.setObjectName("total_field")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.total_field)
        self.combo_pay = QtWidgets.QComboBox(self.edit_page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.combo_pay.setFont(font)
        self.combo_pay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_pay.setCurrentText("")
        self.combo_pay.setObjectName("combo_pay")
        self.combo_pay.addItem("")
        self.combo_pay.addItem("")
        self.combo_pay.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.combo_pay)
        self.combo_staff = QtWidgets.QComboBox(self.edit_page)
        self.combo_staff.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_staff.setObjectName("combo_staff")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_staff)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.frame = QtWidgets.QFrame(self.edit_page)
        self.frame.setMinimumSize(QtCore.QSize(0, 25))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_5.addWidget(self.frame)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.edit_page)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 336, 191))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.list_prod_edit = QtWidgets.QVBoxLayout()
        self.list_prod_edit.setObjectName("list_prod_edit")
        self.verticalLayout_7.addLayout(self.list_prod_edit)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.addWidget(self.scrollArea_3)
        self.field10_state = QtWidgets.QFrame(self.edit_page)
        self.field10_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field10_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field10_state.setObjectName("field10_state")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.field10_state)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox = QtWidgets.QCheckBox(self.field10_state)
        self.checkBox.setCheckable(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_12.addWidget(self.checkBox)
        self.button_cancel = QtWidgets.QPushButton(self.field10_state)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_cancel.setFont(font)
        self.button_cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_12.addWidget(self.button_cancel)
        self.button_save = QtWidgets.QPushButton(self.field10_state)
        self.button_save.setMinimumSize(QtCore.QSize(0, 30))
        self.button_save.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_12.addWidget(self.button_save)
        self.verticalLayout_5.addWidget(self.field10_state)
        self.stackedWidget.addWidget(self.edit_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.edit_view)
        self.list_product_2 = QtWidgets.QFrame(invoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_product_2.sizePolicy().hasHeightForWidth())
        self.list_product_2.setSizePolicy(sizePolicy)
        self.list_product_2.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(218, 221, 225);")
        self.list_product_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_product_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_product_2.setObjectName("list_product_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.list_product_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.list_staff_label_2 = QtWidgets.QLabel(self.list_product_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.list_staff_label_2.sizePolicy().hasHeightForWidth())
        self.list_staff_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_staff_label_2.setFont(font)
        self.list_staff_label_2.setObjectName("list_staff_label_2")
        self.verticalLayout_4.addWidget(self.list_staff_label_2)
        self.line_2 = QtWidgets.QFrame(self.list_product_2)
        font = QtGui.QFont()
        font.setPointSize(4)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("border-color: rgb(103, 103, 103);\n"
"background-color: rgb(79, 79, 79);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.list_product_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 206, 463))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.scrollAreaWidgetContents_2.setFont(font)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.horizontalLayout.addWidget(self.list_product_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(invoice)
        self.stackedWidget.setCurrentIndex(1)
        self.combo_pay.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(invoice)

    def retranslateUi(self, invoice):
        _translate = QtCore.QCoreApplication.translate
        invoice.setWindowTitle(_translate("invoice", "Form"))
        self.list_staff_label.setText(_translate("invoice", "Danh sách đơn hàng"))
        self.button_add.setText(_translate("invoice", "Thêm"))
        self.button_edit.setText(_translate("invoice", "Sửa"))
        self.button_delete.setText(_translate("invoice", "Xóa"))
        self.label.setText(_translate("invoice", "Tên"))
        self.label_3.setText(_translate("invoice", "Địa chỉ"))
        self.label_5.setText(_translate("invoice", "Phone"))
        self.label_7.setText(_translate("invoice", "BankNum"))
        self.label_9.setText(_translate("invoice", "Bank name"))
        self.label_11.setText(_translate("invoice", "status"))
        self.label_13.setText(_translate("invoice", "isAdmin"))
        self.name_label.setText(_translate("invoice", "Khách hàng"))
        self.address_label.setText(_translate("invoice", "Nhân viên"))
        self.role_label.setText(_translate("invoice", "Tổng tiền"))
        self.phone_label.setText(_translate("invoice", "Thanh toán"))
        self.combo_pay.setPlaceholderText(_translate("invoice", "Chọn phương thức thanh toán"))
        self.combo_pay.setItemText(0, _translate("invoice", "Cash"))
        self.combo_pay.setItemText(1, _translate("invoice", "Credit"))
        self.combo_pay.setItemText(2, _translate("invoice", "VnPay"))
        self.label_2.setText(_translate("invoice", "Tên"))
        self.label_4.setText(_translate("invoice", "Số lượng"))
        self.label_6.setText(_translate("invoice", "Thành tiền"))
        self.checkBox.setText(_translate("invoice", "Chế độ sửa"))
        self.button_cancel.setText(_translate("invoice", "Cancel"))
        self.button_save.setText(_translate("invoice", "Save"))
        self.list_staff_label_2.setText(_translate("invoice", "Danh sách sản phẩm"))
