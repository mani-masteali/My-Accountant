import re
from datetime import datetime
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QStandardItem
from db import DataBase
from __future__ import annotations
class User:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.nationalId = None
        self.phoneNumber = None
        self.userName = None
        self.password = None
        self.city = None
        self.email = None
        self.birthDate = None
        self.securityQAnswer = None
    # بررسی معتبر بودن اسم کوچک و تعریف آن برای کاربر

    def get_first_name(self, firstName):
        if len(re.findall('[a-z]', firstName))+len(re.findall('[A-Z]', firstName)) == len(firstName):
            self.firstName = firstName
        else:
            raise ValueError(
                'first name must only consist of English letters.')
    # بررسی معتبر بودن نام خانوادگی و تعریف آن برای کاربر

    def get_last_name(self, lastName):
        if len(re.findall('[a-z]', lastName))+len(re.findall('[A-Z]', lastName)) == len(lastName):
            self.lastName = lastName
        else:
            raise ValueError('last name must only consist of English letters.')
    # بررسی معتبر بودن کد ملی و تعریف آن برای کاربر

    def get_code_meli(self, nationalId):
        if len(nationalId) == 10:
            if len(re.findall('[0-9]', nationalId)) == len(nationalId):
                self.nationalId = nationalId
            else:
                raise ValueError('National ID only has numbers in it.')
        else:
            raise ValueError('National ID must have ten numbers.')
    # بررسی معتبر بودن شماره تلفن و تعریف آن برای کاربر

    def get_phone_number(self, phoneNumber):
        if len(phoneNumber) == 11 and len(re.findall('[0-9]', phoneNumber)) == len(phoneNumber) and bool(re.search('^09.', phoneNumber)) == True:
            self.phoneNumber = phoneNumber
        elif len(phoneNumber) != 11:
            raise ValueError('phone number must have eleven digits.')
        elif len(re.findall('[0-9]', phoneNumber)) != len(phoneNumber):
            raise ValueError('phone number must only consist of digits.')
        elif bool(re.search('^09.', phoneNumber)) == False:
            raise ValueError('[red]phone number must begin with 09.')
    # گرفتن یوزرنیم از کاربر  که می تواند به هر شکل دلخواه باشد.

    def get_username(self, userName, database):
        database.cursor.execute(
            "SELECT user_name FROM users WHERE user_name=?", (userName,))
        result = database.cursor.fetchone()
        if result:
            raise ValueError("This user name already exists")
        else:
            self.userName = userName
    # گرفتن پسورد در صورتی که شرایط دلخواه مسئله را رعایت کند

    def get_password(self, password):
        if len(password) >= 6 and len(re.findall('[a-z]', password)) >= 1 and len(re.findall('[A-Z]', password)) >= 1 and len(re.findall("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password)) >= 1 and len(re.findall('[0-9]', password)) >= 1:
            self.password = password
        elif len(password) < 6:
            raise ValueError('password must be at least 6 characters long.')
        elif len(re.findall('[a-z]', password)) < 1:
            raise ValueError(
                'password must contain at least one lowercase letter.')
        elif len(re.findall('[A-Z]', password)) < 1:
            raise ValueError(
                'password must contain at least one uppercase letter.')
        elif len(re.findall("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"), password) < 1:
            raise ValueError('password must contain at least one digit.')
        elif len(re.findall('[0-9]', password)) < 1:
            raise ValueError(
                'password must contain at least one special character (!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).')
    # برای تایید رمز عبور

    def check_repeated_password(self, repeatedPassword):
        if repeatedPassword != self.password:
            raise ValueError('passwords do not match')
        else:
            return 0
    # گرفتن نام شهر از کاربر از لیست شهر های تعریف شده در رابط گرافیکی

    def get_city(self, city):
        self.city = city
    # بررسی معتبر بودن ایمیل و گرفتن از کاربر

    def get_email(self, email, database):
        database.cursor.execute(
            "SELECT email FROM users WHERE email=?", (email,))
        result = database.cursor.fetchone()
        if result:
            raise ValueError("This email already exists")
        else:
            if bool(re.findall(r'[A-Za-z0-9]+@(gmail|yahoo)\.com', email)) == True:
                self.email = email
            else:
                raise ValueError('Invalid email')

    def get_birth_date(self, birthDate):
        if bool(re.findall('[1-2][0-9][0-9][0-9]/[0-1][0-9]/[0-3][0-9]', birthDate)) == True:
            year = birthDate[0:4]
            month = birthDate[5:7]
            day = birthDate[8:10]
            if int(year) >= 1920 and int(year) <= 2005 and 1 <= int(month) <= 12:
                max_days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
                            6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
                if 1 <= int(day) <= max_days[int(month)]:
                    self.birthDate = birthDate
                else:
                    raise ValueError(f'invalid day. this month has only {max_days[int(month)]}')
            elif int(year) < 1920 or int(year) > 2005:
                raise ValueError(f'birth year must be between 1920 and 2005')
            elif int(month) < 1 or int(month) > 12:
                raise ValueError(f'month must be between 1 and 12')
        else:
            raise ValueError(f'invalid birth date format')
    # گرفتن پاسخ سوال امنیتی که از کاربر پرسیده می شود

    def get_security_questions_answer(self, answer):
        self.securityQAnswer = answer
    # اطلاعات کاربر در یک دیتابیس ذخیره می شود

    def save_database(self, database):
        database.cursor.execute("INSERT INTO users(first_name, last_name, national_id, phone_number, user_name, password, city, email, birth_date, security_q_answer) VALUES(?,?,?,?,?,?,?,?,?,?)",
                                (self.firstName, self.lastName, self.nationalId, self.phoneNumber, self.userName, self.password, self.city, self.email, self.birthDate, self.securityQAnswer))
        database.commit()

class RegisterFine:
    def __init__(self, db):
        self.db = db

    def register_income(self, amount, date, category, description):
        self.validate_amount(amount)
        self.validate_date(date)
        self.validate_category(category)
        self.validate_description(description)

        cursor = self.db.cursor
        cursor.execute("INSERT INTO income_fine (amount, date, category, description) VALUES (?,?,?,?)",
                    (amount, date, category, description))
        self.db.commit()

    def register_expense(self, amount, date, category, description):
        self.validate_amount(amount)
        self.validate_date(date)
        self.validate_category(category)
        self.validate_description(description)

        cursor = self.db.cursor
        cursor.execute("INSERT INTO expense_fine (amount, date, category, description) VALUES (?,?,?,?)",
                    (amount, date, category, description))
        self.db.commit()

    def validate_amount(self, amount):
        if not amount:
            raise ValueError("Amount cannot be empty")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def validate_date(self, date):
        if not date:
            raise ValueError("Date cannot be empty")
        try:
            datetime.strptime(date, '%Y/%m/%d')
        except ValueError:
            raise ValueError("Invalid date format. Must be yyyy/mm/dd")

    def validate_category(self, category):
        if not category:
            raise ValueError("Category cannot be empty")

    def validate_description(self, description):
        if description and len(description) > 100:
            raise ValueError("Description must be 100 characters or less")

    def create_tables(self):
        cursor = self.db.cursor
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS income_fine (
                amount REAL,
                date TEXT,
                category TEXT,
                description TEXT
            )
        """)
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS expense_fine (
                amount REAL,
                date TEXT,
                category TEXT,
                description TEXT
            )
        """)
        self.db.commit()

class Category:
    def __init__(self, name):
        self.name = name

    def validate_name(self):
        if not self.name:
            raise ValueError("Category name cannot be empty")
        if len(self.name) > 15:
            raise ValueError(
                "Category name cannot be longer than 15 characters")
        if not re.match("^[A-Za-z0-9]*$", self.name):
            raise ValueError(
                "Category name can only contain English letters and numbers")

    def save_to_database(self, db, category_type):
        cursor = db.cursor
        cursor.execute(f"SELECT name FROM {category_type} WHERE name=?", (self.name,))
        if cursor.fetchone():
            raise ValueError("Category name already exists")
        cursor.execute(
            f"INSERT INTO {category_type} (name) VALUES (?)", (self.name,))
        db.commit()

class Search:
    def __init__(self, menu: SearchMenu):
        self.menu = menu
        self.model = self.menu.model
        self.table = self.menu.table

    def search(self, db: DataBase):
        self.searchText = self.menu.searchLine.text()
        self.searchfilters = {
            'day': self.menu.get_filters()[0] if self.menu.get_filters()[0].strip() else None,
            'month': self.menu.get_filters()[1] if self.menu.get_filters()[1].strip() else None,
            'year': self.menu.get_filters()[2] if self.menu.get_filters()[2].strip() else None,
            'income_expense': self.menu.get_filters()[3] if self.menu.get_filters()[3].strip() else None,
            'money_range': self.menu.get_filters()[4] if self.menu.get_filters()[4].strip() else None,
            'search_in': self.menu.get_filters()[5] if self.menu.get_filters()[5].strip() else None
        }
        if self.searchfilters['income_expense'] == 'income':
            base_query = f"SELECT * FROM income_fine WHERE (date LIKE '%{self.searchText}%' OR category LIKE '%{self.searchText}%' OR description LIKE '%{self.searchText}%' or amount LIKE '%{self.searchText}%')"
            self.filtering(base_query)
            db.cursor.execute(base_query)
            rows = db.cursor.fetchall()
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Amount", "Date", "Category", "Description"])
            for row in rows:
                date = QStandardItem(str(row[0]))
                category = QStandardItem(str(row[1]))
                description = QStandardItem(str(row[2]))
                amount = QStandardItem(str(row[3]))
                self.model.appendRow([date, category, description, amount])
            self.table.show()
        elif self.searchfilters['income_expense'] == 'expense':
            base_query = f"SELECT * FROM expense_fine WHERE (date LIKE '%{self.searchText}%' OR category LIKE '%{self.searchText}%' OR description LIKE '%{self.searchText}%' or amount LIKE '%{self.searchText}%')"
            self.filtering(base_query)
            db.cursor.execute(base_query)
            rows = db.cursor.fetchall()
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Amount", "Date", "Category", "Description"])
            for row in rows:
                date = QStandardItem(str(row[0]))
                category = QStandardItem(str(row[1]))
                description = QStandardItem(str(row[2]))
                amount = QStandardItem(str(row[3]))
                self.model.appendRow([date, category, description, amount])
            self.table.show()
        elif self.searchfilters['income_expense'] == 'both':
            base_query1 = base_query = f"SELECT * FROM income_fine WHERE (date LIKE '%{self.searchText}%' OR category LIKE '%{self.searchText}%' OR description LIKE '%{self.searchText}%' or amount LIKE '%{self.searchText}%')"
            self.filtering(base_query1)
            db.cursor.execute(base_query1)
            base_query2 = base_query = f"SELECT * FROM expense_fine WHERE (date LIKE '%{self.searchText}%' OR category LIKE '%{self.searchText}%' OR description LIKE '%{self.searchText}%' or amount LIKE '%{self.searchText}%')"
            self.filtering(base_query2)
            db.cursor.execute(base_query2)
            rows = db.cursor.fetchall()
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Amount", "Date", "Category", "Description"])
            for row in rows:
                date = QStandardItem(str(row[0]))
                category = QStandardItem(str(row[1]))
                description = QStandardItem(str(row[2]))
                amount = QStandardItem(str(row[3]))
                self.model.appendRow([date, category, description, amount])
            self.table.show()

    def filtering(self, base_query):
        for filter, value in self.searchfilters.items():
            if filter != 'income_expense' and value is not None:
                if filter == 'day' and value is not None:
                    base_query += f" AND SUBSTRING(date,9,2)='{value}'"
                elif filter == 'month' and value is not None:
                    base_query += f" AND SUBSTRING(date,6,2)='{value}'"
                elif filter == 'year' and value is not None:
                    base_query += f" AND SUBSTRING(date,1,4)='{value}'"
                elif filter == 'money_range' and value is not None:
                    value_range = value.split(sep=' ')
                    base_query += f" AND amount BETWEEN {value_range[0]} AND {value_range[1]}"
                elif filter == 'search_in' and value is not None:
                    if value == 'categories':
                        base_query += f" AND category='{value}'"
                    elif value == 'description':
                        base_query += f" AND description='{value}'"
                    elif value == 'both':
                        base_query += f" AND category='{value}' and description='{value}'"

class Report:
    def __init__(self, menu: ReportMenu):
        self.menu = menu
        self.model=self.menu.model
        self.table=self.menu.table
    def search(self, db: DataBase):
        self.searchfilters = {
            'day': self.menu.get_filters()[0] if self.menu.get_filters()[0].strip() else None,
            'month': self.menu.get_filters()[1] if self.menu.get_filters()[1].strip() else None,
            'year': self.menu.get_filters()[2] if self.menu.get_filters()[2].strip() else None,
            'income_expense': self.menu.get_filters()[3] if self.menu.get_filters()[3].strip() else None,
            'money_range': self.menu.get_filters()[4] if self.menu.get_filters()[4].strip() else None,
            'search_in': self.menu.get_filters()[5] if self.menu.get_filters()[5].strip() else None
        }
        if self.searchfilters['income_expense'] == 'income':
            base_query = ["SELECT * FROM income_fine WHERE"]
            print(base_query)
            self.filtering(base_query)
            db.cursor.execute(base_query[0])
            rows = db.cursor.fetchall()
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Amount", "Date", "Category", "Description"])
            for row in rows:
                date = QStandardItem(str(row[0]))
                category = QStandardItem(str(row[1]))
                description = QStandardItem(str(row[2]))
                amount = QStandardItem(str(row[3]))
                self.model.appendRow([date, category, description, amount])
            self.table.show()
        elif self.searchfilters['income_expense'] == 'expense':
            base_query = ["SELECT * FROM expense_fine WHERE"]
            self.filtering(base_query)
            db.cursor.execute(base_query[0])
            rows = db.cursor.fetchall()
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Amount", "Date", "Category", "Description"])
            for row in rows:
                date = QStandardItem(str(row[0]))
                category = QStandardItem(str(row[1]))
                description = QStandardItem(str(row[2]))
                amount = QStandardItem(str(row[3]))
                self.model.appendRow([date, category, description, amount])
            self.table.show()
            print(self.searchfilters)
            print(row)
        elif self.searchfilters['income_expense'] == 'both':
            base_query1 = base_query = ["SELECT * FROM income_fine WHERE"]
            self.filtering(base_query1)
            db.cursor.execute(base_query1[0])
            base_query2 = base_query = ["SELECT * FROM expense_fine WHERE"]
            self.filtering(base_query2)
            db.cursor.execute(base_query2[0])
            rows = db.cursor.fetchall()
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Amount", "Date", "Category", "Description"])
            for row in rows:
                date = QStandardItem(str(row[0]))
                category = QStandardItem(str(row[1]))
                description = QStandardItem(str(row[2]))
                amount = QStandardItem(str(row[3]))
                self.model.appendRow([date, category, description, amount])
            self.table.show()

    def filtering(self, base_query):
        print(self.searchfilters.items())
        for filter, value in self.searchfilters.items():
            if filter != 'income_expense' and value is not None:
                if filter == 'day' and value is not None:
                    base_query[0] += f" SUBSTR(date, 9) ='{value}'"
                elif filter == 'month' and value is not None:
                    base_query[0] += f" AND SUBSTR(date, 6, 2)='{value}'"
                elif filter == 'year' and value is not None:
                    base_query[0] += f" AND SUBSTR(date, 1, 4)='{value}'"
                elif filter == 'money_range' and value is not None:
                    value_range = value.split(sep=' ')
                    base_query[0] += f" AND amount BETWEEN {value_range[0]} AND {value_range[1]}"
                elif filter == 'search_in' and value is not None:
                        base_query[0] += f" AND category='{value}'"

