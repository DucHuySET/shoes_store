import sys
sys.path.append('.\\lib\modules\customer\model')
sys.path.append('.\\lib\core')
from database_config import DatabaseConfig
from customer_model import CustomerModel
import mysql.connector as connector
class CustomerRepository:

    def __init__(self):
        self.db = connector.connect(
            host=DatabaseConfig().host,
            port=DatabaseConfig().port,
            user=DatabaseConfig().user,
            password=DatabaseConfig().password,
            database=DatabaseConfig().database
        )
        self.cursor = self.db.cursor()

    def get_all_customers(self):
        select_query = "SELECT * FROM Customer"
        self.cursor.execute(select_query)
        list_data = self.cursor.fetchall()
        list_customers = []
        for row in list_data:
            customer = CustomerModel.from_row(row)
            list_customers.append(customer)
        return list_customers

    def get_customer_by_id(self, customer_id):
        select_query = "SELECT * FROM Customer WHERE CustomerId = %s"
        self.cursor.execute(select_query, (customer_id,))
        customer_data = self.cursor.fetchone()
        if customer_data:
            return CustomerModel.from_row(customer_data)
        else:
            return None

    def create_customer(self, customer):
        insert_query = ("INSERT INTO Customer (CustomerId, CustomerName, CustomerPhone, "
                        "CustomerEmail, CustomerAddress) VALUES (%s, %s, %s, %s, %s)")
        values = (customer.customer_id, customer.customer_name, customer.customer_phone,
                  customer.customer_email, customer.customer_address)
        try:
            self.cursor.execute(insert_query, values)
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error creating customer: {e}")
            return False

    def update_customer(self, customer):
        update_query = ("UPDATE Customer SET CustomerName = %s, CustomerPhone = %s, "
                        "CustomerEmail = %s, CustomerAddress = %s WHERE CustomerId = %s")
        values = (customer.customer_name, customer.customer_phone, customer.customer_email,
                  customer.customer_address, customer.customer_id)
        try:
            self.cursor.execute(update_query, values)
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error updating customer: {e}")
            return False

    def delete_customer_by_id(self, customer_id):
        delete_query = "DELETE FROM Customer WHERE CustomerId = %s"
        try:
            self.cursor.execute(delete_query, (customer_id,))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error deleting customer: {e}")
            return False

    def reconnect(self):
        self.db.reconnect()
