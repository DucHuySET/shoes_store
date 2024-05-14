import sys
sys.path.append('.\\lib\modules\login\controller')
sys.path.append('.\\lib\modules\login\\view')
sys.path.append('.\\lib\modules\home\\view')
sys.path.append(".\\lib\core")
from login_controller import LoginController as controller
from login_view import Ui_LoginView as view
from PyQt5.QtWidgets import QMainWindow

from home_screen import HomeScreen
from app_controller import AppController

class LoginScreen(QMainWindow):
    def __init__(self, stackScr):
        super().__init__()
        self.ui = view()
        self.controller = controller()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login)
        self.stackScr = stackScr     
    
    ### Navigation
    def goToHome(self, isAdmin):
        homeScr = HomeScreen(isAdmin, self.stackScr)
        self.stackScr.addWidget(homeScr)
        self.stackScr.setCurrentIndex(self.stackScr.currentIndex()+1)
    def login(self):
        user = self.ui.user_field.text()
        password = self.ui.password_field.text()

        if len(user)==0 or len(password)==0:
            self.ui.error.setText("Please input all fields.")

        else:
            result, self.staff = self.controller.login(user,password)
            if result == True:
                self.goToHome(self.staff.isAdmin)
                appController = AppController()
                appController.user = self.staff
            else:
                self.ui.error.setText("Invalid username or password")
