import os
import sqlite3 

class CommonSqliteActions:
    def __init__(self):
        self.openDb()

    def openDb(self):
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'investment_accounts.db'))
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def closeDb(self):
        self.connection.commit()
        self.connection.close()