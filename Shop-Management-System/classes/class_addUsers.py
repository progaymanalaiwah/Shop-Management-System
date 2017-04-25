#_*_ coding:utf8 _*_
from funcClasses.funClassAddUsers import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.addUsers import *
from connect import *
from connectFtp import *

class addUser(QWidget,Ui_Users,funClassAddUser):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.move(200,0)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.textPassword.setEchoMode(QLineEdit.Password)
        self.textPasswordShow.setVisible(False)
        self.labImageName.setVisible(False)
        self.labUserPassword.setVisible(False)
        self.labUserID.setVisible(False)

        self.con = connect()
        self.connectFTP = connectFtp()

        """[ Start Event Function ]"""
        self.labCreatePasswordComplix.mousePressEvent = self.createPasswordComplix
        self.labShowMenuPer.mousePressEvent = self.showMenuPermission
        self.labAddImgUser.mousePressEvent = self.selectImgUser
        self.btnAddUser.clicked.connect(self.addUser)
        self.btnCancel.clicked.connect(self.Cancel)
        self.labShowPassword.mousePressEvent = self.ShowPassword
        self.textPassword.keyReleaseEvent = self.CopyPassword
        self.textPasswordShow.keyReleaseEvent = self.CopyPassword
        self.checkBoxAll.clicked.connect(self.CheckAllPer)
        self.btnSelectUsers.clicked.connect(self.SelectUser)
        self.btnEditUser.clicked.connect(self.EditUser)
        """ [ End Event Function ] """

    def EditUser(self):
        fullName = self.textFullName.text()
        userName = self.textUsername.text()
        email = self.textEmail.text()
        numberID = self.textNumberID.text()
        numberPhone = self.textNumberPhone.text()
        sex = str(self.comboxSex.currentText())
        print sex
        password = self.textPassword.text()
        passHash = hashlib.md5(password).hexdigest()
        passwordOld = str(self.labUserPassword.text())
        imageNameOld = str(self.labImageName.text())
        imageCheck = True
        try:
            numberID = int(numberID);numberIDError = True
        except ValueError:
            numberIDError = False
        try:
            numberPhone = int(numberPhone);numberPhoneError = True
        except ValueError:
            numberPhoneError = False
        try:
            imageUser = self.InfoImage['path']
            extension = self.InfoImage['extension']
            NameImage = imageNameOld.split(".")[0] + "." + extension
        except:
            imageCheck = False
            NameImage = imageNameOld

        checkBoxPermission = {1: self.checkBoxCalc, 2: self.checkBoxChat,3:self.checkBoxSettings,
                              11: self.checkBoxSSection, 12: self.checkBoxSStor, 201: self.checkBoxSection,
                              21: self.checkBoxAddItem, 22: self.checkBoxSItem, 23: self.checkBoxSCatecory,
                              203: self.checkBoxItem,
                              31: self.checkBoxSCust, 204: self.checkBoxCust,
                              41: self.checkBoxSEmployee, 205: self.checkBoxEmployee,
                              51: self.checkBoxAddUser, 52: self.checkBoxViewUser, 206: self.checkBoxUsers}
        NumberPermission = [1, 2,3, 11, 12, 201, 21, 22, 23, 203, 31, 204, 41, 205, 51, 52, 206]
        permission = []
        for checkBox in NumberPermission:
            if checkBoxPermission[checkBox].isChecked():
                permission.append(checkBox)
            elif self.checkBoxAll.isChecked():
                permission = NumberPermission
        permission = ",".join(map(str, permission))
        checkData = self.con.select("Username", "user", "Username = '{}' and UserID != '{}'".format(userName,str(self.labUserID.text())), 1)
        if password == "" or password == " ":
            password = passwordOld
        if not fullName or not numberPhone or not numberID or not userName or not email:
            self.msgShow('تعديل مستخدم', 'الرجاء ملء جميع الحقول فهيه مطلوبه', 3)
        elif sex == 'جنس المستخدم':
            self.msgShow('تعديل مستخدم', 'الرجاء تحديد جنس العميل', 3)
        elif numberIDError == False:
            self.msgShow('تعديل مستخدم', 'الرجاء كتابت الرقم الوطني بطريقه صحيحه', 3)
        elif numberPhoneError == False:
            self.msgShow('تعديل مستخدم', 'الرجاء كتابت الرقم الهاتف بطريقه صحيحه', 3)
        elif  checkData > 0:
            self.msgShow('تعديل مستخدم', 'اسم المستخدم الذي تود ادخاله موجود مسبقا', 3)
        else:
            if imageCheck != False:
                uploudImgUser = self.connectFTP.UploadFileFtp('Users', imageUser, NameImage)
            columnAndValue= "`FullName` = '{}', `Username` = '{}', `Password` = '{}', `Email` = '{}', `PhoneNumber` = '{}', `NumberID` = '{}', `permission` = '{}',`sex` = '{}'".format(fullName, userName,
                                                                                passHash, email,
                                                                                numberPhone, numberID,
                                                                                permission, sex)

            UpdateUser = self.con.update('user', columnAndValue,"UserID = {}".format(str(self.labUserID.text())))
            if UpdateUser or uploudImgUser == True:
                self.msgShow('تعديل مستخدم', 'تم تعديل المستخدم [ {} ] بنجاح'.format(userName), 1)
            else:
                self.msgShow('تعديل مستخدم', 'حدث مشكله اثناء تعديل المستخدم'.format(userName), 2)
            self.Cancel()













