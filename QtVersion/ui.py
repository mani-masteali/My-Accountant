import sys

from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QLabel, QLineEdit, QGridLayout, QWidget,
    QComboBox, QRadioButton, QButtonGroup, QTableView, QVBoxLayout
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QStandardItemModel

from db import DataBase
from logic import User, RegisterFine, Category, Search, Report


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("QtVersion/Logo.png"))
        self.setWindowTitle("ElmosBalance")
        self.setFixedSize(800, 600)
        self.showMaximized()
        self.db = DataBase()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.signupLoginMenu = SignupLoginMenu(self)

class SignupLoginMenu():
    def __init__(self, window: MyWindow):
        self.window = window
        self.singuping = False
        self.logining = False
        self.wrongpass=0
        self.login_signup_menu()

    def login_signup_menu(self):
        self.welcominglabel = QLabel(
            'Welcome to elmos balance. If you wish to continue, press login or signup.', self.window)
        self.welcominglabel.setGeometry(150, 100, 400, 200)
        self.welcominglabel.show()
        self.signupButton = QPushButton('Sign up', self.window)
        self.signupButton.setGeometry(300, 250, 200, 50)
        self.signupButton.clicked.connect(self.signup)
        self.signupButton.show()
        self.signinButton = QPushButton('Log in', self.window)
        self.signinButton.setGeometry(300, 350, 200, 50)
        self.signinButton.clicked.connect(self.login)
    # functions for signup
        self.signinButton.show()

    def signup(self):
        # hiding buttons and the label from the very beginning menu
        self.welcominglabel.hide()
        self.signupButton.hide()
        self.signinButton.hide()
        self.user = User()
        self.layout = QGridLayout(self.window.centralWidget())
        # variables for first name
        self.firstNameLabel = QLabel('enter your first name: ', self.window)
        self.firstNameLine = QLineEdit(self.window)
        self.firstnamewarning = QLabel(' ', self.window)
        # variables for last name
        self.lastNameLabel = QLabel('enter your last name: ', self.window)
        self.lastNameLine = QLineEdit(self.window)
        self.lastnamewarning = QLabel(' ', self.window)
        # variables for national id
        self.nationalIDLabel = QLabel('enter your national id: ', self.window)
        self.nationalIDLine = QLineEdit(self.window)
        self.nationalIDwarning = QLabel(' ', self.window)
        # variables for phone number
        self.phoneNumberLabel = QLabel(
            'enter your phone number: ', self.window)
        self.phoneNumberLine = QLineEdit(self.window)
        self.phonenumberwarning = QLabel(' ', self.window)
        # variabled for user name
        self.userNameLabel = QLabel('enter your user name: ', self.window)
        self.userNameLine = QLineEdit(self.window)
        self.usernamewarning = QLabel(' ', self.window)
        # variables for password
        self.passwordLabel = QLabel('enter your password: ', self.window)
        self.passwordLine = QLineEdit(self.window)
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordwarning = QLabel(' ', self.window)
        # variables for repeated password
        self.repeatedpasswordLabel = QLabel(
            'confirm your password: ', self.window)
        self.repeatedpasswordLine = QLineEdit(self.window)
        self.repeatedpasswordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeatedpasswordwarning = QLabel(' ', self.window)
        # variables for choosing the city
        self.cityLabel = QLabel('choose your city: ', self.window)
        self.cityCombobox = QComboBox(self.window)
        self.cities = ['Karaj',
                    'Ardabil',
                    'Bushehr',
                    'Shahrekord',
                    'Tabriz',
                    'Shiraz',
                    'Rasht',
                    'Gorgan',
                    'Hamadan',
                    'Bandar Abas',
                    'Ilam',
                    'Isfahan',
                    'Kerman',
                    'Kermanshah',
                    'Ahwaz',
                    'Yasuj',
                    'Sanandaj',
                    'Khoramabad',
                    'Arak',
                    'Sari',
                    'Bojnurd',
                    'Qazvin',
                    'Qom',
                    'Mashhad',
                    'Semnan',
                    'Zahedan',
                    'Birjand',
                    'Tehran',
                    'Urmia',
                    'Yazd',
                    'Zanjan']
        self.cityCombobox.addItems(self.cities)
        # variables for email
        self.emailLabel = QLabel('enter your email: ', self.window)
        self.emailLine = QLineEdit(self.window)
        self.emailwarning = QLabel(' ', self.window)
        # variables for date
        self.dateLabel = QLabel('enter your birth date: ', self.window)
        self.dateLine = QLineEdit(self.window)
        self.datewarning = QLabel(' ', self.window)
        # variables for security question answers
        self.securityLabel = QLabel('What is your favorite car brand?')
        self.securityLine = QLineEdit(self.window)
        # submit button
        self.submit = QPushButton('Submit', self.window)
        self.submit.clicked.connect(self.submit_button)
        # show and set layout
        self.layout.addWidget(self.firstNameLabel, 0, 0)
        self.layout.addWidget(self.firstNameLine, 0, 1)
        self.layout.addWidget(self.firstnamewarning, 0, 2)
        self.layout.addWidget(self.lastNameLabel, 1, 0)
        self.layout.addWidget(self.lastNameLine, 1, 1)
        self.layout.addWidget(self.lastnamewarning, 1, 2)
        self.layout.addWidget(self.nationalIDLabel, 2, 0)
        self.layout.addWidget(self.nationalIDLine, 2, 1)
        self.layout.addWidget(self.nationalIDwarning, 2, 2)
        self.layout.addWidget(self.phoneNumberLabel, 3, 0)
        self.layout.addWidget(self.phoneNumberLine, 3, 1)
        self.layout.addWidget(self.phonenumberwarning, 3, 2)
        self.layout.addWidget(self.userNameLabel, 4, 0)
        self.layout.addWidget(self.userNameLine, 4, 1)
        self.layout.addWidget(self.usernamewarning, 4, 2)
        self.layout.addWidget(self.passwordLabel, 5, 0)
        self.layout.addWidget(self.passwordLine, 5, 1)
        self.layout.addWidget(self.passwordwarning, 5, 2)
        self.layout.addWidget(self.repeatedpasswordLabel, 6, 0)
        self.layout.addWidget(self.repeatedpasswordLine, 6, 1)
        self.layout.addWidget(self.repeatedpasswordwarning, 6, 2)
        self.layout.addWidget(self.cityLabel, 7, 0)
        self.layout.addWidget(self.cityCombobox, 7, 1)
        self.layout.addWidget(self.emailLabel, 8, 0)
        self.layout.addWidget(self.emailLine, 8, 1)
        self.layout.addWidget(self.emailwarning, 8, 2)
        self.layout.addWidget(self.dateLabel, 9, 0)
        self.layout.addWidget(self.dateLine, 9, 1)
        self.layout.addWidget(self.datewarning, 9, 2)
        self.layout.addWidget(self.securityLabel, 10, 0)
        self.layout.addWidget(self.securityLine, 10, 1)
        self.layout.addWidget(self.submit, 11, 0, 1, 3)
    
    def _validate_field(self,getter,value,warning_label:QLabel,*extra_args):
        try:
            getter(value,*extra_args)
            if warning_label.text().strip():
                warning_label.setText(" ")
        except ValueError as e:
            warning_label.setText(str(e))

    def get_first_name(self):
        self._validate_field(self.user.get_first_name,self.firstNameLine.text(),self.firstnamewarning)

    def get_last_name(self):
        self._validate_field(self.user.get_last_name,self.lastNameLine.text(),self.lastnamewarning)

    def get_code_meli(self):
        self._validate_field(self.user.get_code_meli,self.nationalIDLine.text(),self.nationalIDwarning)

    def get_phone_number(self):
        self._validate_field(self.user.get_phone_number,self.phoneNumberLine.text(),self.phonenumberwarning)

    def get_user_name(self):
        self._validate_field(self.user.get_username,self.userNameLine.text(),self.usernamewarning,self.window.db)

    def get_password(self):
        self._validate_field(self.user.get_password,self.passwordLine.text(),self.passwordwarning)

    def check_repeated_password(self):
        self._validate_field(self.user.check_repeated_password,self.repeatedpasswordLine.text(),self.repeatedpasswordwarning)

    def get_city(self):
        self.user.get_city(self.cityCombobox.currentText())

    def get_email(self):
        self._validate_field(self.user.get_email, self.emailLine.text(), self.emailwarning, self.window.db)

    def get_birth_date(self):
        self._validate_field(self.user.get_birth_date, self.dateLine.text(), self.datewarning)

    def get_security_questions_answer(self):
        self.securityLineText = self.securityLine.text()
        self.user.get_security_questions_answer(self.securityLineText)

    def clear_layout(self, layout):
        for row in range(layout.rowCount()):
            for column in range(layout.columnCount()):
                item = layout.itemAtPosition(row, column)
                if item:
                    widget = item.widget()
                    if widget:
                        widget.setVisible(False)

    def return_layout(self, layout):
        for row in range(layout.rowCount()):
            for column in range(layout.columnCount()):
                item = layout.itemAtPosition(row, column)
                if item:
                    widget = item.widget()
                    if widget:
                        widget.setVisible(False)

    def submit_button(self):
        self.valid = True
        self.get_first_name()
        self.get_last_name()
        self.get_code_meli()
        self.get_phone_number()
        self.get_user_name()
        self.get_password()
        self.check_repeated_password()
        self.get_city()
        self.get_email()
        self.get_birth_date()
        self.get_security_questions_answer()
        if self.firstnamewarning.text() != ' ' or self.lastnamewarning.text() != ' ' or self.nationalIDwarning.text() != ' ' or self.phonenumberwarning.text() != ' ' or self.usernamewarning.text() != ' ' or self.passwordwarning.text() != ' ' or self.repeatedpasswordwarning.text() != ' ' or self.emailwarning.text() != ' ' or self.datewarning.text() != ' ':
            self.valid = False
        if self.valid:
            self.singuping = True
            self.user.save_database(self.window.db)
            self.clear_layout(self.layout)
            self.mainMenu = MainMenu(self.window)
    # functions for login

    def login(self):
        self.welcominglabel.hide()
        self.signupButton.hide()
        self.signinButton.hide()
        # variables for user name
        self.loginlayout = QGridLayout(self.window.centralWidget())
        self.userNameLoginLabel = QLabel('enter your username: ', self.window)
        self.userNameLoginLine = QLineEdit(self.window)
        # variables for password
        self.passwordLoginLabel = QLabel('enter your password: ', self.window)
        self.passwordLoginLine = QLineEdit(self.window)
        self.passwordLoginLine.setEchoMode(QLineEdit.EchoMode.Password)
        # submit button
        self.Loginsubmit = QPushButton('Submit', self.window)
        self.Loginsubmit.clicked.connect(self.submit_login)
        # warning if the username or password was wrong
        self.Loginwarning = QLabel(' ', self.window)
        # variables for forget password
        self.forgetpassword = QLabel('forgot password', self.window)
        self.forgetpassword.mousePressEvent = self.forget_password
        # layout
        self.loginlayout.addWidget(self.userNameLoginLabel, 0, 0)
        self.loginlayout.addWidget(self.userNameLoginLine, 0, 1)
        self.loginlayout.addWidget(self.passwordLoginLabel, 1, 0, 1, 1)
        self.loginlayout.addWidget(self.passwordLoginLine, 1, 1, 1, 1)
        self.loginlayout.addWidget(self.Loginwarning, 3, 1, 1, 1)
        self.loginlayout.addWidget(self.Loginsubmit, 2, 1)
        self.loginlayout.addWidget(self.forgetpassword, 2, 0)
        self.loginlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def check_user_and_pass(self):
        self.window.db.cursor.execute("SELECT user_name,password FROM users WHERE user_name=? AND password=?", (
            self.userNameLoginLine.text(), self.passwordLoginLine.text()))
        result = self.window.db.cursor.fetchone()
        if result:
            self.wrongpass=0
            self.logining = True
            self.usernamelogin = self.userNameLoginLine.text()
            self.clear_layout(self.loginlayout)
            self.mainMenu = MainMenu(self.window)
        else:
            self.wrongpass+=1
            self.Loginwarning.setText('username or password is wrong')
            if self.wrongpass%3==0:
                self.Loginsubmit.setEnabled(False)
                QTimer.singleShot(6000, lambda: self.Loginsubmit.setEnabled(True))


    def submit_login(self):
        self.check_user_and_pass()

    def forget_password(self, event):
        self.clear_layout(self.loginlayout)
        self.userEmailLabel = QLabel(
            'Enter your username or email:', self.window)
        self.userEmailLine = QLineEdit(self.window)
        self.forgetwarning = QLabel(' ', self.window)
        self.forgetsubmit = QPushButton('Submit', self.window)
        self.forgetsubmit.clicked.connect(self.check_data)
        self.loginlayout.addWidget(self.userEmailLabel, 0, 0)
        self.loginlayout.addWidget(self.userEmailLine, 0, 1)
        self.loginlayout.addWidget(self.forgetsubmit, 1, 1, 1, 1)
        self.loginlayout.addWidget(self.forgetwarning, 2, 1, 1, 1)

    def check_data(self):
        self.window.db.cursor.execute("SELECT user_name,email FROM users WHERE user_name=? OR email=?", (
            self.userEmailLine.text(), self.userEmailLine.text()))
        result = self.window.db.cursor.fetchone()
        if result:
            self.forgetwarning.setText(' ')
            self.forgetsubmit.clicked.disconnect()
            self.questionLabel = QLabel(
                'What is your favorite Car Brand? ', self.window)
            self.questionLine = QLineEdit(self.window)
            self.userEmailLabel.setVisible(False)
            self.userEmailLine.setVisible(False)
            self.forgetsubmit.setVisible(False)
            self.loginlayout.addWidget(self.questionLabel, 0, 0)
            self.loginlayout.addWidget(self.questionLine, 0, 1)
            self.forgetsubmit = QPushButton('Submit', self.window)
            self.forgetsubmit.clicked.connect(self.check_security)
            self.loginlayout.addWidget(self.forgetsubmit, 1, 1)
        else:
            self.forgetwarning.setText('this username/email does not exist')

    def check_security(self):
        self.window.db.cursor.execute(
            "SELECT security_q_answer FROM users WHERE security_q_answer=? ", (self.questionLine.text(),))
        answer = self.window.db.cursor.fetchone()
        if answer:
            self.window.db.cursor.execute("SELECT password FROM users WHERE user_name=? OR email=?", (
                self.userEmailLine.text(), self.userEmailLine.text()))
            password = self.window.db.cursor.fetchone()
            self.forgetwarning.setText(f'your password is: {password[0]}')
        else:
            self.forgetwarning.setText('your security answer was wrong.')

