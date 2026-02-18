import sqlite3
class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("ElmosBalance.db")
        self.cursor = self.db.cursor()
        self.create_data_base()

    def commit(self):
        self.db.commit()

    def create_data_base(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (first_name TEXT, last_name TEXT, national_id TEXT, phone_number TEXT, user_name TEXT, password TEXT, city TEXT, email TEXT, birth_date TEXT, security_q_answer TEXT)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS income_categories (name TEXT PRIMARY KEY)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS expense_categories (name TEXT PRIMARY KEY)")
