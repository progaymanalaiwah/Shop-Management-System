# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.Settings import *
import json,MySQLdb,ftplib,hashlib
from connect import *


class Settings(QWidget,Ui_Settings):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.fileJson = "Settings.Conf"
        try:
            self.con = connect()
            self.ShowInfoOnForm()
        except:pass

        self.labCheckDB.mousePressEvent = self.CheckConnectDB
        self.labCheckFTP.mousePressEvent = self.CheckConnectFtp
        self.btnSave.clicked.connect(self.SaveInformation)

        self.labRunServer.mousePressEvent   = self.RunServer


    # Function Run Server Chat
    def RunServer(self,e):
        import Server as ServerChat
        self.Server = ServerChat.ServerDlg()
        self.labRunServer.setEnabled(False)

    def ShowInfoOnForm(self):
        with open(self.fileJson,'r') as file:
            Settings = json.load(file)
        DB           = Settings['Settings']['DB']
        FTP          = Settings['Settings']['FTP']
        InfoEmail    = Settings['Settings']['InfoEmail']
        Info         = Settings['Settings']['Info']
        InfoSettings = Settings['Settings']['InfoSettings']

        # Information Database
        self.textHostDB.setText(DB['Host'])
        self.textUserDB.setText(DB['Username'])
        self.textPassDB.setText(DB['password'])
        self.textNameDB.setText(DB['Name'])

        # Information FTP
        self.textHostFTP.setText(FTP['Host'])
        self.textUserFTP.setText(FTP['Username'])
        self.textPassFTP.setText(FTP['Password'])

        # Information Email Address
        self.textEmail.setText(InfoEmail['Email'])
        self.textPassEmail.setText(InfoEmail['Password'])
        self.textPassEmail.setEchoMode(QLineEdit.Password)



        # Infor Genrall
        self.comBoxCategory.addItem(Info['Category'])
        category = self.con.select('SectionName','section')
        for i in category:
            self.comBoxCategory.addItem(i[0])

        theme    = Info['Theme']
        if theme == 'Theme/qtPyDark.qss':
            self.ComBoxTheme.setItemText(0,self.ComBoxTheme.itemText(0))
        else:
            self.ComBoxTheme.setItemText(0, self.ComBoxTheme.itemText(1))
            self.ComBoxTheme.setItemText(1, 'الافتراضي'.decode())

    def CheckConnectDB(self,e):
        user = str(self.textUserDB.text())
        pwd  = str(self.textPassDB.text())
        Host = str(self.textHostDB.text())
        Name = str(self.textNameDB.text())
        try:
            con = MySQLdb.connect(Host,user,pwd,Name)
            QMessageBox.information(self,'التحقق من معلومات الاتصال'.decode(),'المعلومات التي ادخلتها صحيحه'.decode())
            con.close()
        except:
            QMessageBox.critical(self,'التحقق من معلومات االتصال'.decode(),'معلومات الاتصال التي ادخلتها غير صحيحه'.decode())

    def CheckConnectFtp(self,e):
        HostFTP = str(self.textHostFTP.text())
        UserFTP = str(self.textUserFTP.text())
        PwdFtp  = str(self.textPassFTP.text())
        try:
            ftp = ftplib.FTP(HostFTP,UserFTP,PwdFtp)
            QMessageBox.information(self, 'التحقق من معلومات الاتصال'.decode(), 'المعلومات التي ادخلتها صحيحه'.decode())
            ftp.close()
        except:
            QMessageBox.critical(self, 'التحقق من معلومات االتصال'.decode(),
                                 'معلومات الاتصال التي ادخلتها غير صحيحه'.decode())



    def SaveInformation(self):
        with open(self.fileJson,'r') as file:
            Settings = json.load(file)
        DB        = Settings['Settings']['DB']
        FTP       = Settings['Settings']['FTP']
        InfoEmail = Settings['Settings']['InfoEmail']
        Info      = Settings['Settings']['Info']
        InfoSettings = Settings['Settings']['InfoSettings']

        # Information Database
        DB['Host']     = str(self.textHostDB.text())
        DB['Username'] = str(self.textUserDB.text())
        DB['password'] = str(self.textPassDB.text())
        DB['Name']     = str(self.textNameDB.text())

        # Information FTP
        FTP['Host']     = str(self.textHostFTP.text())
        FTP['Username'] = str(self.textUserFTP.text())
        FTP['Password'] = str(self.textPassFTP.text())

        # Information Email Address
        InfoEmail['Email']    = str(self.textEmail.text())
        InfoEmail['Password'] = str(self.textPassEmail.text())

        if  self.textUsername.text() != "" or  self.textPassword.text() != "":
            InfoSettings['Username']  = hashlib.sha1(self.textUsername.text()).hexdigest()
            InfoSettings['Password']  = hashlib.sha1(self.textPassword.text()).hexdigest()

        # Information
        Info['Category']  = str(self.comBoxCategory.currentText()).decode()
        com = str(self.ComBoxTheme.currentText())
        if com == 'الافتراضي':
            Info['Theme'] = 'Theme/qtPyDark.qss'
        else:
            Info['Theme'] = 'Theme/default.qss'

        try:
            with open(self.fileJson,'w') as f:
                f.write(json.dumps(Settings, ensure_ascii=False))
            QMessageBox.information(self,'حفظ البينات'.decode(),'تم حفظ البينات '.decode())
        except:
            QMessageBox.critical(self,'حفظ البينات'.decode(),'حدث خلل اثناء حفظ الاعدادات الرجاء المحاوله في وقت اخر'.decode())








