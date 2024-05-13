
import mysql.connector as connector

from lib.modules.login.model.user_model import StaffModel

class LoginController:
    
    def __init__(self) -> None:
        self.isAdmin = False
        self.db = connector.connect(host = "localhost", port = "3306", user = "root", password = "123456aZ@", database = "QLCH_SHOES")
        self.cursor = self.db.cursor()
    # def __delattr__(self, name: str) -> None:
    #     pass
    def login(self, username, password):
        selectQuery = """SELECT * FROM staff"""
        self.cursor.execute(selectQuery)
        listInfo = self.cursor.fetchall()
        self.listStaff = []
        for e in listInfo:
            staffModel = StaffModel()
            staffModel.fromRow(e)
            self.listStaff.append(staffModel)
        for e in self.listStaff:
            if (e.Username == username and e.Password_ == password):
                return True, e
        return False, e
