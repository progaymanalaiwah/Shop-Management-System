# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import urllib,hashlib,string,random,re

class funEmployes():
    # Function Create Report All Employes Html Page
    def createReportHtmlPage(self):
        Active = str(self.comboxEmploActive.currentText())
        if Active == 'الموظفين النشطين':
            emploActive = 1
        else:
            emploActive = 0
        sql = """
                SELECT employes.* ,Section.SectionName,User.UserName FROM employes
                INNER JOIN Section ON
                employes.SectionID = Section.SectionID
                INNER JOIN User ON
                employes.UserID = User.UserID
                WHERE emploActive = {0}
            """.format(emploActive)
        con = self.con.con
        con = con.cursor()
        con.execute(sql)
        InfoEmployes = con.fetchall()
        lenghtEmployes = len(InfoEmployes)
        self.tableEmployes.setRowCount(lenghtEmployes)
        self.labEmploNumber.setText(str(lenghtEmployes))
        Row = 0
        nowTime = str(time.strftime("%I:%M:%S %p"))
        day     = str(time.strftime("%d-%m-%Y"))
        text = """
            <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    	<title>تقرير الموظفين</title>
    </head>
    <style>
    	body{direction: rtl; background: #fff;}
    	*{font-family: sans-serif;}
    	.container{margin: 0px;}
    	.pull-right{float: right;}
    	.pull-left{float: left;}
    	.text-center{text-align: center;}
    	.padding{padding-right: 40px;}
    	.bold{font-weight: bold;}
    	table  {
    		border-collapse: collapse;
    	}
    	table tr:first-child td{
    		background: #3E4651;
    	    color: #FFF;
    	    padding: 3px;
    	   width: 166.25px;
    	   text-align: center;
    	}
    	table tr td{
    		background-color: #fff;
    		border:1px solid #777;
    	}

    </style>
    <body>
    	<div class="container">
    		<div class="header">
    		<h3 class="text-center">بسم الله الرحمن الرحيم </h3>
    			<div class="pull-right">
    				<div>
    					<span class="bold">  نوع التقرير : </span>
    					<span> تقرير مفصل عن كل الموظفين </span>
    					<p></p>
    					<span class="bold">  طلب التقرير  : </span>
    					<span> ايمن محمود محمد عليوة </span>
    				</div>
    			</div>
    			<div class="pull-left">
    				<span class="bold">تاريخ التقرير : </span>
    				<span> %s </span>
    				<p></p>
    				<span class="bold">الوقت    </span>
    				<span class="padding"> <span class="bold"> : </span> %s </span>
    			</div>
    		</div>
    		<br>
    		<br>

    		<br>
    		<br>

    		<table class="text-center">
    			<tr>
    				<td>الرقم الوطني</td>
    				<td>الاسم</td>
    				<td>الراتب</td>
    				<td>العمر</td>
    				<td>القسم</td>
    				<td>تاريخ التوظيف</td>
    				<td>رقم الهاتف</td>
    				<td>المظيف</td>

    			</tr>

            """% (day,nowTime)
        reportEmployes = open('report/reportEmployees.html', 'w')
        reportEmployes.write(text)
        reportEmployes.close()
        reportEmployes = open('report/reportEmployees.html', 'a+')
        for info in InfoEmployes:
            text = """
                <tr>
    				<td>{0}</td>
    				<td>{1}</td>
    				<td>{2}</td>
    				<td>{3}</td>
    				<td>{4}</td>
    				<td>{5}</td>
    				<td>{6}</td>
    				<td>{7}</td>
    			</tr>
                """.format(str(info[1]).decode("utf-8"),
                           str(info[0]).decode("utf-8"),
                           str(info[6]).decode("utf-8"),
                           str(info[7]).decode("utf-8"),
                           str(info[12]).decode("utf-8"),
                           str(info[3]).decode("utf-8"),
                           str(info[2]).decode("utf-8"),
                           str(info[13]).decode("utf-8"))
            reportEmployes.write(text)
        reportEmployes.write("""
                    </table>
                </div>
            </body>
            </html>
            """)
        reportEmployes.close()


    # Function Edit Informaton Employee
    def editEmployes(self):
        employeeName        = self.textEmploName.text()
        employeeNumberID    = self.textEmploNumberID.text()
        employeeNumberPhone = self.textEmploNumberPhone.text()
        employeeAge         = self.textEmploAge.text()
        employeeSalry       = self.textEmploSalary.text()
        employeeAddreass    = self.textEmploAddreass.toPlainText()
        employeeSex         = str(self.comboxEmploSex.currentText())
        SectionName         = str(self.comBoxEmploSection.currentText())
        Row                 = self.tableEmployes.currentRow()
        NumberID            = self.tableEmployes.item(Row,0).text()
        infoEmploye         = self.con.select('image,EmployeName','employes','NumberID = {}'.format(NumberID),2)
        NameImageExtension  = infoEmploye[0]
        NameImage           = str(NameImageExtension).split('.')[0]
        SectionName         = str(self.comBoxEmploSection.currentText())
        UserID              = 1
        SectionID = self.con.select("SectionID","Section","SectionName = '{0}'".format(SectionName),2)[0]
        EmployeName = infoEmploye[1].decode("utf-8")
        CheckNumberD = self.con.checkData('employes','NumberID',employeeNumberID+" and EmployeName != '{0}'".format(EmployeName))
        if not employeeName or not employeeNumberID or not employeeNumberPhone or not employeeAge or not employeeSalry or not employeeAddreass:
            self.msgShow("تعديل الموظف","يجب ملء جميع الحقول فهيه مطلوب",2)
        elif employeeSex == 'جنس الموظف':
            self.msgShow("تعديل الموظف","يجب اختيار جنس الموظف",2)
        elif SectionName == 'قسم عمل الموظف':
            self.msgShow("تعديل الموظف", "يجب اختيار قسم عمل الموظف", 2)
        elif CheckNumberD == True:
            self.msgShow("تعديل الموظف", "الرقم الوطني موجود بلفعل", 2)
        else:
            try:
                InfoImage = self.InfoImage
                pathImage = InfoImage['path']
                extension = InfoImage['extension']
                UploudImage = self.connectFTP.UploadFileFtp("employes", pathImage, NameImage+"."+extension)
                if UploudImage != True:
                    self.msgShow("تعديل الموظف", "حث مشكلة اثناء رفع الصوره الرجاء المحاوله في وقت اخر", 2)
                    return False
            except:pass
            try:
                data = "`EmployeName` = '{}', `NumberID` = '{}', `NumberPhone` = '{}',`image` = '{}', `Salary` = '{}', `Age` = '{}', `Sex` = '{}', `Address`= '{}', `SectionID` = '{}', `UserID` = '{}'".format(employeeName,employeeNumberID,employeeNumberPhone,NameImageExtension,employeeSalry,employeeAge,employeeSex,employeeAddreass,SectionID,UserID)
                try:
                    resultInsert = self.con.update("employes",data,"NumberID = '{0}'".format(NumberID))
                except:pass
                if resultInsert:
                    self.msgShow("تعديل الموظف", "تم تعديل موظف بنجاح", 1)
                    self.Cancel()
                    self.showEmployes()
                else:pass
            except:pass
            self.Cancel()

    # Function Insert Data Of Form
    def infoEmployesOfForm(self,e):
        Row = self.tableEmployes.currentRow()
        NumberID = self.tableEmployes.item(Row,0).text()
        infoEmploye = self.con.select('*','employes','NumberID = {0}'.format(NumberID),2)
        self.textEmploName.setText(infoEmploye[0])
        self.textEmploNumberPhone.setText(infoEmploye[2])
        self.textEmploSalary.setText(infoEmploye[6])
        self.textEmploAddreass.setPlainText(infoEmploye[9])
        self.textEmploAge.setText(str(infoEmploye[7]))
        self.textEmploNumberID.setText(infoEmploye[1])
        path = "http://" + self.connectFTP.HOSTFTP + '/Home/' + self.connectFTP.NameFile + '/employes/' + infoEmploye[5]
        ImageEmploye = QPixmap()
        data = urllib.urlopen(path).read()
        ImageEmploye.loadFromData(data)
        self.labEmploye.setPixmap(ImageEmploye)
        SectionName = self.con.select('SectionName','Section','SectionID = "{0}"'.format(infoEmploye[10]),2)[0]
        self.comBoxEmploSection.setItemText(0,SectionName)
        self.comboxEmploSex.clear()
        if infoEmploye[8] == 'ذكر':
            self.comboxEmploSex.addItems(['ذكر'.decode('utf-8'),'انثي'.decode('utf-8')])
        else:
            self.comboxEmploSex.addItems(['انثي'.decode('utf-8'),'ذكر'.decode('utf-8')])
        self.btnEmploEdit.setEnabled(True)
        self.btnEmploAdd.setEnabled(False)
        self.btnEmploActive.setEnabled(False)
        self.btnEmploNotActive.setEnabled(False)

    # Function Search Of Employes
    def SearchEmploye(self, e):
        Active = str(self.comboxEmploActive.currentText())
        if Active == 'الموظفين النشطين':
            emploActive = 1
        else:
            emploActive = 0

        Data = self.textEmploSearch.text()
        sql = """
              SELECT employes.* ,Section.SectionName,User.UserName FROM employes
              INNER JOIN Section ON
              employes.SectionID = Section.SectionID
              INNER JOIN User ON
              employes.UserID = User.UserID
              WHERE
              (employes.EmployeName LIKE '%{}%' OR
              employes.NumberID LIKE '%{}%' OR
              employes.NumberPhone LIKE '%{}%' OR
              employes.DateOfEmployment LIKE '%{}%' OR
              employes.Salary LIKE '%{}%' OR
              employes.Age LIKE '%{}%' OR
              Section.SectionName LIKE '%{}%' OR
              User.UserName LIKE '%{}%' ) AND
              emploActive = {}
          """.format(Data, Data, Data, Data, Data, Data, Data, Data, emploActive)
        con = self.con.con
        con = con.cursor()
        con.execute(sql)
        InfoEmployes = con.fetchall()
        lenghtEmployes = len(InfoEmployes)
        self.tableEmployes.setRowCount(lenghtEmployes)
        self.labEmploNumber.setText(str(lenghtEmployes))
        Row = 0
        for info in InfoEmployes:
            self.tableEmployes.setItem(Row, 0, QTableWidgetItem(str(info[1]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 1, QTableWidgetItem(str(info[0]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 2, QTableWidgetItem(str(info[6]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 3, QTableWidgetItem(str(info[7]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 4, QTableWidgetItem(str(info[12]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 5, QTableWidgetItem(str(info[3]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 6, QTableWidgetItem(str(info[2]).decode("utf-8")))
            self.tableEmployes.setItem(Row, 7, QTableWidgetItem(str(info[13]).decode("utf-8")))

            # Add setToolTip To Item
            self.tableEmployes.item(Row, 0).setToolTip(str(info[1]).decode("utf-8"))
            self.tableEmployes.item(Row, 1).setToolTip(str(info[0]).decode("utf-8"))
            self.tableEmployes.item(Row, 2).setToolTip(str(info[6]).decode("utf-8"))
            self.tableEmployes.item(Row, 3).setToolTip(str(info[7]).decode("utf-8"))
            self.tableEmployes.item(Row, 4).setToolTip(str(info[12]).decode("utf-8"))
            self.tableEmployes.item(Row, 5).setToolTip(str(info[3]).decode("utf-8"))
            self.tableEmployes.item(Row, 6).setToolTip(str(info[2]).decode("utf-8"))
            self.tableEmployes.item(Row, 7).setToolTip(str(info[13]).decode("utf-8"))
            Row += 1


    # Function Active And Not Active An Employes
    def ActiveEmploye(self):
        if self.tableEmployes.selectedItems():
            Active = str(self.comboxEmploActive.currentText())
            if Active == 'الموظفين النشطين':
                emploActive = 0
                conMsg = 'تم الغاء الموظف بنجاح'
            else:
                emploActive = 1
                conMsg = 'تم تفعيل الموظف بنجاح'

            Row          = self.tableEmployes.currentRow()
            EmployeID    = self.tableEmployes.item(Row,0).text()
            resultActive = self.con.update('employes','emploActive = "{0}"'.format(emploActive),"NumberID = {0}".format(EmployeID))
            if resultActive:
                self.msgShow('الموظف',conMsg,1)
                self.showEmployes()
        else:
            self.msgShow('الموظف','يجب تحديد الموظف الذي تود الغائه',2)


    def showEmployes(self):
        Active = str(self.comboxEmploActive.currentText())
        if Active == 'الموظفين النشطين':
            emploActive = 1
            self.btnEmploActive.setEnabled(False)
            self.btnEmploNotActive.setEnabled(True)
        else:
            emploActive = 0
            self.btnEmploActive.setEnabled(True)
            self.btnEmploNotActive.setEnabled(False)


        sql = """
            SELECT employes.* ,Section.SectionName,User.FullName FROM employes
            INNER JOIN Section ON
            employes.SectionID = Section.SectionID
            INNER JOIN User ON
            employes.UserID = User.UserID
            WHERE emploActive = {0}
        """.format(emploActive)
        con = self.con.con
        con = con.cursor()
        con.execute(sql)
        InfoEmployes = con.fetchall()
        lenghtEmployes = len(InfoEmployes)
        self.tableEmployes.setRowCount(lenghtEmployes)
        self.labEmploNumber.setText(str(lenghtEmployes))
        Row = 0
        for info in InfoEmployes:
            self.tableEmployes.setItem(Row,0,QTableWidgetItem(str(info[1]).decode("utf-8")))
            self.tableEmployes.setItem(Row,1,QTableWidgetItem(str(info[0]).decode("utf-8")))
            self.tableEmployes.setItem(Row,2,QTableWidgetItem(str(info[6]).decode("utf-8")))
            self.tableEmployes.setItem(Row,3,QTableWidgetItem(str(info[7]).decode("utf-8")))
            self.tableEmployes.setItem(Row,4,QTableWidgetItem(str(info[12]).decode("utf-8")))
            self.tableEmployes.setItem(Row,5,QTableWidgetItem(str(info[3]).decode("utf-8")))
            self.tableEmployes.setItem(Row,6,QTableWidgetItem(str(info[2]).decode("utf-8")))
            self.tableEmployes.setItem(Row,7,QTableWidgetItem(str(info[13]).decode("utf-8")))

            # Add setToolTip To Item
            self.tableEmployes.item(Row, 0).setToolTip(str(info[1]).decode("utf-8"))
            self.tableEmployes.item(Row, 1).setToolTip(str(info[0]).decode("utf-8"))
            self.tableEmployes.item(Row, 2).setToolTip(str(info[6]).decode("utf-8"))
            self.tableEmployes.item(Row, 3).setToolTip(str(info[7]).decode("utf-8"))
            self.tableEmployes.item(Row, 4).setToolTip(str(info[12]).decode("utf-8"))
            self.tableEmployes.item(Row, 5).setToolTip(str(info[3]).decode("utf-8"))
            self.tableEmployes.item(Row, 6).setToolTip(str(info[2]).decode("utf-8"))
            self.tableEmployes.item(Row, 7).setToolTip(str(info[13]).decode("utf-8"))
            Row+=1

    # Function Add Employee To Database
    def addEmployee(self):
        employeeName        = self.textEmploName.text()
        employeeNumberID    = self.textEmploNumberID.text()
        employeeNumberPhone = self.textEmploNumberPhone.text()
        employeeAge         = self.textEmploAge.text()
        employeeSalry       = self.textEmploSalary.text()
        employeeAddreass    = self.textEmploAddreass.toPlainText()
        employeeSex         = str(self.comboxEmploSex.currentText())
        SectionName         = str(self.comBoxEmploSection.currentText())
        UserID              = self.labUserID.text()
        try:
            SectionID = self.con.select("SectionID","Section","SectionName = '{0}'".format(SectionName),2)[0]
            pathImage = self.InfoImage['path']
            Extension = self.InfoImage['extension']
            NameImage = self.RandomKeyImage() + "." + Extension
        except TypeError as e:pass
        except  Exception as e:
            pathImage = ''

        if not employeeNumberID:pass
        else:
         CheckNumberD = self.con.checkData('employes','NumberID',employeeNumberID,"NumberID = '{0}'".format(employeeNumberID))


        if not employeeName or not employeeNumberID or not employeeNumberPhone or not employeeAge or not employeeSalry or not employeeAddreass:
            self.msgShow("اظافة الموظف","يجب ملء جميع الحقول فهيه مطلوب",2)
        elif employeeSex == 'جنس الموظف':
            self.msgShow("اظافة الموظف","يجب اختيار جنس الموظف",2)
        elif SectionName == 'قسم عمل الموظف':
            self.msgShow("اظافة الموظف", "يجب اختيار قسم عمل الموظف", 2)
        elif not pathImage:
            self.msgShow("اظافة الموظف", "يجب اختيار صورت  الموظف", 2)
        elif CheckNumberD == True:
            self.msgShow("اظافة الموظف", "الرقم الوطني موجود بلفعل", 2)
        else:
            UploudImage = self.connectFTP.UploadFileFtp("employes",pathImage,NameImage)
            if UploudImage:
                ColumnTable = "`EmployeName`, `NumberID`, `NumberPhone`,`image`, `Salary`, `Age`, `Sex`, `Address`, `SectionID`, `UserID`"
                ColumnValue = "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'".format(employeeName,employeeNumberID,employeeNumberPhone,NameImage,employeeSalry,employeeAge,employeeSex,employeeAddreass,SectionID,UserID)
                try:
                   resultInsert = self.con.insert("employes",ColumnTable,ColumnValue)
                   if resultInsert:
                       self.msgShow("اظافة الموظف", "تم اظافة موظف بنجاح", 1)
                       self.Cancel()
                       self.showEmployes()
                   else:
                       self.connectFTP.ftp.cwd('./employes')
                       self.connectFTP.ftp.delete(NameImage)
                       self.msgShow("اظافة الموظف", "حث مشكلة اثناء اظافة الموظف الرجاء المحاوله في وقت اخر", 2)
                except:
                   self.connectFTP.ftp.cwd('./employes')
                   self.connectFTP.ftp.delete(NameImage)
                   self.msgShow("اظافة الموظف", "حث مشكلة اثناء اظافة الموظف الرجاء المحاوله في وقت اخر", 2)
                   self.Cancel()
            else:
                self.msgShow("اظافة الموظف", "حث مشكلة اثناء رفع الصوره الرجاء المحاوله في وقت اخر", 2)

    # Function Select Image Of Computer
    def SelectImageEployee(self,e):
        import os
        # Username Computer
        UsernameComputer = os.environ.get("USERNAME")
        # Path Open
        OpenPath = "c:/Users/{0}/Pictures/".format(UsernameComputer)
        Filter = "*.jpg;;*.png;;*.gif;;*.jpge"
        PathImage = str(QFileDialog.getOpenFileNameAndFilter(self,'صورت العميل '.decode(),OpenPath,Filter)[0])
        if PathImage:
            self.labEmploye.setPixmap(QPixmap(PathImage))
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

    # Function Show Section Of ComBox
    def ShowSection(self):
        DateSection = self.con.select("SectionName","Section","ActiveSection=1")
        for item in DateSection:
            data = str(item[0]).decode("utf-8")
            self.comBoxEmploSection.addItem(data)

    # Function Cancel
    def Cancel(self):
        self.textEmploAddreass.clear()
        self.textEmploAge.clear()
        self.textEmploName.clear()
        self.textEmploNumberID.clear()
        self.textEmploSalary.clear()
        self.textEmploSearch.clear()
        self.textEmploNumberPhone.clear()
        self.labEmploye.setPixmap(QPixmap(":/images/employes.png"))
        self.comboxEmploActive.setCurrentIndex(0)
        self.comBoxEmploSection.setCurrentIndex(0)
        self.comboxEmploSex.setCurrentIndex(0)
        self.tableEmployes.setEnabled(True)
        self.btnEmploAdd.setEnabled(True)
        self.btnEmploActive.setEnabled(False)
        self.btnEmploNotActive.setEnabled(True)
        self.btnEmploEdit.setEnabled(False)
        self.comboxEmploSex.clear()
        self.comboxEmploSex.addItems(['جنس الموظف'.decode('utf-8'),'ذكر'.decode('utf-8'), 'انثي'.decode('utf-8')])
        self.comBoxEmploSection.setItemText(0, 'قسم عمل الموظف'.decode('utf-8'))

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