class MainMenu():
    def __init__(self, window: MyWindow):
        self.window=window
        self.show_main_menu()

    def register_income(self):
        self.hide_menu()
        self.registerIncomeMenu=RegisterIncomeMenu(self.window)

    def register_expense(self):
        self.hide_menu()
        self.registerIncomeMenu=RegisterExpenseMenu(self.window)

    def show_categories(self):
        self.hide_menu()
        self.categoryMenu=CategoryMenu(self.window)

    def show_search(self):
        self.hide_menu()
        self.searchMenu=SearchMenu(self.window)

    def show_reporting(self):
        self.hide_menu()
        self.reportMenu=ReportMenu(self.window)

    def show_settings(self):
        self.hide_menu()
        self.settingMenu=SettingMenu(self.window)

    def show_main_menu(self):
        # Welcome label
        self.welcominglabel=QLabel('Welcome to elmos balance.', self.window)
        self.welcominglabel.setGeometry(150, 100, 400, 200)
        self.welcominglabel.show()

        # Register Income button
        self.registerIncomeButton=QPushButton('Register Income', self.window)
        self.registerIncomeButton.setGeometry(100, 250, 200, 50)
        self.registerIncomeButton.clicked.connect(self.register_income)
        self.registerIncomeButton.show()

        # Register Expense button
        self.registerExpenseButton=QPushButton(
            'Register Expense', self.window)
        self.registerExpenseButton.setGeometry(350, 250, 200, 50)
        self.registerExpenseButton.clicked.connect(self.register_expense)
        self.registerExpenseButton.show()

        # Categories button
        self.categoriesButton=QPushButton('Categories', self.window)
        self.categoriesButton.setGeometry(100, 350, 200, 50)
        self.categoriesButton.clicked.connect(self.show_categories)
        self.categoriesButton.show()

        # Search button
        self.searchButton=QPushButton('Search', self.window)
        self.searchButton.setGeometry(350, 350, 200, 50)
        self.searchButton.clicked.connect(self.show_search)
        self.searchButton.show()

        # Reporting button
        self.reportingButton=QPushButton('Reporting', self.window)
        self.reportingButton.setGeometry(100, 450, 200, 50)
        self.reportingButton.clicked.connect(self.show_reporting)
        self.reportingButton.show()

        # Settings button
        self.settingsButton=QPushButton('Settings', self.window)
        self.settingsButton.setGeometry(350, 450, 200, 50)
        self.settingsButton.clicked.connect(self.show_settings)
        self.settingsButton.show()

        # Exit button
        self.exitButton=QPushButton('Exit', self.window)
        self.exitButton.setGeometry(250, 550, 200, 50)
        self.exitButton.clicked.connect(self.exit_app)
        self.exitButton.show()

    def exit_app(self):
        # Implement action for Exit button
        self.window.close()

    def hide_menu(self):
        self.welcominglabel.setVisible(False)
        self.registerIncomeButton.setVisible(False)
        self.registerExpenseButton.setVisible(False)
        self.categoriesButton.setVisible(False)
        self.searchButton.setVisible(False)
        self.reportingButton.setVisible(False)
        self.settingsButton.setVisible(False)
        self.exitButton.setVisible(False)

