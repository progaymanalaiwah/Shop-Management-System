#_*_ coding:utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.login import *
from classes.class_mainWindow import *
from classes.class_resetPassword import *
from classes.class_resetPassword import *
from connect import connect
import hashlib

class login(QWidget,Ui_login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(420,150)
        self.mainWindow = mainWindow() #Object Of Class mainWindow
        self.fileJson = 'Settings.Conf'

        """Event Button"""
        self.btnClose.clicked.connect(self.close)     #btn Close Form
        self.btnLogin.clicked.connect(self.loginUser) #btn login User
        self.labReturnPass.mousePressEvent = self.showResetPassowrd
        """Start Center Secreen"""
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())




    """Function Check Value Input User """
    def checkValueLinEdit(self):
        username = str(self.linEditUser.text()).replace(" ","")
        password = str(self.lineEditPassword.text()).replace(" ","")
        if username.isspace() == True or password.isspace() == True:
            QMessageBox.critical(self,'تسجيل الدخول'.decode('UTF-8'),'اسم المستخدم او كلمة المرور  يجب ان لا يحتوي على فرغات   '.decode('UTF-8'))
            return False
        elif not username or not password:
            QMessageBox.critical(self,'تسجيل الدخول'.decode('UTF-8'),'اسم المستخدم او كلمة المرور  يجب ان لا يكون فارغ '.decode('UTF-8'))
            return False
        elif len(username) > 20 or len(password) > 20:
            QMessageBox.critical(self,'تسجيل الدخول'.decode('UTF-8'),'اسم المستخدم او كلمة المرور  يجب ان لا يكون\n طوله اكبر من 20 حرف '.decode('UTF-8'))
            return False
        else:
            return True


    """Function Login User"""
    def loginUser(self):
        username = str(self.linEditUser.text()).replace(" ","")
        password = hashlib.md5(str(self.lineEditPassword.text()).replace(" ","")).hexdigest()
        checkValue = self.checkValueLinEdit() #Funciton Check Value Input User
        if checkValue == True:
            con = connect()
            where = '`Username` = "{0}" AND `Password` = "{1}" AND `Active`= 0 '.format(username,password)
            result = con.select('*','User',where,1)
            if result == True: # if username and password Content In Database SHow Main Window
                UserInfo = con.select('*', 'User', where, 2)
                contentMenu = \
                    {
                    1:self.mainWindow.mainSales,2:self.mainWindow.menuChat,3:self.mainWindow.menuSettingAll,
                    11:self.mainWindow.managmentSection,12:self.mainWindow.SettingStor,201:self.mainWindow.menu2,
                    21:self.mainWindow.addItem,22:self.mainWindow.manegmentItem,23:self.mainWindow.manegmentCategory,203:self.mainWindow.menu3,
                    31:self.mainWindow.SettingCustomers,204:self.mainWindow.menu4,
                    41:self.mainWindow.SettingEmployes,205:self.mainWindow.menu5,
                    51:self.mainWindow.menuAddUser,52:self.mainWindow.menuViewUser,206:self.mainWindow.menu6
                    }
                NumberMenu = [1,2,3,11,12,201,21,22,23,203,31,204,41,205,51,52,206]
                for i in NumberMenu:
                    if i >= 200:contentMenu[i].setTitle('')
                    else:contentMenu[i].setVisible(False)

                UserID = UserInfo[0]
                Username = UserInfo[2]
                per    = str(UserInfo[7]).split(",")
                with open(self.fileJson, 'r') as file:
                    Settings = json.load(file)
                Settings['Settings']['Info']['Username'] = Username
                with open(self.fileJson, 'w') as f:
                    f.write(json.dumps(Settings, ensure_ascii=False))

                for i in per:
                    i = int(i)
                    if i == 201:contentMenu[i].setTitle('الاقسام'.decode())
                    elif i == 201:contentMenu[i].setTitle('الاقسام'.decode())
                    elif i == 203:contentMenu[i].setTitle('المواد'.decode())
                    elif i == 204:contentMenu[i].setTitle('العملاء'.decode())
                    elif i == 205:contentMenu[i].setTitle('الموظفين'.decode())
                    elif i == 206:contentMenu[i].setTitle('المستخدمين'.decode())
                    else:contentMenu[i].setVisible(True)
                self.close()
                self.mainWindow.labUserID.setText(str(UserID))
                print(self.mainWindow.labUserID.text())
                self.mainWindow.showMaximized()
            else:
                QMessageBox.critical(self,'تسجيل الدخول'.decode('UTF-8'),'اسم المستخدم او كلمة الذي \n ادخلته غير صحيح'.decode('UTF-8'))





    def showResetPassowrd(self,e):
        self.resetPassword = resetPassword()
        self.close()
        self.resetPassword.show()
