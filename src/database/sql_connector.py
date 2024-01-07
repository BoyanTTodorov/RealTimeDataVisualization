import sqlite3

class SQLConnector:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS your_table_name (value REAL)")

    def insert_data(self, value):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO your_table_name (value) VALUES (?)", (value,))