class RegisterIncomeMenu:
    def __init__(self, window: MyWindow):
        self.window = window
        self.init_ui()

    def init_ui(self):
        self.window.signupLoginMenu.mainMenu.hide_menu()
        central_widget = QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)

        self.amountLabel = QLabel('Enter amount: ', self.window)
        self.amountLineEdit = QLineEdit(self.window)
        self.amountWarning = QLabel(' ', self.window)

        self.dateLabel = QLabel('Enter date (yyyy/mm/dd): ', self.window)
        self.dateLineEdit = QLineEdit(self.window)
        self.dateWarning = QLabel(' ', self.window)

        self.categoryLabel = QLabel('Select category: ', self.window)
        self.categoryComboBox = QComboBox(self.window)
        self.load_income_categories()

        self.descriptionLabel = QLabel('Enter description: ', self.window)
        self.descriptionLineEdit = QLineEdit(self.window)
        self.descriptionWarning = QLabel(' ', self.window)

        self.submitButton = QPushButton('Submit', self.window)
        self.submitButton.clicked.connect(self.submit_income)
        self.backButton = QPushButton('Back', self.window)
        self.backButton.clicked.connect(self.back)

        self.layout.addWidget(self.amountLabel, 0, 0)
        self.layout.addWidget(self.amountLineEdit, 0, 1)
        self.layout.addWidget(self.amountWarning, 0, 2)
        self.layout.addWidget(self.dateLabel, 1, 0)
        self.layout.addWidget(self.dateLineEdit, 1, 1)
        self.layout.addWidget(self.dateWarning, 1, 2)
        self.layout.addWidget(self.categoryLabel, 2, 0)
        self.layout.addWidget(self.categoryComboBox, 2, 1)
        self.layout.addWidget(self.descriptionLabel, 3, 0)
        self.layout.addWidget(self.descriptionLineEdit, 3, 1)
        self.layout.addWidget(self.descriptionWarning, 3, 2)
        self.layout.addWidget(self.submitButton, 4, 0, 1, 3)
        self.layout.addWidget(self.backButton, 5, 0, 1, 3)

    def load_income_categories(self):
        cursor = self.window.db.cursor
        cursor.execute("SELECT name FROM income_categories")
        categories = [row[0] for row in cursor.fetchall()]
        self.categoryComboBox.addItems(categories)

    def submit_income(self):
        amount = self.amountLineEdit.text()
        date = self.dateLineEdit.text()
        category = self.categoryComboBox.currentText()
        description = self.descriptionLineEdit.text()

        try:
            register_fine = RegisterFine(self.window.db)
            register_fine.create_tables()
            register_fine.register_income(float(amount), date, category, description)
            self.descriptionWarning.setText('Income registered successfully')
        except ValueError as e:
            self.descriptionWarning.setText(str(e))

    def back(self):
        self.amountLabel.setVisible(False)
        self.amountLineEdit.setVisible(False)
        self.amountWarning.setVisible(False)
        self.dateLabel.setVisible(False)
        self.dateLineEdit.setVisible(False)
        self.dateWarning.setVisible(False)
        self.categoryLabel.setVisible(False)
        self.categoryComboBox.setVisible(False)
        self.descriptionLabel.setVisible(False)
        self.descriptionLineEdit.setVisible(False)
        self.descriptionWarning.setVisible(False)
        self.submitButton.setVisible(False)
        self.backButton.setVisible(False)
        self.mainMenu = MainMenu(self.window)

