class StaffModel:
    def __init__(self) -> None:
        self.StaffId = ''
        self.StaffName = ''
        self.StaffAddress= ''
        self.StaffRole= ''
        self.StaffPhone= ''
        self.RankSalary= ''
        self.BankAccNumber = 0
        self.BankName = ''
        self.Status_ = True
        self.Username = ''
        self.Password_ = ''
        self.isAdmin = False
    def toQuery(self) -> str:
        return """
INSERT INTO STAFF (
	StaffId,
    StaffName,
    StaffAddress,
    StaffRole,
    StaffPhone,
    RankSalary,
    BankAccNumber,
    BankName,
    Status_,
    Username,
    Password_,
    isAdmin 
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
    def fromRow(self,rowItem):
        self.StaffId = rowItem[0]
        self.StaffName = rowItem[1]
        self.StaffAddress= rowItem[2]
        self.StaffRole= rowItem[3]
        self.StaffPhone= rowItem[4]
        self.RankSalary= rowItem[5]
        self.BankAccNumber = rowItem[6]
        self.BankName = rowItem[7]
        self.Status_ = rowItem[8]
        self.Username = rowItem[9]
        self.Password_ = rowItem[10]
        self.isAdmin = rowItem[11]
