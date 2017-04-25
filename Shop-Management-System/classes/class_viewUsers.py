#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.viewUsers import *
from funcClasses.funClassViewUser import *
from connect import *
from connectFtp import *

class viewUsers(QWidget,Ui_viewUsers,funViewUser):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableViewUsers.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableViewUsers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewUsers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewUsers.setColumnHidden(0,True)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.con = connect()
        self.conFTP = connectFtp()
        self.ShowUsers()


        """[ Start Event Function  ]"""
        self.comboBoxActive.activated.connect(self.ShowUsers)
        self.tableViewUsers.itemSelectionChanged.connect(self.ShowImageUser)
        self.btnNotActiveUser.clicked.connect(self.activeUser)
        self.btnActiveUser.clicked.connect(self.activeUser)
        self.textSearch.keyReleaseEvent = self.SearchUser
        """[ End Event Function ]"""

    def SearchUser(self,e):
        ActiveUser = str(self.comboBoxActive.currentText())
        Search  = str(self.textSearch.text())
        if ActiveUser == 'المستخدمين الفعالين':Active = 0
        else:Active = 1
        if Search == "" or Search == " ":self.ShowUsers()

        like = "FullName LIKE '%{0}%' OR Email LIKE '%{1}%'  OR  PhoneNumber LIKE '%{2}%' OR NumberID LIKE '%{3}%' OR DataRegister LIKE '%{4}%'".format(Search,Search,Search,Search,Search)
        sql = """SELECT * FROM user WHERE (({0}) AND Active = {1}) """.format(like,Active)
        print sql
        con = self.con.con  # Variable Connect Database
        con = con.cursor()
        con.execute(sql)
        SearchResult = con.fetchall()
        lenght = len(SearchResult)
        self.tableViewUsers.setRowCount(lenght)
        self.NumberUser.setText(str(lenght))
        row = 0
        for info in SearchResult:
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