class ChangeUserProfile:
    def __init__(self, window: MyWindow):
        self.window = window
        self.change_profile_menu()

    def change_profile_menu(self):
        central_widget = QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)

        # variables for first name
        self.firstNameLabel = QLabel('First Name: ', self.window)
        self.firstNameLine = QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.firstNameLine.setText(
                self.window.signupLoginMenu.user.firstName)
        else:
            self.firstNameLine.setText("")
        self.firstNameLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.firstName if self.window.signupLoginMenu.user else "")

        # variables for last name
        self.lastNameLabel = QLabel('Last Name: ', self.window)
        self.lastNameLine = QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.lastNameLine.setText(
                self.window.signupLoginMenu.user.lastName)
        else:
            self.lastNameLine.setText("")
        self.lastNameLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.lastName if self.window.signupLoginMenu.user else "")

        # variables for phone number
        self.phoneNumberLabel = QLabel('Phone Number: ', self.window)
        self.phoneNumberLine = QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.phoneNumberLine.setText(
                self.window.signupLoginMenu.user.phoneNumber)
        else:
            self.phoneNumberLine.setText("")
        self.phoneNumberLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.phoneNumber if self.window.signupLoginMenu.user else "")

        # variables for password
        self.passwordLabel = QLabel('Password: ', self.window)
        self.passwordLine = QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.passwordLine.setText(
                self.window.signupLoginMenu.user.password)
        else:
            self.passwordLine.setText("")
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.password if self.window.signupLoginMenu.user else "")

        # variables for city
        self.cityLabel = QLabel('City: ', self.window)
        self.cityCombobox = QComboBox(self.window)
        self.cities = ['Karaj',
                       'Ardabil',
                       'Bushehr',
                       'Shahrekord',
                       'Tabriz',
                       'Shiraz',
                       'Rasht',
                       'Gorgan',
                       'Hamadan',
                       'Bandar Abas',
                       'Ilam',
                       'Isfahan',
                       'Kerman',
                       'Kermanshah',
                       'Ahwaz',
                       'Yasuj',
                       'Sanandaj',
                       'Khoramabad',
                       'Arak',
                       'Sari',
                       'Bojnurd',
                       'Qazvin',
                       'Qom',
                       'Mashhad',
                       'Semnan',
                       'Zahedan',
                       'Birjand',
                       'Tehran',
                       'Urmia',
                       'Yazd',
                       'Zanjan']
        self.cityCombobox.addItems(self.cities)
        if self.window.signupLoginMenu.user is not None:
            self.cityCombobox.setCurrentText(
                self.window.signupLoginMenu.user.city)
        else:
            self.cityCombobox.setCurrentText("")
        self.cityCombobox.currentTextChanged.connect(
            lambda text: self.window.signupLoginMenu.user.city if self.window.signupLoginMenu.user else "")

        # variables for email
        self.emailLabel = QLabel('Email: ', self.window)
        self.emailLine = QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.emailLine.setText(self.window.signupLoginMenu.user.email)
        else:
            self.emailLine.setText("")
        self.emailLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.email if self.window.signupLoginMenu.user else "")

        # variables for birth date
        self.dateLabel = QLabel('Birth Date: ', self.window)
        self.dateLine = QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.dateLine.setText(self.window.signupLoginMenu.user.birthDate)
        else:
            self.dateLine.setText("")
        self.dateLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.birthDate if self.window.signupLoginMenu.user else "")

        # submit button
        self.submit = QPushButton('Submit', self.window)
        self.submit.clicked.connect(self.submit_button)

        # back button
        self.back = QPushButton('Back', self.window)
        self.back.clicked.connect(self.back_button)

        # layout
        self.layout.addWidget(self.firstNameLabel, 0, 0)
        self.layout.addWidget(self.firstNameLine, 0, 1)
        self.layout.addWidget(self.lastNameLabel, 1, 0)
        self.layout.addWidget(self.lastNameLine, 1, 1)
        self.layout.addWidget(self.phoneNumberLabel, 2, 0)
        self.layout.addWidget(self.phoneNumberLine, 2, 1)
        self.layout.addWidget(self.passwordLabel, 3, 0)
        self.layout.addWidget(self.passwordLine, 3, 1)
        self.layout.addWidget(self.cityLabel, 4, 0)
        self.layout.addWidget(self.cityCombobox, 4, 1)
        self.layout.addWidget(self.emailLabel, 5, 0)
        self.layout.addWidget(self.emailLine, 5, 1)
        self.layout.addWidget(self.dateLabel, 6, 0)
        self.layout.addWidget(self.dateLine, 6, 1)
        self.layout.addWidget(self.submit, 7, 0, 1, 2)
        self.layout.addWidget(self.back, 8, 0, 1, 2)

    def submit_button(self):
        # implement your logic here to update the user profile
        pass
    
    def back_button(self):
        # implement your logic here to go back to the previous menu
        pass
        def __init__(self, window: MyWindow):
            self.window=window
            self.change_profile_menu()
    
    def change_profile_menu(self):
        central_widget=QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout=QGridLayout(central_widget)
        # variables for first name
        self.firstNameLabel=QLabel('First Name: ', self.window)
        self.firstNameLine=QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.firstNameLine.setText(
                self.window.signupLoginMenu.user.firstName)
        else:
            self.firstNameLine.setText("")
        self.firstNameLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.firstName if self.window.signupLoginMenu.user else "")

