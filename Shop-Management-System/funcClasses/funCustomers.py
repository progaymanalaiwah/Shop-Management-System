# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import urllib,hashlib,string,random,re
class funCustomers():

    # Function Select Image Of Computer
    def SelectImageCustomer(self,e):
        import os
        # Username Computer
        UsernameComputer = os.environ.get("USERNAME")
        # Path Open
        OpenPath = "c:/Users/{0}/Pictures/".format(UsernameComputer)
        Filter = "*.jpg;;*.png;;*.gif;;*.jpge"
        PathImage = str(QFileDialog.getOpenFileNameAndFilter(self,'صورت العميل '.decode(),OpenPath,Filter)[0])
        if PathImage:
            self.labCustomerImage.setPixmap(QPixmap(PathImage))
            # Size Image
            SizeImage = os.stat(PathImage).st_size / 1024
            # Extension Image
            Extension  = PathImage.split(".")[-1]
            # Array Content Information Image
            Image = {"path":PathImage,"size":SizeImage,"extension":Extension}
            # Glopal Arrar Image
            self.InfoImage = Image

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

    # Function Add Customers
    def AddCustomers(self):
        try:
            # the InfoImage is Globle Array Of Function SelectImageCustomer
            infoImage   = self.InfoImage
            CustImage   = self.InfoImage['path']
            extension   = self.InfoImage['extension']
        except AttributeError as e:
            CustImage = ":/images/UserDefault.png";
            extension = 'png'

        CustName    = self.lineEditCustomerName.text()
        CustEmail   = self.lineEditCustomerEmail.text()
        CustPhone   = self.lineEditCustomerPhone.text()
        CustAddress = self.plainTextEditCustomerAddress.toPlainText()
        CustSex     = str(self.comboBoxSex.currentText())
        CustNameImage = self.RandomKeyImage()+"."+extension
        UserID        = self.labUserID.text()

        # Filter Email Using Regex
        EmailRegex  = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', CustEmail)
        # Check Value Of Form
        if not CustName or not CustEmail or not CustAddress or not CustPhone:
            QMessageBox.critical(self,'اظافة عميل'.decode(),'يجب ملء جميع الحقول فهيه مطلوبه'.decode())
        elif  EmailRegex == None:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'البريد الالكتروني الذي ادخلته غير صحيح'.decode())
        elif CustSex == 'جنس العميل':
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'يجب اختيار جنس العميل'.decode())
        elif len(CustPhone) > 20:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'رقم العميل يجب ان لا يكون اكبر من 20 رقم '.decode())
        elif len(CustEmail) > 50:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'بريد العميل يجب ان لا يكون اكبر من 50 رقم '.decode())
        elif len(CustName) > 50:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'اسم العميل يجب ان  لا يكون اكبر من 50 رقم '.decode())
        elif len(CustAddress) > 230:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'عنوان العميل يجب ان يكون اقل من 230 حرف'.decode())
        else:
            if CustImage == ":/images/UserDefault.png":
                MsgImage = QMessageBox.warning(self, 'اظافة عميل'.decode(), 'انت لم تختر صورت العميل سوف يتم اختيار الصوره الافتراضيه'.decode(),QMessageBox.Ok | QMessageBox.No,QMessageBox.No)
                if  MsgImage == QMessageBox.No:
                    return False
            resultUpload = self.connectFTP.UploadFileFtp('Customers',CustImage,CustNameImage)
            if resultUpload:
                ColumnTable = "`CustomersName`,`CustomersPhone`,`CustomersEmail`,`CustomersAddress`,`CustomersSex`,`UserID`,`CustomerImage`"
                ColumnValue = "'{0}','{1}','{2}','{3}','{4}','{5}','{6}'".format(CustName,CustPhone,CustEmail,CustAddress,CustSex,UserID,CustNameImage)
                try:
                    resultAddCust = self.con.insert('customers',ColumnTable,ColumnValue)
                    if resultAddCust:
                        QMessageBox.information(self, 'اظافة عميل'.decode(),
                                             'تم اظافة العميل بنجاح'.decode())
                        self.ShowCustomers()
                    else:
                        self.connectFTP.ftp.cwd('./Customers')
                        self.connectFTP.ftp.delete(CustNameImage)
                        QMessageBox.critical(self, 'اظافة عميل'.decode(),
                                             'حدث خلل اثناء اظافة العميل الرجاء المحاوله في وقت اخر'.decode())
                except:
                    self.connectFTP.ftp.cwd('./Customers')
                    self.connectFTP.ftp.delete(CustNameImage)
                    QMessageBox.critical(self, 'اظافة عميل'.decode(),
                                         'حدث خلل اثناء اظافة العميل الرجاء المحاوله في وقت اخر'.decode())
            else:
                QMessageBox.critical(self, 'اظافة عميل'.decode(), 'حدث خلل اثناء رفع الصوره الرجاء المحاوله في وقت اخر'.decode())

    # Function Show Customers On Table
    def ShowCustomers(self):
        selectAction = str(self.comboBoxSelectActive.currentText())
        if selectAction == 'العملاء الفعالين':
            CustomersActive = 1
            self.btnCustomerNotActivet.setEnabled(True)
            self.btnCustomerActive.setEnabled(False)
        else:
            CustomersActive = 0
            self.btnCustomerNotActivet.setEnabled(False)
            self.btnCustomerActive.setEnabled(True)

        con = self.con.con
        con = con.cursor()
        sql = """
            SELECT customers.* ,user.FullName FROM `customers`
            INNER JOIN user ON
            customers.UserID = User.UserID
            WHERE CustomersActive = {0} ORDER BY CustomersID DESC
        """.format(CustomersActive)
        # Data Customers
        con.execute(sql)
        Info = con.fetchall()
        lengthCustomers = len(Info)
        self.tableCustomer.setColumnCount(8)
        self.tableCustomer.setRowCount(lengthCustomers)
        Row = 0
        for info in Info:
            self.tableCustomer.setItem(Row,0,QTableWidgetItem(str(info[0])))
            self.tableCustomer.setItem(Row, 1, QTableWidgetItem(str(info[1]).decode('utf-8')))
            self.tableCustomer.setItem(Row, 2, QTableWidgetItem(str(info[3]).decode('utf-8')))
            self.tableCustomer.setItem(Row, 3, QTableWidgetItem(str(info[2]).decode('utf-8')))
            self.tableCustomer.setItem(Row, 4, QTableWidgetItem(str(info[5]).decode('utf-8')))
            self.tableCustomer.setItem(Row, 5, QTableWidgetItem(str(info[10]).decode('utf-8')))
            self.tableCustomer.setItem(Row, 6, QTableWidgetItem(str(info[7]).decode('utf-8')))
            self.tableCustomer.setItem(Row, 7, QTableWidgetItem(str(info[6]).decode('utf-8')))
            Row+=1

    # Function Cancel
    def Cancel(self):
        self.tableCustomer.setEnabled(True)
        self.btnCustomerEdit.setEnabled(False)
        self.btnCustomerActive.setEnabled(False)
        self.btnCustomerAdd.setEnabled(True)
        self.btnCustomerNotActivet.setEnabled(True)
        self.lineEditCustomerPhone.clear()
        self.lineEditCustomerEmail.clear()
        self.lineEditCustomerName.clear()
        self.lineEditCustomerSearch.clear()
        self.plainTextEditCustomerAddress.clear()
        self.comboBoxSex.clear()
        self.comboBoxSex.addItems(["جنس العميل".decode("utf-8"), "ذكر".decode("utf-8"), "انثى".decode("utf-8")])
        self.labCustomerImage.setPixmap(QPixmap(":images/UserDefault.png"))

    # Function Show Information Customer Of Form
    def ShowInfoOfForm(self,e):
        Row = e.row()
        CustID      = self.tableCustomer.item(Row, 0).text()
        CustName    = self.tableCustomer.item(Row,1).text()
        CustPhone   = self.tableCustomer.item(Row,3).text()
        CustAddress = self.tableCustomer.item(Row,7).text()
        CustEmail   = self.tableCustomer.item(Row,2).text()
        CustSex     = self.tableCustomer.item(Row,6).text()
        NameImage   = self.con.select("CustomerImage","customers","CustomersID = {0}".format(CustID),2)[0]
        Url   = "http://"+self.connectFTP.HOSTFTP + "/Home/" +self.connectFTP.NameFile + "/Customers/" + NameImage
        data = urllib.urlopen(Url).read()
        print(self.connectFTP.HOSTFTP)
        NameImage = QPixmap()
        NameImage.loadFromData(data)
        self.labCustID.setText(CustID)
        self.labCustomerImage.setPixmap(NameImage)
        self.lineEditCustomerName.setText(CustName)
        self.lineEditCustomerEmail.setText(CustEmail)
        self.lineEditCustomerPhone.setText(CustPhone)
        self.plainTextEditCustomerAddress.setPlainText(CustAddress)
        self.comboBoxSex.setItemText(0,CustSex)
        self.btnCustomerAdd.setEnabled(False)
        self.btnCustomerEdit.setEnabled(True)
        self.btnCustomerNotActivet.setEnabled(False)
        self.btnCustomerActive.setEnabled(False)
        self.tableCustomer.setEnabled(False)


    # Function Edit Customers
    def EditCustomer(self):
        try:
            # the InfoImage is Globle Array Of Function SelectImageCustomer
            infoImage   = self.InfoImage
            CustImage   = self.InfoImage['path']
            extension   = self.InfoImage['extension']
        except AttributeError as e:
            CustImage = False
        CustName      = self.lineEditCustomerName.text()
        CustEmail     = self.lineEditCustomerEmail.text()
        CustPhone     = self.lineEditCustomerPhone.text()
        CustAddress   = self.plainTextEditCustomerAddress.toPlainText()
        CustSex       = str(self.comboBoxSex.currentText())
        CustID = self.labCustID.text()
        CustNameImage = self.con.select("CustomerImage","customers","CustomersID = {0}".format(CustID),2)[0]
        print CustNameImage
        UserID = '1'

        # Filter Email Using Regex
        EmailRegex  = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', CustEmail)
        # Check Value Of Form
        if not CustName or not CustEmail or not CustAddress or not CustPhone:
            QMessageBox.critical(self,'اظافة عميل'.decode(),'يجب ملء جميع الحقول فهيه مطلوبه'.decode())
        elif  EmailRegex == None:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'البريد الالكتروني الذي ادخلته غير صحيح'.decode())
        elif CustSex == 'جنس العميل':
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'يجب اختيار جنس العميل'.decode())
        elif len(CustPhone) > 20:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'رقم العميل يجب ان لا يكون اكبر من 20 رقم '.decode())
        elif len(CustEmail) > 50:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'بريد العميل يجب ان لا يكون اكبر من 50 رقم '.decode())
        elif len(CustName) > 50:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'اسم العميل يجب ان  لا يكون اكبر من 50 رقم '.decode())
        elif len(CustAddress) > 230:
            QMessageBox.critical(self, 'اظافة عميل'.decode(), 'عنوان العميل يجب ان يكون اقل من 230 حرف'.decode())

        else:
            resultUpload = True
            if CustImage != False:
                resultUpload = self.connectFTP.UploadFileFtp('Customers',CustImage,CustNameImage)
            if resultUpload:
                ColumnTable = "`CustomersName` ='{0}',`CustomersPhone` = '{1}',`CustomersEmail` = '{2}',`CustomersAddress` = '{3}',`CustomersSex` = '{4}'".format(CustName,CustPhone,CustEmail,CustAddress,CustSex)
                try:
                    resultAddCust = self.con.update("customers",ColumnTable,"CustomersID = {}".format(CustID))
                    if resultAddCust:
                        QMessageBox.information(self, 'اظافة عميل'.decode(),
                                             'تم تعديل العميل بنجاح العميل بنجاح'.decode())
                        self.ShowCustomers()
                        self.Cancel()
                except:
                    self.connectFTP.ftp.cwd('./Customers')
                    self.connectFTP.ftp.delete(CustNameImage)
                    QMessageBox.critical(self, 'اظافة عميل'.decode(),
                                         'حدث خلل اثناء تعديل العميل الرجاء المحاوله في وقت اخر'.decode())
                self.Cancel()
            else:
                QMessageBox.critical(self, 'اظافة عميل'.decode(), 'حدث خلل اثناء رفع الصوره الرجاء المحاوله في وقت اخر'.decode())


    # Function Active And Not Active Customers
    def ActiveCustomer(self):
        if self.tableCustomer.selectedItems():
            typeActive  = str(self.comboBoxSelectActive.currentText())
            Row = self.tableCustomer.currentRow()
            CustomersID = self.tableCustomer.item(Row,0).text()
            if typeActive == "العملاء الفعالين":
                ActiveCustomer = 0
                msgOk = "هل انت متئكد من الغاء العميل".decode("UTF-8")
            else:
                ActiveCustomer = 1
                msgOk = "هل انت متئكد من تفعيل العميل العميل".decode("UTF-8")
            Msg = QMessageBox.information(self,'العملاء'.decode("utf-8"),msgOk,QMessageBox.Ok | QMessageBox.No,QMessageBox.No)
            if Msg == QMessageBox.Ok:
                try:
                    resultUpdate = self.con.update("customers","`CustomersActive` = {0}".format(ActiveCustomer),"CustomersID = {0}".format(CustomersID))
                    if resultUpdate:
                        QMessageBox.information(self, 'الغاء العميل'.decode("utf-8"),
                                            'تم الغاء العميل بنجاح'.decode("utf-8"))
                        self.ShowCustomers()
                except:
                    QMessageBox.critical(self, 'الغاء العميل'.decode("utf-8"),
                                        'حذث خلل اثناء الغاء العميل الرجاء المحاوله في ما بعد'.decode("utf-8"))
            else:return False
        else:
            QMessageBox.warning(self,'الغاء العميل'.decode("utf-8"),'يجب تحديد العميل الذي تود الغائه'.decode("utf-8"))