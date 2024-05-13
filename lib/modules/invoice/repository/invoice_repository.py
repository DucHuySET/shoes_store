import sys
sys.path.append('.\lib\modules\invoice\model')
sys.path.append('.\lib\core')
from database_config import DatabaseConfig
from invoice_model import InvoiceModel
from invoice_detail_model import InvoiceDetailModel
from invoice_full import InvoiceFull
import mysql.connector as connector

class InvoiceRepository:
    def __init__(self):
        self.db = connector.connect(
            host=DatabaseConfig().host,
            port=DatabaseConfig().port,
            user=DatabaseConfig().user,
            password=DatabaseConfig().password,
            database=DatabaseConfig().database
        )
        self.cursor = self.db.cursor()

    def getAllInvoices(self):
        selectQuery = "SELECT * FROM INVOICE"
        self.cursor.execute(selectQuery)
        listData = self.cursor.fetchall()
        listInvoices = []
        for e in listData:
            invoice_model = InvoiceModel.from_row(e)
            listDetail = self.getAllProduct(invoice_model.invoice_id)
            invoiceFull = InvoiceFull(invoice_model, listDetail)
            listInvoices.append(invoiceFull)
        return listInvoices
    def getAllProduct(self, invoiceId):
        selectQuery = "SELECT * FROM INVOICE_DETAILS WHERE InvoiceId = %s"
        self.cursor.execute(selectQuery, (invoiceId,))
        listData = self.cursor.fetchall()
        listDetail = []
        for e in listData:
            detail = InvoiceDetailModel.from_row(e)
            listDetail.append(detail)
        return listDetail

    def updateInvoice(self, invoice):
        query = "UPDATE INVOICE SET CustomerId = %s, StaffId = %s, Payments = %s, Date_ = %s, Total = %s WHERE InvoiceId = %s"
        values = (invoice.customer_id, invoice.staff_id, invoice.payments, invoice.date_, invoice.total, invoice.invoice_id)
        self.cursor.execute(query, values)
        self.db.commit()

    def createInvoice(self, invoice):
        query = "INSERT INTO INVOICE (InvoiceId, CustomerId, StaffId, Payments, Date_, Total) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (invoice.invoice_id, invoice.customer_id, invoice.staff_id, invoice.payments, invoice.date_, invoice.total)
        self.cursor.execute(query, values)
        self.db.commit()
    def createInvoiceDetail(self, invoiceDetail):
        query = "INSERT INTO INVOICE_DETAILS (ProductId, InvoiceId, Quantity) VALUES (%s, %s, %s)"
        values = (invoiceDetail.product_id, invoiceDetail.invoice_id, invoiceDetail.quantity)
        self.cursor.execute(query, values)
        self.db.commit()

    def deleteInvoiceById(self, invoice_id):
        query = "DELETE FROM INVOICE WHERE InvoiceId = %s"
        self.cursor.execute(query, (invoice_id,))
        self.db.commit()
    def deleteInvoiceDetailById(self, invoice_id):
        query = "DELETE FROM INVOICE_DETAILS WHERE InvoiceId = %s"
        self.cursor.execute(query, (invoice_id,))
        self.db.commit()
    def getStaffbyId(self, staffId):
        query = "SELECT StaffName FROM STAFF WHERE StaffId = %s"
        self.cursor.execute(query, (staffId, ))
        staffName = self.cursor.fetchone()
        return staffName
    def getInvoiceDetail(self, invoice_id):
        query = "SELECT * FROM INVOICE_DETAILS WHERE InvoiceId = %s"
        self.cursor.execute(query, (invoice_id, ))
        list_data = self.cursor.fetchall()
        list_invoice_detail = []
        for e in list_data:
            invoice_detail = InvoiceDetailModel.from_row(e)
            list_invoice_detail.append(invoice_detail)
        return list_invoice_detail