# variables for last name
        self.lastNameLabel=QLabel('Last Name: ', self.window)
        self.lastNameLine=QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.lastNameLine.setText(
                self.window.signupLoginMenu.user.lastName)
        else:
            self.lastNameLine.setText("")
        self.lastNameLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.lastName if self.window.signupLoginMenu.user else "")

# variables for phone number
        self.phoneNumberLabel=QLabel('Phone Number: ', self.window)
        self.phoneNumberLine=QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.phoneNumberLine.setText(
                self.window.signupLoginMenu.user.phoneNumber)
        else:
            self.phoneNumberLine.setText("")
        self.phoneNumberLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.phoneNumber if self.window.signupLoginMenu.user else "")

# variables for password
        self.passwordLabel=QLabel('Password: ', self.window)
        self.passwordLine=QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.passwordLine.setText(
                self.window.signupLoginMenu.user.password)
        else:
            self.passwordLine.setText("")
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.password if self.window.signupLoginMenu.user else "")

        # variables for city
        self.cityLabel=QLabel('City: ', self.window)
        self.cityCombobox=QComboBox(self.window)
        self.cities=['Karaj',
                       'Ardabil',
                       'Bushehr',
                       'Shahrekord',
                       'Tabriz',
                       'Shiraz',
                       'Rasht',
                       'Gorgan',
                       'Hamadan',
                       'Bandar Abas',
                       'Ilam',
                       'Isfahan',
                       'Kerman',
                       'Kermanshah',
                       'Ahwaz',
                       'Yasuj',
                       'Sanandaj',
                       'Khoramabad',
                       'Arak',
                       'Sari',
                       'Bojnurd',
                       'Qazvin',
                       'Qom',
                       'Mashhad',
                       'Semnan',
                       'Zahedan',
                       'Birjand',
                       'Tehran',
                       'Urmia',
                       'Yazd',
                       'Zanjan']
        self.cityCombobox.addItems(self.cities)
        if self.window.signupLoginMenu.user is not None:
            self.cityCombobox.setCurrentText(
                self.window.signupLoginMenu.user.city)
        else:
            self.cityCombobox.setCurrentText("")
        self.cityCombobox.currentTextChanged.connect(
            lambda text: self.window.signupLoginMenu.user.city if self.window.signupLoginMenu.user else "")

        # variables for email
        self.emailLabel=QLabel('Email: ', self.window)
        self.emailLine=QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.emailLine.setText(self.window.signupLoginMenu.user.email)
        else:
            self.emailLine.setText("")
        self.emailLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.email if self.window.signupLoginMenu.user else "")

        # variables for birth date
        self.dateLabel=QLabel('Birth Date: ', self.window)
        self.dateLine=QLineEdit(self.window)
        if self.window.signupLoginMenu.user is not None:
            self.dateLine.setText(self.window.signupLoginMenu.user.birthDate)
        else:
            self.dateLine.setText("")
        self.dateLine.textChanged.connect(
            lambda text: self.window.signupLoginMenu.user.birthDate if self.window.signupLoginMenu.user else "")
        # submit button
        self.submit=QPushButton('Submit', self.window)
        self.submit.clicked.connect(self.submit_button)
        # back button
        self.back=QPushButton('Back', self.window)
        self.back.clicked.connect(self.back_button)
        # layout
        self.layout.addWidget(self.firstNameLabel, 0, 0)
        self.layout.addWidget(self.firstNameLine, 0, 1)
        self.layout.addWidget(self.lastNameLabel, 1, 0)
        self.layout.addWidget(self.lastNameLine, 1, 1)
        self.layout.addWidget(self.phoneNumberLabel, 2, 0)
        self.layout.addWidget(self.phoneNumberLine, 2, 1)
        self.layout.addWidget(self.passwordLabel, 3, 0)
        self.layout.addWidget(self.passwordLine, 3, 1)
        self.layout.addWidget(self.cityLabel, 4, 0)
        self.layout.addWidget(self.cityCombobox, 4, 1)
        self.layout.addWidget(self.emailLabel, 5, 0)
        self.layout.addWidget(self.emailLine, 5, 1)
        self.layout.addWidget(self.dateLabel, 6, 0)
        self.layout.addWidget(self.dateLine, 6, 1)
        self.layout.addWidget(self.submit, 7, 0, 1, 2)
        self.layout.addWidget(self.back, 8, 0, 1, 2)

    def submit_button(self):
        # implement your logic here to update the user profile
        pass

    def back_button(self):
        self.firstNameLabel.setVisible(False)
        self.firstNameLine.setVisible(False)
        self.lastNameLabel.setVisible(False)
        self.lastNameLine.setVisible(False)
        self.phoneNumberLabel.setVisible(False)
        self.phoneNumberLine.setVisible(False)
        self.passwordLabel.setVisible(False)
        self.passwordLine.setVisible(False)
        self.cityLabel.setVisible(False)
        self.cityCombobox.setVisible(False)
        self.emailLabel.setVisible(False)
        self.emailLine.setVisible(False)
        self.dateLabel.setVisible(False)
        self.dateLine.setVisible(False)
        self.submit.setVisible(False)
        self.back.setVisible(False)
        self.settingMenu=SettingMenu(self.window)

