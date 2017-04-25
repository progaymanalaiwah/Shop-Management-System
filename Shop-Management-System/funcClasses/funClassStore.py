#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class funClassStore():
    """
    Function Add Category To Database
    """
    def addStore(self):
        nameStore = self.lineEditStoreName.text()
        if not nameStore:
            QMessageBox.critical(self ,'اظافة مخزن'.decode('UTF-8'),'ادخل اسم المخزن الذي \n تود اظافته'
                                 .decode('UTF-8'))
            return False
        checkValue = self.con.checkData("Store", "StoreName", "'{0}'".format(nameStore))
        if checkValue == True:
            QMessageBox.critical(self ,'اظافة مخزن'.decode('UTF-8'),'اسم المخزن الذي ادخلته موجود  او قد يكون غير مفعل '
                                 .decode('UTF-8'))
        else:
            data = "'{0}'".format(nameStore)
            """function insert  be of  Class connect"""
            addStore = self.con.insert("`Store`","`StoreName`",data)
            if addStore:
                QMessageBox.information(self, 'اظافة مخزن'.decode('UTF-8'), ' تم اظافة مخزن {0} بنجاح '.format(nameStore)
                                     .decode('UTF-8'))
                self.ShowStore()
                self.Cancel()


    """
    Function Show Section
    Import All Category Of Database And View Category On Form Category
    """
    def ShowStore(self):
        # Vairable Connect Database Content On Function ConnectDB
        con = self.con.con;
        con = con.cursor()
        sql = """
        SELECT
            *
        FROM
            Store
        WHERE ActiveStore = 1 ORDER BY StoreID DESC
        """

        con.execute(sql)
        # Fetch All Date Of Database
        infoStore = con.fetchall()
        lengthDate = len(infoStore)
        # Determination Number Row Of Table
        self.labNumberStore.setText(str(lengthDate))
        self.tableStore.setRowCount(lengthDate)
        Row = 0
        for info in infoStore:
            # Check Number Row IF greater than Of length Data Break Of Statment For
            if Row >=lengthDate :break
            # Insert Date To Table
            self.tableStore.setItem(Row,0,QTableWidgetItem(str(info[0])))
            self.tableStore.setItem(Row, 1, QTableWidgetItem(str(info[1]).decode("UTF-8")))

            Row+=1 # Incriminate One To Variable Row

    """
    Function Not Activate Store Of Database
    """
    def notActivateStore(self):
        if self.tableStore.selectedItems():
            MsgDelete = QMessageBox.information(self,'الغاء المخزن'.decode("UTF-8"),'هل انت متئكد من الغاء المخزن اذا تم الغاء \n المخزن سوف يتم الغاء جميع المواد التابعه له'.decode("UTF-8"),
                                                QMessageBox.Ok|QMessageBox.No,QMessageBox.No)
            if MsgDelete == QMessageBox.Ok:
                Row = self.tableStore.currentRow()
                CategoryID = self.tableStore.item(Row,0).text()
                result = self.con.update('Store','`ActiveStore` = 0','StoreID = {0}'.format(CategoryID))
                if result:
                    QMessageBox.information(self, 'الغاء المخزن'.decode("UTF-8"),
                                              'تم الغاء المخزن بنجاح'.decode("UTF-8"))
                    self.ShowStore()
                else:
                    QMessageBox.information(self, 'الغاء الصنف'.decode("UTF-8"),
                                                        'حدث خلل في الغاء المخزن الرجاء المحاوله في وقت اخر'.decode("UTF-8"))
        else:
            QMessageBox.information(self,'الغاء المخزن'.decode("UTF-8"),'يجب تحديد المخزن الذي تود الغائه'.decode("UTF-8"))


    """
    Function Search Of Section Make Search By Name Section Or ID Section Or ID User Or Name User Or Date Add
    """
    def SearchStore(self,even):
        Search = self.lineEditStoreSearch.text()
        # if Form Search Empty Run Function ShowSection Import All Section Of Database
        if  Search == "" or Search == " " or not Search:
            self.ShowStore()

        else:
            like = "StoreID LIKE '%{0}%' OR StoreName LIKE '%{1}%'".format(Search,Search)
            sql = """SELECT * FROM Store WHERE ({0}) AND ActiveStore = 1""".format(like)
            con = self.con.con # Variable Connect Database
            con = con.cursor()
            con.execute(sql)
            SearchResult = con.fetchall()
            lenghtData = len(SearchResult)
            self.tableStore.setRowCount(int(lenghtData))
            Row = 0 # Number Row Of Table
            # Insert Search Result Of Table Section
            for info in SearchResult:
                if Row > lenghtData:break
                self.tableStore.setItem(Row,0,QTableWidgetItem(str(info[0])))
                self.tableStore.setItem(Row,1,QTableWidgetItem(str(info[1]).decode("UTF-8")))
                Row+=1 # Incrimiate Steb By 1

    def ImportStoreToLineEdit(self,table): # Function One
        self.btnStoreEdit.setEnabled(True)
        self.btnStoreAdd.setEnabled(False)
        self.btnStoreDelete.setEnabled(False)
        self.lineEditStoreSearch.setEnabled(False)
        self.tableStore.setEnabled(False)
        storeName = self.tableStore.item(table.row(),1).text()
        self.lineEditStoreName.setText(storeName)
        self.rowStore =  table.row()

    def EditStore(self): # Function Tow
        StoreID   = self.tableStore.item(self.rowStore,0).text()
        StoreNameOld = self.tableStore.item(self.rowStore, 1).text()
        StoreNameNew = self.lineEditStoreName.text()
        value = "`StoreName` = '{0}'".format(StoreNameNew)
        if not StoreNameNew:
            QMessageBox.critical(self, 'تعديل المخون'.decode('UTF-8'),
                                  'اكتوب اسم المخزن الجديد'.decode('UTF-8'))
        else:
            CheckStoreName = self.con.checkData("Store","StoreName","'{0}'".format(StoreNameNew))
            if CheckStoreName == False:
                result = self.con.update("Store",value,"StoreID = {0}".format(StoreID))
                if result:
                   QMessageBox.information(self,'تعديل المخزن'.decode('UTF-8'),'تم تعديل مخزن [ {0} ] الى مخزن [ {1} ] بنجاح '.decode('UTF-8').format(StoreNameOld,StoreNameNew))
                   self.ShowStore()
                   self.Cancel()
                else:
                   QMessageBox.critical(self, 'تعديل القسم'.decode('UTF-8'),
                                           'حدث خلل اثناء تعديل  قسم [ {0} ] الرجاء \n في وقة اخر  '.decode('UTF-8').format(StoreNameOld))
                   self.Cancel()
            else:
                QMessageBox.information(self, 'تعديل المخزن'.decode('UTF-8'),
                                        'هاذا الاسم القديم المخزن الرجاء ادخال الاسم الجديد ليتم تعديله  '.decode('UTF-8'))

    """
    Function Cancel
    """
    def Cancel(self):
        self.btnStoreEdit.setEnabled(False)
        self.btnStoreAdd.setEnabled(True)
        self.btnStoreDelete.setEnabled(True)
        self.lineEditStoreSearch.setEnabled(True)
        self.tableStore.setEnabled(1)
        self.lineEditStoreName.clear()