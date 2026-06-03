import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="lex_invoice.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # جدول العملاء
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clients 
                            (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)''')
        
        # جدول الفواتير
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS invoices 
                            (id INTEGER PRIMARY KEY, client_id INTEGER, amount REAL, 
                             status TEXT, date TEXT, FOREIGN KEY(client_id) REFERENCES clients(id))''')
        self.conn.commit()

    def add_client(self, name, email, phone):
        self.cursor.execute("INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        self.conn.commit()

    def add_invoice(self, client_id, amount, status, date):
        self.cursor.execute("INSERT INTO invoices (client_id, amount, status, date) VALUES (?, ?, ?, ?)", 
                            (client_id, amount, status, date))
        self.conn.commit()

    def close(self):
        self.conn.close()