class CategoryMenu:
    def __init__(self, window: MyWindow):
        self.window=window
        self.init_ui()

    def init_ui(self):
        self.window.signupLoginMenu.mainMenu.hide_menu()
        central_widget=QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout=QGridLayout(central_widget)

        self.categoryTypeLabel=QLabel('Select category type: ', self.window)
        self.categoryTypeComboBox=QComboBox(self.window)
        self.categoryTypeComboBox.addItems(['Income', 'Expense'])

        self.categoryNameLabel=QLabel('Enter category name: ', self.window)
        self.categoryNameLineEdit=QLineEdit(self.window)
        self.categoryNameWarning=QLabel(' ', self.window)

        self.submitButton=QPushButton('Submit', self.window)
        self.submitButton.clicked.connect(self.submit_category)
        self.backButton=QPushButton('Back', self.window)
        self.backButton.clicked.connect(self.back)

        self.layout.addWidget(self.categoryTypeLabel, 0, 0)
        self.layout.addWidget(self.categoryTypeComboBox, 0, 1)
        self.layout.addWidget(self.categoryNameLabel, 1, 0)
        self.layout.addWidget(self.categoryNameLineEdit, 1, 1)
        self.layout.addWidget(self.categoryNameWarning, 1, 2)
        self.layout.addWidget(self.submitButton, 2, 0, 1, 3)
        self.layout.addWidget(self.backButton, 3, 0, 1, 3)

    def submit_category(self):
        category_type=self.categoryTypeComboBox.currentText().lower() + '_categories'
        category_name=self.categoryNameLineEdit.text()
        category=Category(category_name)

        try:
            category.validate_name()
            category.save_to_database(self.window.db, category_type)
            self.categoryNameWarning.setText('Category added successfully')
        except ValueError as e:
            self.categoryNameWarning.setText(str(e))

    def back(self):
        self.categoryNameLabel.setVisible(False)
        self.categoryNameLineEdit.setVisible(False)
        self.categoryNameWarning.setVisible(False)
        self.categoryTypeComboBox.setVisible(False)
        self.categoryTypeLabel.setVisible(False)
        self.submitButton.setVisible(False)
        self.backButton.setVisible(False)
        self.mainMenu=MainMenu(self.window)

class SearchMenu:
    def __init__(self, window: MyWindow):
        self.window=window
        self.init_ui()

    def init_ui(self):
        self.window.signupLoginMenu.mainMenu.hide_menu()
        central_widget=QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout=QGridLayout(central_widget)

        button_group=QButtonGroup()
        self.searchLabel=QLabel('Type for search: ', self.window)
        self.searchLine=QLineEdit(self.window)
        self.filterLabel=QLabel('filters: ', self.window)

        self.dayfilter=QRadioButton('day:', self.window)
        self.dayLine=QLineEdit(self.window)
        self.dayLine.setVisible(False)
        self.dayfilter.setAutoExclusive(False)
        button_group.addButton(self.dayfilter)
        self.dayfilter.toggled.connect(
            lambda checked: self.dayLine.setVisible(checked))

        self.monthfilter=QRadioButton('month:', self.window)
        self.monthLine=QLineEdit(self.window)
        self.monthLine.setVisible(False)
        self.monthfilter.setAutoExclusive(False)
        button_group.addButton(self.monthfilter)
        self.monthfilter.toggled.connect(
            lambda checked: self.monthLine.setVisible(checked))

        self.yearfilter=QRadioButton('year:', self.window)
        self.yearLine=QLineEdit(self.window)
        self.yearLine.setVisible(False)
        self.yearfilter.setAutoExclusive(False)
        button_group.addButton(self.yearfilter)
        self.yearfilter.toggled.connect(
            lambda checked: self.yearLine.setVisible(checked))

        self.incomeExpensefilter=QRadioButton('type: ', self.window)
        self.incomeExpenseCombo=QComboBox(self.window)
        self.incomeExpenseCombo.setVisible(False)
        self.incomeExpenseCombo.addItem('income')
        self.incomeExpenseCombo.addItem('expense')
        self.incomeExpenseCombo.addItem('both')
        self.incomeExpensefilter.setAutoExclusive(False)
        button_group.addButton(self.incomeExpensefilter)
        self.incomeExpensefilter.toggled.connect(
            lambda checked: self.incomeExpenseCombo.setVisible(checked))

        self.moneyrangefilter=QRadioButton(
            'value range(type two number seperated by space: )', self.window)
        self.moneyrangeline=QLineEdit(self.window)
        self.moneyrangeline.setVisible(False)
        self.moneyrangefilter.setAutoExclusive(False)
        button_group.addButton(self.moneyrangefilter)
        self.moneyrangefilter.toggled.connect(
            lambda checked: self.moneyrangeline.setVisible(checked))

        self.searchinfilter=QRadioButton(
            'choose the one you want to search in: ', self.window)
        self.searchinCombo=QComboBox(self.window)
        self.searchinCombo.addItem('descriptions')
        self.searchinCombo.addItem('categories')
        self.searchinCombo.addItem('both')
        self.searchinLine=QLineEdit(self.window)
        self.searchinCombo.setVisible(False)
        self.searchinLine.setVisible(False)
        self.searchinfilter.setAutoExclusive(False)
        button_group.addButton(self.searchinfilter)
        self.searchinfilter.toggled.connect(
            lambda checked: self.searchinCombo.setVisible(checked))
        self.searchinCombo.currentTextChanged.connect(self.searchin_func)

        self.submitButton=QPushButton('Submit', self.window)
        self.submitButton.clicked.connect(self.show_search_results)
        self.backButton=QPushButton('Back', self.window)
        self.backButton.clicked.connect(self.back)

        self.layout.addWidget(self.searchLabel,0,0)
        self.layout.addWidget(self.searchLine,0,1)
        self.layout.addWidget(self.filterLabel,1,0)
        self.layout.addWidget(self.dayfilter,2,0)
        self.layout.addWidget(self.dayLine,2,1)
        self.layout.addWidget(self.monthfilter,3,0)
        self.layout.addWidget(self.monthLine,3,1)
        self.layout.addWidget(self.yearfilter,4,0)
        self.layout.addWidget(self.yearLine,4,1)
        self.layout.addWidget(self.incomeExpensefilter,5,0)
        self.layout.addWidget(self.incomeExpenseCombo,5,1)
        self.layout.addWidget(self.moneyrangefilter,6,0)
        self.layout.addWidget(self.moneyrangeline,6,1)
        self.layout.addWidget(self.searchinfilter,7,0)
        self.layout.addWidget(self.searchinCombo,7,1)
        self.layout.addWidget(self.searchinLine,7,2)
        self.layout.addWidget(self.submitButton,8,0)
        self.layout.addWidget(self.backButton,8,1)
        self.model = QStandardItemModel(self.window)
        self.table = QTableView(self.window)
        self.table.setModel(self.model)

        self.layout.addWidget(self.table, 9, 0, 1, 2)
        self.table.hide()
    def searchin_func(self):
        if self.searchinCombo.isVisible():
            self.searchinLine.setVisible(True)
        else:
            self.searchinLine.setVisible(False)

    def show_search_results(self):
        self.searchengine=Search(self)
        self.searchengine.search(self.window.db)
    def back(self):
        self.searchLabel.setVisible(False)
        self.searchLine.setVisible(False)
        self.filterLabel.setVisible(False)
        self.dayfilter.setVisible(False)
        self.dayLine.setVisible(False)
        self.monthfilter.setVisible(False)
        self.monthLine.setVisible(False)
        self.yearfilter.setVisible(False)
        self.yearLine.setVisible(False)
        self.incomeExpensefilter.setVisible(False)
        self.incomeExpenseCombo.setVisible(False)
        self.moneyrangefilter.setVisible(False)
        self.moneyrangeline.setVisible(False)
        self.searchinfilter.setVisible(False)
        self.searchinCombo.setVisible(False)
        self.searchinLine.setVisible(False)
        self.submitButton.setVisible(False)
        self.backButton.setVisible(False)
        self.table.setVisible(False)
        self.mainMenu = MainMenu(self.window)
    def get_filters(self):
        self.day = self.dayLine.text()
        self.month = self.monthLine.text()
        self.year = self.yearLine.text()
        self.incomeExpense = self.incomeExpenseCombo.currentText()
        self.moneyrange = self.moneyrangeline.text()
        self.searchin= self.searchinLine.text()
        return [self.day,self.month,self.year,self.incomeExpense,self.moneyrange,self.searchin]

