#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time

"""
Class Content All Function Of Window Section
"""
class funClassSection():

    # Function Add Section To Database
    def addSection(self):
        UserID      = self.labUserID.text()
        nameSection = self.lineEditSectionName.text()
        date        = time.strftime("%Y-%m-%d %H:%M:%S")
        checkValue = self.con.checkData("Section","SectionName","'{0}'".format(nameSection))
        if not nameSection:
            QMessageBox.critical(self ,'اظافة قسم'.decode('UTF-8'),'ادخل اسم القسم الذي \n تود اظافته'
                                 .decode('UTF-8'))
        elif checkValue == True:
            QMessageBox.critical(self ,'اظافة قسم'.decode('UTF-8'),'اسم القسم الذي ادخلته موجود '
                                 .decode('UTF-8'))
        else:
            data = "'{0}','{1}','{2}'".format(nameSection,date,UserID)
            """function insert  be of  Class connect"""
            addSection = self.con.insert("Section","`SectionName`,`DateAdd`,`UserID`",data)
            if addSection:
                QMessageBox.information(self, 'اظافة قسم'.decode('UTF-8'), ' تم اظافة قسم {0} بنجاح '.format(nameSection)
                                     .decode('UTF-8'))
                self.ShowSection()

    """
    Function Show Section
    Import All Section Of Database And View Section On Form Section
    """
    def ShowSection(self):
        # Vairable Connect Database Content On Function ConnectDB
        con = self.con.con;
        con = con.cursor()
        sql = """
        SELECT
            Section.* , User.FullName
        FROM
            Section
        INNER JOIN
            User
        ON
            Section.UserID = User.UserID
        WHERE Section.ActiveSection = 1 ORDER BY SectionID DESC
        """

        con.execute(sql)
        # Fetch All Date Of Database
        infoSection = con.fetchall()
        lengthDate = len(infoSection)
        # Determination Number Row Of Table
        self.labNumberSection.setText(str(lengthDate))
        self.tableSection.setRowCount(lengthDate)
        Row = 0
        for info in infoSection:
            # Check Number Row IF greater than Of length Data Break Of Statment For
            if Row >=lengthDate :break
            # Insert Date To Table
            self.tableSection.setItem(Row,0,QTableWidgetItem(str(info[0])))
            self.tableSection.setItem(Row, 1, QTableWidgetItem(str(info[1]).decode("UTF-8")))
            self.tableSection.setItem(Row, 2, QTableWidgetItem(str(info[2])))
            self.tableSection.setItem(Row,3, QTableWidgetItem(str(info[5]).decode("UTF-8")))
            Row+=1 # Incriminate One To Variable Row

    """
    Function Delete Section
    """
    def DeletSection(self):
        if self.tableSection.selectedItems():
            MsgDelete = QMessageBox.information(self,'الغاء القسم'.decode("UTF-8"),'هل انت متئكد من الغاء القسم اذا تم الغاء \n القسم سوف يتم الغاء جميع الاصناف التابعه له'.decode("UTF-8"),
                                                QMessageBox.Ok|QMessageBox.No,QMessageBox.No)
            if MsgDelete == QMessageBox.Ok:
                Row = self.tableSection.currentRow()
                SectionID = self.tableSection.item(Row,0).text()
                result = self.con.update('Section','`ActiveSection` = 0',"SectionID = {0}".format(SectionID))
                if result:
                    self.con.update('Category','`ActiveCAtegory` = 0','SectionID = {0}'.format(SectionID))
                    QMessageBox.information(self, 'حذف القسم'.decode("UTF-8"),
                                                        'تم الغاء القسم بنجاخ'.decode("UTF-8"))
                    self.ShowSection()
                else:
                    QMessageBox.information(self, 'حذف القسم'.decode("UTF-8"),
                                                        'حدث خلل في الغاء القسم الرجاء المحاوله في وقت اخر'.decode("UTF-8"))
        else:
            QMessageBox.information(self,'حذف القسم'.decode("UTF-8"),'يجب تحديد القسم الذي تود الغائه'.decode("UTF-8"))

    """
    Function Edit Section Edit Section Consist 2 Function One Function
    Import Number Row Section Workers Edit Function Tow Check Vablie
    And Edit Section
    """
    def ImportSectionToLineEdit(self,table): # Function One
        self.btnEditSection.setEnabled(True)
        self.btnAddSection.setEnabled(False)
        self.btnSectionDelete.setEnabled(False)
        self.linEditSectionSearch.setEnabled(False)
        self.tableSection.setEnabled(False)
        SectionName = self.tableSection.item(table.row(),1).text()
        self.lineEditSectionName.setText(SectionName)
        self.rowSection =  table.row()

    def EditSection(self): # Function Tow
        SectionID   = self.tableSection.item(self.rowSection,0).text()
        SectionNameOld = self.tableSection.item(self.rowSection, 1).text()
        SectionNameNew = self.lineEditSectionName.text()
        value = "SectionName = '{0}'".format(SectionNameNew)
        if not SectionNameNew:
            QMessageBox.critical(self, 'تعديل القسم'.decode('UTF-8'),
                                  'اكتوب اسم القسم الجديد'.decode('UTF-8').format(
                                     SectionName))
        else:
            CheckSectionName = self.con.checkData("Section","`SectionName`","'{0}'".format(SectionNameNew))
            if CheckSectionName == False:
                result = self.con.update("Section",value,"SectionID = {0}".format(SectionID))
                if result:
                   QMessageBox.information(self,'تعديل القسم'.decode('UTF-8'),'تم تعديل قسم [ {0} ] الى قسم [ {1} ] بنجاح '.decode('UTF-8').format(SectionNameOld,SectionNameNew))
                   self.ShowSection()
                else:
                   QMessageBox.critical(self, 'تعديل القسم'.decode('UTF-8'),
                                           'حدث خلل اثناء تعديل  قسم [ {0} ] الرجاء \n في وقة اخر  '.decode('UTF-8').format(SectionNameOld))
            else:
                QMessageBox.information(self, 'تعديل القسم'.decode('UTF-8'),
                                        'هاذا الاسم القديم للقسم الرجاء ادخال الاسم الجديد ليتم تعديله  '.decode('UTF-8'))
            self.Cancel()

    """
    Function Cancel
    """
    def Cancel(self):
        self.btnEditSection.setEnabled(False)
        self.btnAddSection.setEnabled(True)
        self.btnSectionDelete.setEnabled(True)
        self.linEditSectionSearch.setEnabled(True)
        self.tableSection.setEnabled(True)
        self.lineEditSectionName.clear()

    """
    Function Search Of Section Make Search By Name Section Or ID Section Or ID User Or Name User Or Date Add
    """
    def SearchSection(self,even):
        Search = self.linEditSectionSearch.text()
        # if Form Search Empty Run Function ShowSection Import All Section Of Database
        if  Search == "" or Search == " " or not Search:
            self.ShowSection()
        else:
            like = "Section.SectionID LIKE '%{0}%' OR Section.SectionName LIKE '%{1}%' OR Section.DateAdd LIKE '%{2}%' OR User.FullName LIKE '%{3}%'".format(Search,Search,Search,Search)
            sql = "SELECT Section.*,User.FullName FROM Section INNER JOIN User ON Section.UserID = User.UserID WHERE ({0}) AND ActiveSection = 1".format(like)
            con = self.con.con # Variable Connect Database
            con = con.cursor()
            con.execute(sql)
            SearchResult = con.fetchall()
            lenghtData = len(SearchResult)
            self.tableSection.setRowCount(int(lenghtData))
            Row = 0 # Number Row Of Table
            # Insert Search Result Of Table Section
            for info in SearchResult:
                if Row > lenghtData:break
                self.tableSection.setItem(Row,0,QTableWidgetItem(str(info[0])))
                self.tableSection.setItem(Row,1,QTableWidgetItem(str(info[1]).decode("UTF-8")))
                self.tableSection.setItem(Row,2,QTableWidgetItem(str(info[2])))
                self.tableSection.setItem(Row,3,QTableWidgetItem(str(info[4]).decode("UTF-8")))
                Row+=1 # Incrimiate Steb By 1