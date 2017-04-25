#_*_ coding:utf8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib
class funViewUser:

    def ShowUsers(self):
        ActiveUser = str(self.comboBoxActive.currentText())
        if ActiveUser == 'المستخدمين الفعالين':
            Active = 0
            self.btnActiveUser.setEnabled(False)
            self.btnNotActiveUser.setEnabled(True)
        else:
            Active = 1
            self.btnNotActiveUser.setEnabled(False)
            self.btnActiveUser.setEnabled(True)

        infos = self.con.select("*", "User", "Active = '{0}' and UserID !=1".format(Active), 0)
        lenght = len(infos)
        self.tableViewUsers.setRowCount(lenght)
        self.NumberUser.setText(str(lenght))
        row = 0
        for info in infos:
            """[ Set Item ]"""
            self.tableViewUsers.setItem(row,0,QTableWidgetItem(str(info[0]).decode()))
            self.tableViewUsers.setItem(row,1, QTableWidgetItem(str(info[1]).decode()))
            self.tableViewUsers.setItem(row,2,QTableWidgetItem(str(info[4]).decode()))
            self.tableViewUsers.setItem(row,3,QTableWidgetItem(str(info[5]).decode()))
            self.tableViewUsers.setItem(row,4,QTableWidgetItem(str(info[6]).decode()))
            self.tableViewUsers.setItem(row,5,QTableWidgetItem(str(info[8]).decode()))
            """[ Tool Tip ]"""
            self.tableViewUsers.item(row,1).setToolTip(str(info[1]).decode("utf-8"))
            self.tableViewUsers.item(row, 2).setToolTip(str(info[4]).decode("utf-8"))
            self.tableViewUsers.item(row, 3).setToolTip(str(info[5]).decode("utf-8"))
            self.tableViewUsers.item(row, 4).setToolTip(str(info[6]).decode("utf-8"))
            self.tableViewUsers.item(row, 5).setToolTip(str(info[8]).decode("utf-8"))
            row+=1

    # Show Images User On Form
    def ShowImageUser(self):
        try:
            Row = self.tableViewUsers.currentRow()
            UserID = self.tableViewUsers.item(Row,0).text()
            img    = self.con.select('img','user','UserID = {0}'.format(UserID),2)[0]
            url = "http://" + self.conFTP.HOSTFTP + "/Home/" + self.conFTP.NameFile + "/Users/" + img
            data = urllib.urlopen(url).read()
            imageUser = QPixmap()
            imageUser.loadFromData(data)
            self.labShowImagesUser.setPixmap(imageUser)
        except:
            self.labShowImagesUser.setPixmap(QPixmap(":/images/users.png"))

    # Function Active User And Not Active User
    def activeUser(self):
        if self.tableViewUsers.selectedItems():
            active = str(self.comboBoxActive.currentText())
            Row = self.tableViewUsers.currentRow()
            UserID = self.tableViewUsers.item(Row,0).text()
            if active == 'المستخدمين الفعالين':
                Active = 1
                self.btnActiveUser.setEnabled(False)
                self.btnNotActiveUser.setEnabled(True)
                msg = 'تم الغاء تفعيل العميل بنجاح'
            else:
                Active = 0
                self.btnNotActiveUser.setEnabled(False)
                self.btnActiveUser.setEnabled(True)
                msg = "تم تفعيل العميل بنجاح"


            update = self.con.update('user','`Active`={}'.format(Active),"UserID = {}".format(UserID))
            if update:
                QMessageBox.information(self,'المستخدمين'.decode(),'{}'.decode().format(msg))
            else:
                QMessageBox.critical(self,'المستخدمين'.decode(),'لقج حدث مشكله غير متوقعه الرجاء المحاوله في وقت اخر'.decode())
            self.ShowUsers()
        else:
            QMessageBox.critical(self, 'المستخدمين'.decode(),
                                    'الرجاء تحديد المستخدم'.decode())