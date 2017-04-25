#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.SettingItem import *
from funcClasses.funClassSettingItem import *
from connect import *
from connectFtp import *

class settingItem(QWidget,Ui_SettingItem,funClassSettingItem):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableSettingItem.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableSettingItem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSettingItem.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSettingItem.setColumnHidden(0,True)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

        # Object Of Class Connect
        self.con = connect()

        self.connectFTP = connectFtp()
        # Function Show Item
        self.ShowItem()
        """[ Start Event ]"""
        self.comboxShowItem.activated.connect(self.ShowItem)
        self.btnNotActive.clicked.connect(self.Active)
        self.btnActive.clicked.connect(self.Active)
        self.tableSettingItem.doubleClicked.connect(self.EditItem)
        self.lineEditSearchItem.keyReleaseEvent = self.SearchItem

        """[ End Event ]"""


    def SearchItem(self,e):
       SearchWord = self.lineEditSearchItem.text()
       ActiveCategory = 1
       if str(self.comboxShowItem.currentText()) == 'المنتجات الفعاله':
           ActiveCategory = 1
       else:
           ActiveCategory = 0
       # if Form Search Empty Run Function ShowSection Import All Section Of Database
       if SearchWord == "" or SearchWord == " " or not SearchWord:
           self.ShowItem()
       else:
           like = "Category.CategoryName LIKE '%{0}%' OR store.StoreName LIKE '%{1}%' OR User.FullName LIKE '%{2}%' OR 	ItemName  LIKE '%{3}%' OR 	Price  LIKE '%{4}%' OR 	Quentity  LIKE '%{5}%' OR 	DateOfProduction  LIKE '%{6}%' OR CompletionDate  LIKE '%{7}%' OR item.DateAdd  LIKE '%{8}%' ".format(SearchWord,SearchWord,SearchWord,SearchWord,SearchWord,SearchWord,SearchWord,SearchWord,SearchWord)
           sql = """SELECT item.*,User.FullName,Category.CategoryName,store.StoreName  FROM item INNER JOIN User ON item.UserID = User.UserID INNER JOIN Category ON item.CategoryID = Category.CategoryID  INNER JOIN store ON item.StoreID = store.StoreID WHERE ({0}) AND ActiveCategory = {1}""".format(
               like,ActiveCategory)
           con = self.con.con  # Variable Connect Database
           con = con.cursor()
           con.execute(sql)
           SearchResult = con.fetchall()
           lenghtData = len(SearchResult)
           self.tableSettingItem.setRowCount(int(lenghtData))
           self.labNumberItem.setText(str(lenghtData))
           Row = 0  # Number Row Of Table
           # Insert Search Result Of Table Section
           for info in SearchResult:
               if Row > lenghtData: break
               self.tableSettingItem.setItem(Row, 1, QTableWidgetItem(str(info[1]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 2, QTableWidgetItem(str(info[13]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 3, QTableWidgetItem(str(info[14]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 4, QTableWidgetItem(str(info[7]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 5, QTableWidgetItem(str(info[5]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 6, QTableWidgetItem(str(info[6]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 7, QTableWidgetItem(str(info[2]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 8, QTableWidgetItem(str(info[3]).decode("UTF-8")))
               self.tableSettingItem.setItem(Row, 9, QTableWidgetItem(str(info[12]).decode("UTF-8")))
               Row += 1  # Incrimiate Steb By 1