class ReportMenu:
    def __init__(self, window: MyWindow):
        self.window=window
        self.init_ui()

    def init_ui(self):
        self.window.signupLoginMenu.mainMenu.hide_menu()
        central_widget=QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout=QGridLayout(central_widget)
        button_group=QButtonGroup()

        self.reportLabel=QLabel(
            'choose the items below to specify your report.', self.window)
        self.dayfilter=QRadioButton('day:', self.window)
        self.dayLine=QLineEdit(self.window)
        self.dayLine.setVisible(False)
        self.dayfilter.setAutoExclusive(False)
        button_group.addButton(self.dayfilter)
        self.dayfilter.toggled.connect(
            lambda checked: self.dayLine.setVisible(checked))

        self.monthfilter=QRadioButton('month:', self.window)
        self.monthLine=QLineEdit(self.window)
        self.monthLine.setVisible(False)
        self.monthfilter.setAutoExclusive(False)
        button_group.addButton(self.monthfilter)
        self.monthfilter.toggled.connect(
            lambda checked: self.monthLine.setVisible(checked))

        self.yearfilter=QRadioButton('year:', self.window)
        self.yearLine=QLineEdit(self.window)
        self.yearLine.setVisible(False)
        self.yearfilter.setAutoExclusive(False)
        button_group.addButton(self.yearfilter)
        self.yearfilter.toggled.connect(
            lambda checked: self.yearLine.setVisible(checked))

        self.incomeExpensefilter=QRadioButton('type: ', self.window)
        self.incomeExpenseCombo=QComboBox(self.window)
        self.incomeExpenseCombo.setVisible(False)
        self.incomeExpenseCombo.addItem('income')
        self.incomeExpenseCombo.addItem('expense')
        self.incomeExpenseCombo.addItem('both')
        self.incomeExpensefilter.setAutoExclusive(False)
        button_group.addButton(self.incomeExpensefilter)
        self.incomeExpensefilter.toggled.connect(lambda checked: self.incomeExpenseCombo.setVisible(checked))

        self.moneyrangefilter=QRadioButton('value range(type two number seperated by space: )',self.window)
        self.moneyrangeline=QLineEdit(self.window)
        self.moneyrangeline.setVisible(False)
        self.moneyrangefilter.setAutoExclusive(False)
        button_group.addButton(self.moneyrangefilter)
        self.moneyrangefilter.toggled.connect(lambda checked: self.moneyrangeline.setVisible(checked))

        self.categoryfilter=QRadioButton('please choose the category you want to search in: ',self.window)
        self.categoryline=QLineEdit(self.window)
        self.categoryline.setVisible(False)
        self.categoryfilter.setAutoExclusive(False)
        button_group.addButton(self.categoryfilter)
        self.categoryfilter.toggled.connect(lambda checked: self.categoryline.setVisible(checked))

        self.submitButton = QPushButton('Submit', self.window)
        self.submitButton.clicked.connect(self.show_search_results)
        self.backButton = QPushButton('Back', self.window)
        self.backButton.clicked.connect(self.back)

        self.layout.addWidget(self.reportLabel,0,0)
        self.layout.addWidget(self.dayfilter,1,0)
        self.layout.addWidget(self.dayLine,1,1)
        self.layout.addWidget(self.monthfilter,2,0)
        self.layout.addWidget(self.monthLine,2,1)
        self.layout.addWidget(self.yearfilter,3,0)
        self.layout.addWidget(self.yearLine,3,1)
        self.layout.addWidget(self.incomeExpensefilter,4,0)
        self.layout.addWidget(self.incomeExpenseCombo,4,1)
        self.layout.addWidget(self.moneyrangefilter,5,0)
        self.layout.addWidget(self.moneyrangeline,5,1)
        self.layout.addWidget(self.categoryfilter,6,0)
        self.layout.addWidget(self.categoryline,6,1)
        self.layout.addWidget(self.submitButton,7,0)
        self.layout.addWidget(self.backButton,7,1)
        self.model = QStandardItemModel(self.window)
        self.table = QTableView(self.window)
        self.table.setModel(self.model)

        self.layout.addWidget(self.table, 8, 0, 1, 2)
        self.table.hide()
    def back(self):
        self.reportLabel.setVisible(False)
        self.dayfilter.setVisible(False)
        self.dayLine.setVisible(False)
        self.monthfilter.setVisible(False)
        self.monthLine.setVisible(False)
        self.yearfilter.setVisible(False)
        self.yearLine.setVisible(False)
        self.incomeExpensefilter.setVisible(False)
        self.incomeExpenseCombo.setVisible(False)
        self.moneyrangefilter.setVisible(False)
        self.moneyrangeline.setVisible(False)
        self.categoryfilter.setVisible(False)
        self.categoryline.setVisible(False)
        self.submitButton.setVisible(False)
        self.backButton.setVisible(False)
        self.table.setVisible(False)
        self.mainMenu = MainMenu(self.window)
    def show_search_results(self):
        self.reportEngine=Report(self)
        self.reportEngine.search(self.window.db)
    def get_filters(self):
        self.day = self.dayLine.text()
        self.month = self.monthLine.text()
        self.year = self.yearLine.text()
        self.incomeExpense = self.incomeExpenseCombo.currentText()
        self.moneyrange = self.moneyrangeline.text()
        self.searchin= self.categoryline.text()
        return [self.day,self.month,self.year,self.incomeExpense,self.moneyrange,self.searchin]

