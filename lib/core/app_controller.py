
import sys
sys.path.append('.\\lib\core')
sys.path.append('.\\lib\modules\invoice\model')
from database_config import DatabaseConfig
import mysql.connector as connector
from invoice_model import InvoiceModel
from matplotlib.ticker import FixedLocator
from PyQt5.QtCore import  pyqtSignal, QObject

### Create Singleton app controller
class AppController(QObject):
  signalRefreshStat = pyqtSignal(object) 
  user = None
  revenue_by_month = [0] * 12
  list_month = [x for x in range(1, 13)]
  fixed_locator = FixedLocator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
  total_reve = 0
  total_prod = 0
  total_invoice = 0

  def __init__(self) -> None:
      super().__init__()
      self.db = connector.connect(host = DatabaseConfig().host, port = DatabaseConfig().port, user = DatabaseConfig().user, password = DatabaseConfig().password, database = DatabaseConfig().database)
      self.cursor = self.db.cursor()
      self.fetchData()

  def fetchData(self):
    self.fetchRevenue()
    self.fetchProd()
  
  def fetchRevenue(self):
    self.total_reve = 0
    selectQuery = "SELECT * FROM INVOICE"
    self.cursor.execute(selectQuery)
    listData = self.cursor.fetchall()
    self.total_invoice = len(listData)
    listInvoiceModels = []
    for e in listData:
      invoice_model = InvoiceModel.from_row(e)
      listInvoiceModels.append(invoice_model)
    for i in range(len(self.revenue_by_month)):
      self.revenue_by_month[i] = 0
    for e in listInvoiceModels:
      month = e.date_.month
      self.revenue_by_month[month-1] += e.total
      self.total_reve += e.total
  def fetchProd(self):
    self.total_prod = 0
    selectQuery = "SELECT * FROM PRODUCT"
    self.cursor.execute(selectQuery)
    listData = self.cursor.fetchall()
    self.total_prod = len(listData)
  
  def refreshHomeStat(self):
    self.db.reconnect()
    self.fetchData()
    print(self.total_prod)
    self.signalRefreshStat.emit(True)

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(AppController, cls).__new__(cls)
    return cls.instance