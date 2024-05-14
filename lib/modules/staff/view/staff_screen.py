import sys
sys.path.append('.\\lib\modules\staff\model')
sys.path.append('.\\lib\modules\staff\controller')
sys.path.append('.\\lib\modules\staff\model')
sys.path.append('.\\lib\\ui')

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PyQt5 import QtCore

from staff_controller import StaffController

from staff_view import Ui_Staff
from staff_card import Ui_staff_card
from staff_model import StaffModel
# from confirm_dialog_ui import Ui_confirm_dialog


### Mode 0: create, 1: update

class StaffScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.mode = 0
        self.controller = StaffController()
        self.controller.signalSelectStaff.connect(self.showDetail)
        self.ui = Ui_Staff()
        self.ui.setupUi(self)
        self.viewStaff()
        self.ui.button_add.clicked.connect(self.gotoEditForm)
        self.ui.button_save.clicked.connect(self.save)
        self.ui.button_cancel.clicked.connect(self.cancel)
        self.ui.button_edit.clicked.connect(self.gotoEditCurrentStaff)
        self.ui.button_delete.clicked.connect(self.delete)
    
    def viewStaff(self):
        self.clearLayout(self.ui.gridLayout)
        row = 0
        if (len(self.controller.listStaff) > 0):
            for i in range(len(self.controller.listStaff)):
                staffCard = StaffCard(self.controller.listStaff[i], self.controller)
                if (i % 3 == 0):                 
                    self.ui.gridLayout.addWidget(staffCard, row, 0, 1, 1)
                elif (i % 3 == 1):                 
                    self.ui.gridLayout.addWidget(staffCard, row, 1, 1, 1)
                else:
                    self.ui.gridLayout.addWidget(staffCard, row, 2, 1, 1)
                    row += 1
    def showDetail(self,staff):
        self.gotoDetail()
        self.ui.detail_name.setText(staff.staff_name)
        self.ui.detail_add.setText(staff.staff_address)
        self.ui.detail_phone.setText(staff.staff_phone)
        self.ui.detail_banknum.setText(str(staff.bank_acc_number))
        self.ui.detail_bankname.setText(staff.bank_name)
        self.ui.detail_status.setText(str(staff.status))
        self.ui.detail_admin.setText(str(staff.is_admin))
    def gotoDetail(self):
        if (self.ui.stackedWidget.currentIndex() == 1):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()-1)
    def gotoEditForm(self):
        if (self.ui.stackedWidget.currentIndex() == 0):
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()+1)
    def gotoEditCurrentStaff(self):
        self.mode = 1
        self.prepareEdit()
        self.gotoEditForm()

    def save(self):
        staff_id = str(int(self.controller.listStaff[len(self.controller.listStaff)-1].staff_id) + 1)
        staff = StaffModel(staff_id=staff_id ,
                           staff_name=self.ui.name_field.text(),
                           staff_address=self.ui.address_field.text(),
                           staff_role=self.ui.role_field.text(),
                           staff_phone=self.ui.phone_field.text(),
                           rank_salary=self.ui.salary_field.text(),
                           bank_acc_number=self.ui.bankAcc_field.text(),
                           bank_name=self.ui.bankName_field.text(),
                           status=self.ui.status_check.isChecked(),
                           is_admin=self.ui.isAdmin_check.isChecked(),
                           password=self.ui.pass_field.text(),
                           username=self.ui.user_field.text())
        result = False
        if (self.mode == 0):
            staff_id = str(int(self.controller.listStaff[len(self.controller.listStaff)-1].staff_id) + 1)
            staff = StaffModel(staff_id=staff_id ,
                           staff_name=self.ui.name_field.text(),
                           staff_address=self.ui.address_field.text(),
                           staff_role=self.ui.role_field.text(),
                           staff_phone=self.ui.phone_field.text(),
                           rank_salary=self.ui.salary_field.text(),
                           bank_acc_number=self.ui.bankAcc_field.text(),
                           bank_name=self.ui.bankName_field.text(),
                           status=self.ui.status_check.isChecked(),
                           is_admin=self.ui.isAdmin_check.isChecked(),
                           password=self.ui.pass_field.text(),
                           username=self.ui.user_field.text())
            result = self.controller.createStaff(staff)
        elif (self.mode == 1):
            staff = StaffModel(staff_id=self.controller.selectedStaff.staff_id,
                           staff_name=self.ui.name_field.text(),
                           staff_address=self.ui.address_field.text(),
                           staff_role=self.ui.role_field.text(),
                           staff_phone=self.ui.phone_field.text(),
                           rank_salary=self.ui.salary_field.text(),
                           bank_acc_number=self.ui.bankAcc_field.text(),
                           bank_name=self.ui.bankName_field.text(),
                           status=self.ui.status_check.isChecked(),
                           is_admin=self.ui.isAdmin_check.isChecked(),
                           password=self.ui.pass_field.text(),
                           username=self.ui.user_field.text())
            result = self.controller.updateStaff(staff)
        if (result):
            self.clearInput()
            self.refresh()
    def cancel(self):
        self.clearInput()
        if (self.mode == 1):
            self.gotoDetail()
    def clearInput(self):
        self.ui.name_field.clear()
        self.ui.address_field.clear()
        self.ui.role_field.clear()
        self.ui.phone_field.clear()
        self.ui.salary_field.clear()
        self.ui.bankAcc_field.clear()
        self.ui.bankName_field.clear()
        self.ui.user_field.clear()
        self.ui.pass_field.clear()
        self.ui.status_check.setChecked(False)
        self.ui.isAdmin_check.setChecked(False)
    def refresh(self):
        self.controller.fetchListStaff()
        self.viewStaff()
    def prepareEdit(self):
        if (self.controller.selectedStaff != None):
            self.setInput(self.controller.selectedStaff)
    def setInput(self, staff):
        self.ui.name_field.setText(staff.staff_name)
        self.ui.address_field.setText(staff.staff_address)
        self.ui.role_field.setText(staff.staff_role)
        self.ui.phone_field.setText(staff.staff_phone)
        self.ui.salary_field.setText(str(staff.rank_salary))
        self.ui.bankAcc_field.setText(str(staff.bank_acc_number))
        self.ui.bankName_field.setText(staff.bank_name)
        self.ui.user_field.setText(staff.username)
        self.ui.pass_field.setText(staff.password)
        self.ui.status_check.setChecked(staff.status)
        self.ui.isAdmin_check.setChecked(staff.is_admin)
    def delete(self):
        self.dialog = CustomDialog(self)
        if self.dialog.exec():
            self.controller.deleteStaff(self.controller.selectedStaff.staff_id)
            self.refresh()
            self.gotoEditForm()
    def clearLayout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
class StaffCard(QWidget):
    def __init__(self, staff, controller):
        self.staff = staff
        self.controller = controller
        super().__init__()
        self.ui = Ui_staff_card()
        self.ui.setupUi(self)
        self.ui.name_content.setText(self.staff.staff_name)
        self.ui.phone_content.setText(self.staff.staff_phone)
        self.ui.addr_content.setText(self.staff.staff_address)
        self.ui.pushButton.clicked.connect(self.selectStaff)
    
    def selectStaff(self):
        self.controller.setStaff(self.staff)

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