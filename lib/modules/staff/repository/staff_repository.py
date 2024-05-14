import sys
sys.path.append('.\\lib\modules\staff\model')
sys.path.append('.\\lib\core')
from database_config import DatabaseConfig
from staff_model import StaffModel
import mysql.connector as connector



class StaffRepository:
    def __init__(self) -> None:
        self.db = connector.connect(host = DatabaseConfig().host, port = DatabaseConfig().port, user = DatabaseConfig().user, password = DatabaseConfig().password, database = DatabaseConfig().database)
        self.cursor = self.db.cursor()

    def getAllStaff(self):
        selectQuery = """SELECT * FROM staff"""
        self.cursor.execute(selectQuery)
        listData = self.cursor.fetchall()
        listStaff = []
        for e in listData:
            staff = StaffModel.from_row(e)
            listStaff.append(staff)
        return listStaff
    
    def updateStaff(self, staff):
        query = "UPDATE STAFF SET StaffName = %s, StaffAddress = %s, StaffRole = %s, StaffPhone = %s, RankSalary = %s, BankAccNumber = %s, BankName = %s, Status_ = %s, Username = %s, Password_ = %s, isAdmin = %s WHERE StaffId = %s"
        values = (staff.staff_name, staff.staff_address, staff.staff_role, staff.staff_phone, staff.rank_salary, staff.bank_acc_number, staff.bank_name, staff.status, staff.username, staff.password, staff.is_admin, str(staff.staff_id))
        self.cursor.execute(query, values)
        self.db.commit()
    
    def createStaff(self, staff):
        query = "INSERT INTO STAFF (StaffId, StaffName, StaffAddress, StaffRole, StaffPhone, RankSalary, BankAccNumber, BankName, Status_, Username, Password_, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (staff.staff_id, staff.staff_name, staff.staff_address, staff.staff_role, staff.staff_phone, staff.rank_salary, staff.bank_acc_number, staff.bank_name, staff.status, staff.username, staff.password, staff.is_admin)
        self.cursor.execute(query, values)
        self.db.commit()
    
    def deleteById(self, staffId):
        query = "DELETE FROM STAFF WHERE StaffId = %s"
        self.cursor.execute(query, (staffId,))
        self.db.commit()