class StaffModel:
    def __init__(self, staff_id, staff_name, staff_address, staff_role, staff_phone, rank_salary, bank_acc_number, bank_name, status, username, password, is_admin):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_address = staff_address
        self.staff_role = staff_role
        self.staff_phone = staff_phone
        self.rank_salary = rank_salary
        self.bank_acc_number = bank_acc_number
        self.bank_name = bank_name
        self.status = status
        self.username = username
        self.password = password
        self.is_admin = is_admin

    @staticmethod
    def createQueryInsert(staff):
        query = "INSERT INTO STAFF (StaffId, StaffName, StaffAddress, StaffRole, StaffPhone, RankSalary, BankAccNumber, BankName, Status_, Username, Password_, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (staff.staff_id, staff.staff_name, staff.staff_address, staff.staff_role, staff.staff_phone, staff.rank_salary, staff.bank_acc_number, staff.bank_name, staff.status, staff.username, staff.password, staff.is_admin)
        return query, values

    @staticmethod
    def from_row(row):
            return StaffModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

