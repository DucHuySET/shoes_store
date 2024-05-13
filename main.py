import sys
sys.path.append(".\lib\core")

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from lib.modules.login.view.login_screen import LoginScreen
from app_controller import AppController


def main():
    appController = AppController()
    app = QApplication(sys.argv)

    stackScr = QStackedWidget()
    login = LoginScreen(stackScr)
    stackScr.addWidget(login)
    

    appScr = QMainWindow()
    appScr.setWindowTitle("Shoes Shop Manager")
    appScr.setCentralWidget(stackScr)
    appScr.showMaximized()

    sys.exit(app.exec_())

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
if __name__ == "__main__":
    main()