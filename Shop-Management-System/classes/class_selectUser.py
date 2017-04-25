#_*_ coding:utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.selectUser import *
from connect import *
from connectFtp import *
import  urllib
class selectUser(QWidget,Ui_SelectUser):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableSelectUser.setEditTriggers(QHeaderView.NoEditTriggers)
        self.tableSelectUser.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableSelectUser.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.con = connect()
        self.conFTP = connectFtp()


        self.textUserSearcch.keyReleaseEvent = self.searchUserSelect
        self.tableSelectUser.doubleClicked.connect(self.ClickTableAndSelect)

    # Function Show User
    def ShowUser(self):
        infos = self.con.select("*", "User", "Active = 0")
        lenght = len(infos)
        self.tableSelectUser.setRowCount(lenght)
        row = 0
        for info in infos:
            """[ Set Item ]"""
            self.tableSelectUser.setItem(row,0,QTableWidgetItem(str(info[0]).decode()))
            self.tableSelectUser.setItem(row,1, QTableWidgetItem(str(info[1]).decode()))
            self.tableSelectUser.setItem(row,2,QTableWidgetItem(str(info[6]).decode()))
            self.tableSelectUser.setItem(row,3,QTableWidgetItem(str(info[4]).decode()))

            """[ Tool Tip ]"""
            self.tableSelectUser.item(row,1).setToolTip(str(info[1]).decode("utf-8"))
            self.tableSelectUser.item(row, 2).setToolTip(str(info[6]).decode("utf-8"))
            self.tableSelectUser.item(row, 3).setToolTip(str(info[4]).decode("utf-8"))
            row+=1

    #  Function Search User In Database
    def searchUserSelect(self,e):
        Search  = str(self.textUserSearcch.text())
        if Search == "" or Search == " ":self.ShowUser()
        like = "FullName LIKE '%{0}%' OR Email LIKE '%{1}%'  OR   NumberID LIKE '%{2}%' ".format(Search,Search,Search)
        sql = """SELECT * FROM user WHERE ({0}) AND Active = 0 """.format(like)
        con = self.con.con  # Variable Connect Database
        con = con.cursor()
        con.execute(sql)
        SearchResult = con.fetchall()
        lenght = len(SearchResult)
        self.tableSelectUser.setRowCount(lenght)
        row = 0
        for info in SearchResult:
            """[ Set Item ]"""
            self.tableSelectUser.setItem(row,0,QTableWidgetItem(str(info[0]).decode()))
            self.tableSelectUser.setItem(row,1, QTableWidgetItem(str(info[1]).decode()))
            self.tableSelectUser.setItem(row,2,QTableWidgetItem(str(info[6]).decode()))
            self.tableSelectUser.setItem(row,3,QTableWidgetItem(str(info[4]).decode()))

            """[ Tool Tip ]"""
            self.tableSelectUser.item(row,1).setToolTip(str(info[1]).decode("utf-8"))
            self.tableSelectUser.item(row, 2).setToolTip(str(info[6]).decode("utf-8"))
            self.tableSelectUser.item(row, 3).setToolTip(str(info[4]).decode("utf-8"))
            row+=1

    # Function Cick Tabel And Select Table
    def ClickTableAndSelect(self):
        import classes.class_addUsers
        self.infoUser = classes.class_addUsers.addUser()
        self.infoUser.btnEditUser.setEnabled(True)
        Row    = self.tableSelectUser.currentRow()
        UserID = str(self.tableSelectUser.item(Row,0).text())
        info = self.con.select("*", "User", "UserID = '{0}' ".format(UserID),2)
        self.infoUser.textFullName.setText(str(info[1]).decode())
        self.infoUser.textNumberID.setText(str(info[6]).decode())
        self.infoUser.textUsername.setText(str(info[2]).decode())
        self.infoUser.textNumberPhone.setText(str(info[5]).decode())
        self.infoUser.textEmail.setText(str(info[4]).decode())
        self.infoUser.labUserPassword.setText(str(info[3]).decode())
        self.infoUser.labImageName.setText(str(info[10]).decode())
        self.infoUser.labUserID.setText(str(info[0]))
        if str(info[11]).decode() == 'ذكر':
            sex = 1
        else:sex = 2
        self.infoUser.comboxSex.setCurrentIndex(sex)
        pathImage = "http://" + self.conFTP.HOSTFTP + "/Home/" + self.conFTP.NameFile + "/Users/" + str(info[10])
        openUrl = urllib.urlopen(pathImage).read()
        pixmap = QPixmap()
        pixmap.loadFromData(openUrl)
        self.infoUser.labAddImgUser.setPixmap(pixmap)
        checkBoxPermission = {1: self.infoUser.checkBoxCalc, 2: self.infoUser.checkBoxChat,
                              11: self.infoUser.checkBoxSSection, 12: self.infoUser.checkBoxSStor, 201: self.infoUser.checkBoxSection,
                              21: self.infoUser.checkBoxAddItem, 22: self.infoUser.checkBoxSItem, 23: self.infoUser.checkBoxSCatecory,
                              203: self.infoUser.checkBoxItem,
                              31: self.infoUser.checkBoxSCust, 204: self.infoUser.checkBoxCust,
                              41: self.infoUser.checkBoxSEmployee, 205: self.infoUser.checkBoxEmployee,
                              51: self.infoUser.checkBoxAddUser, 52: self.infoUser.checkBoxViewUser, 206: self.infoUser.checkBoxUsers}
        NumberPermission = str(info[7]).split(',')
        try:
            for checkBox in NumberPermission:
                checkBoxPermission[int(checkBox)].setChecked(True)
        except:pass
        self.infoUser.btnAddUser.setEnabled(False)
        self.close()
        self.infoUser.show()