class SettingMenu:
    def __init__(self, window: MyWindow):
        self.window = window
        self.init_ui()

    def init_ui(self):
        self.window.signupLoginMenu.mainMenu.hide_menu()
        self.central_widget = QWidget(self.window)
        self.window.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.changeUserProfileButton = QPushButton(
            "Change user profile", self.window)
        self.changeUserProfileButton.clicked.connect(self.change_user_profile)
        self.layout.addWidget(self.changeUserProfileButton)

        self.deleteUserProfileButton = QPushButton(
            "Delete user Profile", self.window)
        self.deleteUserProfileButton.clicked.connect(self.delete_user_profile)
        self.layout.addWidget(self.deleteUserProfileButton)

        self.deleteIncomesButton = QPushButton("Delete incomes", self.window)
        self.deleteIncomesButton.clicked.connect(self.delete_incomes)
        self.layout.addWidget(self.deleteIncomesButton)

        self.deleteExpensesButton = QPushButton("Delete expenses", self.window)
        self.deleteExpensesButton.clicked.connect(self.delete_expenses)
        self.layout.addWidget(self.deleteExpensesButton)

        self.mainMenuButton = QPushButton("Main menu", self.window)
        self.mainMenuButton.clicked.connect(self.back)
        self.layout.addWidget(self.mainMenuButton)

        # Set the geometry for the central widget
        self.central_widget.setGeometry(100, 100, 300, 200)
        self.window.show()  # Show the window

    def change_user_profile(self):
        self.profile = ChangeUserProfile(self.window)
        # implement changing user profile logic here
        pass

    def delete_user_profile(self):
        # implement deleting user profile logic here
        pass

    def delete_incomes(self):
        # implement deleting incomes logic here
        pass

    def delete_expenses(self):
        # implement deleting expenses logic here
        pass

    def back(self):
        self.changeUserProfileButton.setVisible(False)
        self.deleteUserProfileButton.setVisible(False)
        self.deleteIncomesButton.setVisible(False)
        self.deleteExpensesButton.setVisible(False)
        self.mainMenuButton.setVisible(False)
        self.mainMenu = MainMenu(self.window)

class RegisterExpenseMenu:
    def __init__(self, window: MyWindow):
        self.window = window
        self.init_ui()

    def init_ui(self):
        self.window.signupLoginMenu.mainMenu.hide_menu()
        central_widget = QWidget(self.window)
        self.window.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)

        self.amountLabel = QLabel('Enter amount: ', self.window)
        self.amountLineEdit = QLineEdit(self.window)
        self.amountWarning = QLabel(' ', self.window)

        self.dateLabel = QLabel('Enter date (yyyy/mm/dd): ', self.window)
        self.dateLineEdit = QLineEdit(self.window)
        self.dateWarning = QLabel(' ', self.window)

        self.categoryLabel = QLabel('Select category: ', self.window)
        self.categoryComboBox = QComboBox(self.window)
        self.load_expense_categories()

        self.descriptionLabel = QLabel('Enter description: ', self.window)
        self.descriptionLineEdit = QLineEdit(self.window)
        self.descriptionWarning = QLabel(' ', self.window)

        self.submitButton = QPushButton('Submit', self.window)
        self.submitButton.clicked.connect(self.submit_expense)
        self.backButton = QPushButton('Back', self.window)
        self.backButton.clicked.connect(self.back)

        self.layout.addWidget(self.amountLabel, 0, 0)
        self.layout.addWidget(self.amountLineEdit, 0, 1)
        self.layout.addWidget(self.amountWarning, 0, 2)
        self.layout.addWidget(self.dateLabel, 1, 0)
        self.layout.addWidget(self.dateLineEdit, 1, 1)
        self.layout.addWidget(self.dateWarning, 1, 2)
        self.layout.addWidget(self.categoryLabel, 2, 0)
        self.layout.addWidget(self.categoryComboBox, 2, 1)
        self.layout.addWidget(self.descriptionLabel, 3, 0)
        self.layout.addWidget(self.descriptionLineEdit, 3, 1)
        self.layout.addWidget(self.descriptionWarning, 3, 2)
        self.layout.addWidget(self.submitButton, 4, 0, 1, 3)
        self.layout.addWidget(self.backButton, 5, 0, 1, 3)

    def load_expense_categories(self):
        cursor = self.window.db.cursor
        cursor.execute("SELECT name FROM expense_categories")
        categories = [row[0] for row in cursor.fetchall()]
        self.categoryComboBox.addItems(categories)

    def submit_expense(self):
        amount = self.amountLineEdit.text()
        date = self.dateLineEdit.text()
        category = self.categoryComboBox.currentText()
        description = self.descriptionLineEdit.text()

        try:
            register_fine = RegisterFine(self.window.db)
            register_fine.create_tables()
            if self.window.signupLoginMenu.logining:
                register_fine.register_income(float(
                    amount), date, category, description, self.window.signupLoginMenu.usernamelogin)
            elif self.window.signupLoginMenu.singuping:
                register_fine.register_income(float(
                    amount), date, category, description, self.window.signupLoginMenu.user.userName)
            self.descriptionWarning.setText('Expense registered successfully')
        except ValueError as e:
            self.descriptionWarning.setText(str(e))

    def back(self):
        self.amountLabel.setVisible(False)
        self.amountLineEdit.setVisible(False)
        self.amountWarning.setVisible(False)
        self.dateLabel.setVisible(False)
        self.dateLineEdit.setVisible(False)
        self.dateWarning.setVisible(False)
        self.categoryLabel.setVisible(False)
        self.categoryComboBox.setVisible(False)
        self.descriptionLabel.setVisible(False)
        self.descriptionLineEdit.setVisible(False)
        self.descriptionWarning.setVisible(False)
        self.submitButton.setVisible(False)
        self.backButton.setVisible(False)
        self.mainMenu = MainMenu(self.window)
