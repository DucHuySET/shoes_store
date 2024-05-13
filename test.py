import mysql.connector as connector

db = connector.connect(host = "localhost", port = "3306", user = "root", password = "123456aZ@", database = "QLCH_SHOES")
print(db)
cursor = db.cursor()
# select statement for tblemployee which returns all columns
employeetbl_select = """SELECT * FROM staff"""
 
# execute the select query to fetch all rows
cursor.execute(employeetbl_select)
 
# fetch all the data returned by the database
employee_data = cursor.fetchall()
 
# print all the data returned by the database
for e in employee_data:
    print(e[0])
 
# finally closing the database connection
db.close()