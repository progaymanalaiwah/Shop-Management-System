# _*_ coding:utf8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from classes.class_selectUser import *
import time,string,random,hashlib

class funClassAddUser:
    # Function Create Password Complix
    def createPasswordComplix(self,e):
        lenght  = random.randrange(10,20)
        contentPassword =  string.digits + string.ascii_uppercase + string.ascii_lowercase + '!$#^&*'
        password = "".join(random.choice(contentPassword) for i in range(lenght))
        self.textCreatePasswordComplix.setText(password)

    # Function Show And Hedding Menu Permessions
    def showMenuPermission(self,e):
        formHeight     = self.height() # Default Value 351
        groupBoxPer    = self.groupBokPer.height() # Default Value 41
        groupBoxButton = self.groupBoxButtonControl.pos().y() # Default Value y 280
        if formHeight == 351:
            self.setFixedHeight(635)
            self.groupBoxButtonControl.move(10,567)
            self.groupBokPer.setFixedHeight(331)
        else:
            self.setFixedHeight(351)
            self.groupBoxButtonControl.move(10,280)
            self.groupBokPer.setFixedHeight(41)

    # Function Create Random Key For Name Image
    def RandomKeyImage(self):
        millis = hashlib.md5(str(time.time())).hexdigest()[:16]
        stringLetters = list(string.ascii_letters + string.hexdigits)
        random.shuffle(stringLetters)
        stringLetters = ''.join(stringLetters[:9])
        keyImage = list(millis+stringLetters)
        random.shuffle(keyImage)
        keyImage = ''.join(keyImage)
        return keyImage

    # Function Select Image Of Computer
    def selectImgUser(self,e):
        import os
        # Username Computer
        UsernameComputer = os.environ.get("USERNAME")
        # Path Open
        OpenPath = "c:/Users/{0}/Pictures/".format(UsernameComputer)
        Filter = "*.jpg;;*.png;;*.gif;;*.jpge"
        PathImage = str(QFileDialog.getOpenFileNameAndFilter(self, 'اختيار صورت المستخدم '.decode("utf-8"), OpenPath, Filter)[0])
        if PathImage:
            self.labAddImgUser.setPixmap(QPixmap(PathImage))
            # Size Image
            SizeImage = os.stat(PathImage).st_size / 1024
            # Extension Image
            Extension = PathImage.split(".")[-1]
            # Array Content Information Image
            Image = {"path": PathImage, "size": SizeImage, "extension": Extension}
            # Glopal Arrar Image
            self.InfoImage = Image

    # Function Show Message
    def msgShow(self,title,text,Msgicon):
        if Msgicon == 1:
            QMessageBox.information(self,title.decode("utf-8"),text.decode("utf-8"))
        elif Msgicon == 2:
            QMessageBox.critical(self, title.decode("utf-8"), text.decode("utf-8"))
        elif Msgicon == 3:
            QMessageBox.warning(self, title.decode("utf-8"), text.decode("utf-8"))
        else:
            QMessageBox.question(self, title.decode("utf-8"), text.decode("utf-8"))

            # Function Add User To Database

    def addUser(self):
        fullName = self.textFullName.text()
        userName = self.textUsername.text()
        email = self.textEmail.text()
        numberID = self.textNumberID.text()
        numberPhone = self.textNumberPhone.text()
        sex = str(self.comboxSex.currentText())
        password = self.textPassword.text()
        passHash = hashlib.md5(password).hexdigest()
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
            NameImage = self.RandomKeyImage() + "." + extension
        except:
            imageUser = False
        checkBoxPermission = {1: self.checkBoxCalc, 2: self.checkBoxChat,3:self.checkBoxSettings,
                              11: self.checkBoxSSection, 12: self.checkBoxSStor, 201: self.checkBoxSection,
                              21: self.checkBoxAddItem, 22: self.checkBoxSItem, 23: self.checkBoxSCatecory,
                              203: self.checkBoxItem,
                              31: self.checkBoxSCust, 204: self.checkBoxCust,
                              41: self.checkBoxSEmployee, 205: self.checkBoxEmployee,
                              51: self.checkBoxAddUser, 52: self.checkBoxViewUser, 206: self.checkBoxUsers}
        NumberPermission = [1, 2, 11, 12, 201, 21, 22, 23, 203, 31, 204, 41, 205, 51, 52, 206]
        permission = []
        for checkBox in NumberPermission:
            if checkBoxPermission[checkBox].isChecked():
                permission.append(checkBox)
            elif self.checkBoxAll.isChecked():
                permission = NumberPermission
        permission = ",".join(map(str, permission))
        checkData = self.con.select("Username","user","Username = '{}'".format(userName),1)
        if not fullName or not numberPhone or not numberID or not userName or not email or not password:
            self.msgShow('اظافة مستخدم', 'الرجاء ملء جميع الحقول فهيه مطلوبه', 3)
        elif sex == 'جنس المستخدم':
            self.msgShow('اظافة مستخدم', 'الرجاء تحديد جنس العميل', 3)
        elif numberIDError == False:
            self.msgShow('اظافة مستخدم', 'الرجاء كتابت الرقم الوطني بطريقه صحيحه', 3)
        elif numberPhoneError == False:
            self.msgShow('اظافة مستخدم', 'الرجاء كتابت الرقم الهاتف بطريقه صحيحه', 3)
        elif imageUser == False:
            self.msgShow('اظافة مستخدم', 'الرجاء اختيار صورة المستخدم', 3)
        elif checkData > 0:
            self.msgShow('اظافة مستخدم', 'اسم المستخدم الذي تود ادخاله موجود مسبقا', 3)
        else:
            msgPer = QMessageBox.Ok
            if not permission:
                msgPer = QMessageBox.warning(self, 'اظافة مستخدم '.decode(),
                                             'انت لم تضف اي صلاحيات للمستخدم هل انت متئكد من هاذا'.decode(),
                                             QMessageBox.Ok, QMessageBox.No | QMessageBox.No)
            if msgPer == QMessageBox.Ok:
                uploudImgUser = self.connectFTP.UploadFileFtp('Users', imageUser, NameImage)
                if uploudImgUser:
                    columnTable = "`FullName`, `Username`, `Password`, `Email`, `PhoneNumber`, `NumberID`, `permission`, `img`, `sex`"
                    valueColumn = "'{}','{}','{}','{}','{}','{}','{}','{}','{}'".format(fullName, userName,
                                                                                        passHash, email,
                                                                                        numberPhone, numberID,
                                                                                        permission, NameImage, sex)
                    try:
                        insertUser = self.con.insert('user', columnTable, valueColumn)
                        if insertUser:
                            self.msgShow('اظافة مستخدم', 'تم اظافة المستخدم [ {} ] بنجاح'.format(userName), 1)
                        else:
                            self.connectFTP.ftp.cwd("./User")
                            self.connectFTP.ftp.delete(NameImage)
                    except:
                        self.connectFTP.ftp.cwd("./User")
                        self.connectFTP.ftp.delete(NameImage)
                    self.Cancel()

                elif not uploudImgUser:
                    self.msgShow('اظافة مستخدم', 'حذث مشكله اثناء اظافة صورة العميل الرجاء المحاوله في وقت اخر', 2)

    def CopyPassword(self, e):
        textPwd = self.textPassword
        textPwdShow = self.textPasswordShow
        if textPwdShow.isVisible():
            self.textPassword.setText(self.textPasswordShow.text())
        else:
            self.textPasswordShow.setText(self.textPassword.text())

    def ShowPassword(self, e):
        textPwd = self.textPassword
        textPwdShow = self.textPasswordShow
        if textPwdShow.isVisible():
            textPwdShow.setVisible(False)
        else:
            textPwdShow.setVisible(True)

    def CheckAllPer(self):
        checkBoxPermission = {1: self.checkBoxCalc, 2: self.checkBoxChat, 200: self.checkBoxGen,
                              11: self.checkBoxSSection, 12: self.checkBoxSStor, 201: self.checkBoxSection,
                              21: self.checkBoxAddItem, 22: self.checkBoxSItem, 23: self.checkBoxSCatecory,
                              203: self.checkBoxItem,
                              31: self.checkBoxSCust, 204: self.checkBoxCust,
                              41: self.checkBoxSEmployee, 205: self.checkBoxEmployee,
                              51: self.checkBoxAddUser, 52: self.checkBoxViewUser, 206: self.checkBoxUsers}
        NumberPermission = [1, 2, 11, 12, 201, 21, 22, 23, 203, 31, 204, 41, 205, 51, 52, 206, 200]
        permission = []
        for checkBox in NumberPermission:
            if self.checkBoxAll.isChecked():
                checkBoxPermission[checkBox].setChecked(True)

            else:
                checkBoxPermission[checkBox].setChecked(False)

    # Function Cancel
    def Cancel(self):
        self.labAddImgUser.setPixmap(QPixmap(":/images/users.png"))
        self.textPassword.clear()
        self.textFullName.clear()
        self.textCreatePasswordComplix.clear()
        self.textNumberID.clear()
        self.textNumberPhone.clear()
        self.textEmail.clear()
        self.textUsername.clear()
        self.comboxSex.setCurrentIndex(0)
        self.btnEditUser.setEnabled(False)
        self.btnAddUser.setEnabled(True)
        checkBoxPermission = {1: self.checkBoxCalc, 2: self.checkBoxChat,200:self.checkBoxGen,207:self.checkBoxAll,
                              11: self.checkBoxSSection, 12: self.checkBoxSStor, 201: self.checkBoxSection,
                              21: self.checkBoxAddItem, 22: self.checkBoxSItem, 23: self.checkBoxSCatecory,
                              203: self.checkBoxItem,
                              31: self.checkBoxSCust, 204: self.checkBoxCust,
                              41: self.checkBoxSEmployee, 205: self.checkBoxEmployee,
                              51: self.checkBoxAddUser, 52: self.checkBoxViewUser, 206: self.checkBoxUsers}
        NumberPermission = [1, 2, 11, 12, 201, 21, 22, 23, 203, 31, 204, 41, 205, 51, 52, 206,200,207]
        permission = []
        for checkBox in NumberPermission:
             checkBoxPermission[checkBox].setChecked(False)


    def SelectUser(self):
        self.selectUser = selectUser()
        self.selectUser.ShowUser()
        self.selectUser.show()
        self.close()



