#_*_ coding:utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.resetPassword import *
from connect import *
import hashlib,string,random
import xml.etree.ElementTree as EL
import smtplib,json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class resetPassword(QWidget,Ui_resetPassword):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.btnOkRestPassword.setVisible(False)
        self.textCheckPassword.setVisible(False)
        self.textaddCode.setVisible(False)
        self.textNewPasword.setVisible(False)
        self.btnCheckCode.setVisible(False)
        self.textNewPasword.setEchoMode(QLineEdit.Password)
        self.textCheckPassword.setEchoMode(QLineEdit.Password)
        self.con = connect()
        self.btnLoginReset.clicked.connect(self.ShowFormLogin)
        self.btnReset.clicked.connect(self.checkInfoUser)
        self.btnOkRestPassword.clicked.connect(self.resetPsswordUser)
        self.btnCheckCode.clicked.connect(self.CheckCode)


    def ShowFormLogin(self):
        import classes.class_login as login
        log = login.login()
        log.show()
        self.close()

    def checkInfoUser(self):
        self.setEnabled(False)
        self.setCursor(Qt.ForbiddenCursor)
        Username = str(self.textUsername.text())
        Email    = str(self.textEmail.text())
        NumberID = str(self.textNumberID.text())
        if not Username or not Email or not NumberID:
            QMessageBox.critical(self,'استعادت كلمة المرور'.decode(),'الرجاء ملء جميع الحقول '.decode())
            self.setEnabled(True)
        else:
            self.UserID = self.con.select("UserID","user","Username = '{0}' AND Email = '{1}' AND NumberID = '{2}'".format(Username,Email,NumberID),1)
            print self.UserID
            if self.UserID > 0:
            	with open('Settings.Conf') as f:
            		jsonData = json.load(f)

                Email = jsonData["Settings"]['InfoEmail']['Email']
                pwd   = jsonData["Settings"]['InfoEmail']['Password']
                emailUser = str(self.textEmail.text())
                Code =  str(self.CreateCode())

                msg = MIMEMultipart()
                msg['Subject'] = "Password recovery"
                msg['From'] = Email
                msg['To'] = emailUser
                html = """\
                <html>
                  <head></head>
                  <body>
                    <h3>Hi This Is Password recovery code</h3>

                     <strong style='display:block;color:#1abc9c;padding:10px; background:#ddd;border:1px solid #ccc'>{0}</strong>
                  </body>
                </html>
                """.format(Code)
                part = MIMEText(html, 'html')
                msg.attach(part)
                try:
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                except:
                    QMessageBox.information(self, 'استعادت كلمة المرور'.decode(),
                                            'الاتصال بل الانترنت غير متوفر الرجاء التحقق من الاتصال '.decode())
                    self.setEnabled(True)
                    self.setCursor(Qt.ArrowCursor)
                    return False
                s.starttls()
                try:
                	s.login(Email, pwd)
            	except:
	                QMessageBox.critical(self, 'استعادت كلمة المرور'.decode(),'اميل الشركه غير صالح الرجاء التحقق من الاميل'.decode())
                        self.setEnabled(True)
                        self.setCursor(Qt.ArrowCursor)
                        return False


                s.sendmail(Email,emailUser, msg.as_string())
                sendOk = s.quit()
                if sendOk:
                    up = self.con.update('user','CodeResetPassword = "{}"'.format(Code),'Username = "{0}"'.format(str(self.textUsername.text())))
                    if up:
                        QMessageBox.information(self,'ارستعادت كلمة المرور'.decode(),'تم ارسال كود التحقق الي البريد الالكتروني'.decode())
                    else:
                        QMessageBox.critical(self,'استعادت كلمة المرور'.decode(),'حذث مشكله الرجاء المحاوله في وقت اخر'.decode())
                        self.close()
                self.btnReset.setVisible(False)
                self.textEmail.setVisible(False)
                self.textUsername.setVisible(False)
                self.textNumberID.setVisible(False)
                self.btnOkRestPassword.setVisible(False)
                self.btnCheckCode.setVisible(True)
                self.textCheckPassword.setVisible(True)
                self.textNewPasword.setVisible(True)
                self.textaddCode.setVisible(True)
            else:
                QMessageBox.critical(self, 'اتسعادت كلمة المرور'.decode(), ' المعلومات التي ادخلنها غير صحيحه'.decode())
            self.setEnabled(True)
            self.setCursor(Qt.ArrowCursor)

    def CheckCode(self):
        username = self.textUsername.text()
        Code     = self.con.select('CodeResetPassword','user','Username = "{0}"'.format(username))[0][0]
        print Code
        textCode = self.textaddCode.text()
        if Code == textCode:
            QMessageBox.information(self,'تغير كلمة السر'.decode(),'الكود الذي ادخلته صحيح يمكنك تغير كلمة السر'.decode())
            self.textaddCode.setEnabled(False)
            self.btnCheckCode.setVisible(False)
            self.btnOkRestPassword.setVisible(True)
            self.textNewPasword.setEnabled(True)
            self.textCheckPassword.setEnabled(True)
        else:
            QMessageBox.critical(self,'تغير كلمة السر'.decode(),'ان الكود الذي اتخلته غير مطابق'.decode())






    def CreateCode(self):
        lenght = random.randrange(10,20)
        Code = string.ascii_uppercase + string.digits + string.ascii_lowercase + '#@!'
        CodeRandom = "".join(random.choice(Code) for i in range(lenght))
        return  CodeRandom

    def resetPsswordUser(self):
        NewPssword =  str(self.textNewPasword.text())
        CheckPassword = self.textCheckPassword.text()
        HashPass = hashlib.md5(NewPssword).hexdigest()
        if not NewPssword or not CheckPassword:
            QMessageBox.critical(self, 'اتسعادت كلمة المرور'.decode(), 'الرجاء ملء جميع الحقول '.decode())
        elif NewPssword != CheckPassword:
            QMessageBox.critical(self, 'استعادت كلمة المرور'.decode(), 'كلمت المرور غير متطابقه '.decode())

        else:
           RestPass =  self.con.update('user',"Password = '{0}'".format(HashPass),"UserID = '{0}'".format(self.UserID))
           if RestPass:
               QMessageBox.information(self, 'استعادت كلمة المرور'.decode(), 'تم تغير كلمة المرور بنجاح'.decode())
               self.close()
               import classes.class_login as login
               log = login.login()
               log.show()

