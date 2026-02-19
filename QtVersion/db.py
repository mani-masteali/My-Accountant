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
class FineRepository:
    def __init__(self, db: DataBase):
        self.db = db
    
    def _ensure_column(self, table: str, column: str, col_type: str):
        cur = self.db.cursor
        cur.execute(f"PRAGMA table_info({table})")
        columns = [info[1] for info in cur.fetchall()]
        if column not in columns:
            cur.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")
            self.db.commit()
    def create_tables(self):
        cur = self.db.cursor
        cur.execute("""
        CREATE TABLE IF NOT EXISTS income_fine (
            user_name TEXT,
            amount REAL,
            date TEXT,
            category TEXT,
            description TEXT
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS expense_fine (
            user_name TEXT,
            amount REAL,
            date TEXT,
            category TEXT,
            description TEXT
        )
        """)
        self.db.commit()
        self._ensure_column("income_fine", "user_name", "TEXT")
        self._ensure_column("expense_fine", "user_name", "TEXT")
    def insert_income(self,user_name, amount, date, category, description):
        self.db.cursor.execute("INSERT INTO income_fine (user_name, amount, date, category, description) VALUES (?, ?, ?, ?, ?)", (user_name, amount, date, category, description))
        self.db.commit()
    def insert_expense(self,user_name, amount, date, category, description):
        self.db.cursor.execute("INSERT INTO expense_fine (user_name, amount, date, category, description) VALUES (?, ?, ?, ?, ?)", (user_name, amount, date, category, description))
        self.db.commit()
class CategoryRepository:
    def __init__(self, db: DataBase):
        self.db = db
    def category_exists(self,table_name:str, name: str):
        cur = self.db.cursor
        cur.execute(f"SELECT 1 FROM {table_name} WHERE name = ? LIMIT 1", (name,))
        return cur.fetchone() is not None
    def insert_category(self,table_name:str, name: str):
        cur = self.db.cursor
        cur.execute(f"INSERT INTO {table_name} (name) VALUES (?)", (name,))
        self.db.commit()