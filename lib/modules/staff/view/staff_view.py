# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/ui/staff.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Staff(object):
    def setupUi(self, Staff):
        Staff.setObjectName("Staff")
        Staff.resize(1008, 547)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Staff)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_product = QtWidgets.QFrame(Staff)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 565, 463))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.list_product)
        self.edit_view = QtWidgets.QFrame(Staff)
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.edit_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.field1_name = QtWidgets.QFrame(self.edit_page)
        self.field1_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field1_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field1_name.setObjectName("field1_name")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.field1_name)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_label = QtWidgets.QLabel(self.field1_name)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.name_field = QtWidgets.QLineEdit(self.field1_name)
        self.name_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_field.setObjectName("name_field")
        self.horizontalLayout_2.addWidget(self.name_field)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field1_name)
        self.field2_addr = QtWidgets.QFrame(self.edit_page)
        self.field2_addr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field2_addr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field2_addr.setObjectName("field2_addr")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.field2_addr)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.address_label = QtWidgets.QLabel(self.field2_addr)
        self.address_label.setObjectName("address_label")
        self.horizontalLayout_4.addWidget(self.address_label)
        self.address_field = QtWidgets.QLineEdit(self.field2_addr)
        self.address_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.address_field.setObjectName("address_field")
        self.horizontalLayout_4.addWidget(self.address_field)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field2_addr)
        self.field3_role = QtWidgets.QFrame(self.edit_page)
        self.field3_role.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field3_role.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field3_role.setObjectName("field3_role")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.field3_role)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.role_label = QtWidgets.QLabel(self.field3_role)
        self.role_label.setObjectName("role_label")
        self.horizontalLayout_5.addWidget(self.role_label)
        self.role_field = QtWidgets.QLineEdit(self.field3_role)
        self.role_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.role_field.setObjectName("role_field")
        self.horizontalLayout_5.addWidget(self.role_field)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field3_role)
        self.field4_phone = QtWidgets.QFrame(self.edit_page)
        self.field4_phone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field4_phone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field4_phone.setObjectName("field4_phone")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.field4_phone)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.phone_label = QtWidgets.QLabel(self.field4_phone)
        self.phone_label.setObjectName("phone_label")
        self.horizontalLayout_6.addWidget(self.phone_label)
        self.phone_field = QtWidgets.QLineEdit(self.field4_phone)
        self.phone_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.phone_field.setObjectName("phone_field")
        self.horizontalLayout_6.addWidget(self.phone_field)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field4_phone)
        self.field5_salary = QtWidgets.QFrame(self.edit_page)
        self.field5_salary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field5_salary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field5_salary.setObjectName("field5_salary")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.field5_salary)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.salary_label = QtWidgets.QLabel(self.field5_salary)
        self.salary_label.setObjectName("salary_label")
        self.horizontalLayout_7.addWidget(self.salary_label)
        self.salary_field = QtWidgets.QLineEdit(self.field5_salary)
        self.salary_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.salary_field.setObjectName("salary_field")
        self.horizontalLayout_7.addWidget(self.salary_field)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field5_salary)
        self.field6_bankAcc = QtWidgets.QFrame(self.edit_page)
        self.field6_bankAcc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field6_bankAcc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field6_bankAcc.setObjectName("field6_bankAcc")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.field6_bankAcc)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.bankAcc_label = QtWidgets.QLabel(self.field6_bankAcc)
        self.bankAcc_label.setObjectName("bankAcc_label")
        self.horizontalLayout_8.addWidget(self.bankAcc_label)
        self.bankAcc_field = QtWidgets.QLineEdit(self.field6_bankAcc)
        self.bankAcc_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bankAcc_field.setObjectName("bankAcc_field")
        self.horizontalLayout_8.addWidget(self.bankAcc_field)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field6_bankAcc)
        self.field7_bankName = QtWidgets.QFrame(self.edit_page)
        self.field7_bankName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field7_bankName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field7_bankName.setObjectName("field7_bankName")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.field7_bankName)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.bankName_label = QtWidgets.QLabel(self.field7_bankName)
        self.bankName_label.setObjectName("bankName_label")
        self.horizontalLayout_9.addWidget(self.bankName_label)
        self.bankName_field = QtWidgets.QLineEdit(self.field7_bankName)
        self.bankName_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bankName_field.setObjectName("bankName_field")
        self.horizontalLayout_9.addWidget(self.bankName_field)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field7_bankName)
        self.field8_Username = QtWidgets.QFrame(self.edit_page)
        self.field8_Username.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field8_Username.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field8_Username.setObjectName("field8_Username")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.field8_Username)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.user_label = QtWidgets.QLabel(self.field8_Username)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout_10.addWidget(self.user_label)
        self.user_field = QtWidgets.QLineEdit(self.field8_Username)
        self.user_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_field.setObjectName("user_field")
        self.horizontalLayout_10.addWidget(self.user_field)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field8_Username)
        self.field9_pass = QtWidgets.QFrame(self.edit_page)
        self.field9_pass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field9_pass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field9_pass.setObjectName("field9_pass")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.field9_pass)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pass_label = QtWidgets.QLabel(self.field9_pass)
        self.pass_label.setObjectName("pass_label")
        self.horizontalLayout_11.addWidget(self.pass_label)
        self.pass_field = QtWidgets.QLineEdit(self.field9_pass)
        self.pass_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pass_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_field.setObjectName("pass_field")
        self.horizontalLayout_11.addWidget(self.pass_field)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.verticalLayout_4.addWidget(self.field9_pass)
        self.field10_state = QtWidgets.QFrame(self.edit_page)
        self.field10_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field10_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field10_state.setObjectName("field10_state")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.field10_state)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.status_check = QtWidgets.QCheckBox(self.field10_state)
        self.status_check.setObjectName("status_check")
        self.horizontalLayout_12.addWidget(self.status_check)
        self.isAdmin_check = QtWidgets.QCheckBox(self.field10_state)
        self.isAdmin_check.setChecked(False)
        self.isAdmin_check.setObjectName("isAdmin_check")
        self.horizontalLayout_12.addWidget(self.isAdmin_check)
        self.button_cancel = QtWidgets.QPushButton(self.field10_state)
        self.button_cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_12.addWidget(self.button_cancel)
        self.button_save = QtWidgets.QPushButton(self.field10_state)
        self.button_save.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_12.addWidget(self.button_save)
        self.verticalLayout_4.addWidget(self.field10_state)
        self.stackedWidget.addWidget(self.edit_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.edit_view)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Staff)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Staff)

    def retranslateUi(self, Staff):
        _translate = QtCore.QCoreApplication.translate
        Staff.setWindowTitle(_translate("Staff", "Form"))
        self.list_staff_label.setText(_translate("Staff", "Danh sách nhân viên"))
        self.button_add.setText(_translate("Staff", "Thêm"))
        self.button_edit.setText(_translate("Staff", "Sửa"))
        self.button_delete.setText(_translate("Staff", "Xóa"))
        self.label.setText(_translate("Staff", "Tên"))
        self.label_3.setText(_translate("Staff", "Địa chỉ"))
        self.label_5.setText(_translate("Staff", "Phone"))
        self.label_7.setText(_translate("Staff", "BankNum"))
        self.label_9.setText(_translate("Staff", "Bank name"))
        self.label_11.setText(_translate("Staff", "status"))
        self.label_13.setText(_translate("Staff", "isAdmin"))
        self.name_label.setText(_translate("Staff", "Name"))
        self.address_label.setText(_translate("Staff", "Address"))
        self.role_label.setText(_translate("Staff", "Role"))
        self.phone_label.setText(_translate("Staff", "Phone"))
        self.salary_label.setText(_translate("Staff", "Salary"))
        self.bankAcc_label.setText(_translate("Staff", "Bank Account"))
        self.bankName_label.setText(_translate("Staff", "Bank Name"))
        self.user_label.setText(_translate("Staff", "User Name"))
        self.pass_label.setText(_translate("Staff", "Password"))
        self.status_check.setText(_translate("Staff", "Status"))
        self.isAdmin_check.setText(_translate("Staff", "isAdmin"))
        self.button_cancel.setText(_translate("Staff", "Cancel"))
        self.button_save.setText(_translate("Staff", "Save"))