import sys
from PyQt6.QtWidgets import QApplication
from ui import MyWindow

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()