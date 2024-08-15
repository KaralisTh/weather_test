import sqlite3
import os

class DbConnection:
    def __init__(self):
        self.db_name = os.getenv('DB_NAME', 'weather_data.db')

    def execute_query(self, query: str, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor, conn

    def fetch_data(self, query: str, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
