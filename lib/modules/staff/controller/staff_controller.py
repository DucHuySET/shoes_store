import sys
sys.path.append('D:\CTARG_Project\Python\may_1\lib\modules\staff\model')
sys.path.append('D:\CTARG_Project\Python\may_1\lib\modules\staff\\repository')

from staff_repository import StaffRepository
from staff_model import StaffModel

from PyQt5.QtCore import QObject, pyqtSignal

class StaffController(QObject):
    signalSelectStaff = pyqtSignal(object) 
    def __init__(self) -> None:
        super().__init__()
        self.selectedStaff = None
        self.repository = StaffRepository()
        self.fetchListStaff()
    
    def fetchListStaff(self):
        self.listStaff = self.repository.getAllStaff()
    def setStaff(self, staff):
        if (self.selectedStaff != staff):
            self.selectedStaff = staff
            self.signalSelectStaff.emit(self.selectedStaff)
    def createStaff(self, staff):
        try:
            self.repository.createStaff(staff)
            return True
        except:
            return False
    def updateStaff(self, staff):     
        try:
            self.repository.updateStaff(staff)
            return True
        except:
            return False
    def deleteStaff(self, staffId):
        try:
            self.repository.deleteById(staffId)
            return True
        except:
            return False