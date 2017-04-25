#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time

class funClassCategory():

    # Function View All Section Of Combox
    def viewSection(self):
        DateSection = self.con.select("SectionName","Section","ActiveSection=1")
        # Works On Empty Item First
        self.comboxShowSection.addItem("اختر القسم".decode("utf-8"))
        for item in DateSection:
            data = str(item[0]).decode("utf-8")
            self.comboxShowSection.addItem(data)

    """
    Function Add Category To Database
    """
    def addCategory(self):
        UserID      = self.labUserID.text()
        nameCategory = self.lineEditCategoryName.text()
        SectionName   = str(self.comboxShowSection.currentText())
        print "[ "+ SectionName + " ]"
        date        = time.strftime("%Y-%m-%d %H:%M:%S")
        checkValue = self.con.checkData("Category","CategoryName","'{0}'".format(nameCategory))
        if not nameCategory:
            QMessageBox.critical(self ,'اظافة قسم'.decode('UTF-8'),'ادخل اسم القسم الذي \n تود اظافته'
                                 .decode('UTF-8'))
        elif SectionName == "اختر القسم" or SectionName == "" or SectionName == " ":
            QMessageBox.critical(self ,'اظافة قسم'.decode('UTF-8'),'الرجاء اختيار القسم الذي تود اظافة صنف [ {0} ] اليه'
                                 .format(nameCategory).decode('UTF-8'))
        elif checkValue == True:
            QMessageBox.critical(self ,'اظافة قسم'.decode('UTF-8'),'اسم القسم الذي ادخلته موجود '
                                 .decode('UTF-8'))
        else:
            SectionID = self.con.select("`SectionID`","Section","SectionName = '{0}'".format(SectionName),2)
            SectionID =  SectionID[0]
            data = "'{0}','{1}','{2}','{3}'".format(nameCategory,date,SectionID,UserID)
            """function insert  be of  Class connect"""
            addSection = self.con.insert("Category","`CategoryName`,`DateAdd`,`SectionID`,`UserID`",data)
            if addSection:
                QMessageBox.information(self, 'اظافة قسم'.decode('UTF-8'), ' تم اظافة قسم {0} بنجاح '.format(nameCategory)
                                     .decode('UTF-8'))
                self.ShowCategory()
                self.Cancel()
            self.comboxShowSection.setItemText(0, ("اختر القسم".decode("utf-8")))




    """
    Function Show Section
    Import All Category Of Database And View Category On Form Category
    """
    def ShowCategory(self):
        # Vairable Connect Database Content On Function ConnectDB
        con = self.con.con;
        con = con.cursor()
        sql = """
        SELECT
            Category.* , User.FullName,Section.SectionName
        FROM
            Category
        INNER JOIN
            User
        ON
            Category.UserID = User.UserID
        INNER JOIN Section
        ON
        Category.SectionID = Section.SectionID
        WHERE Category.ActiveCategory = 1 ORDER BY Category.CategoryID DESC
        """

        con.execute(sql)
        # Fetch All Date Of Database
        infoCategory = con.fetchall()
        lengthDate = len(infoCategory)
        # Determination Number Row Of Table
        self.labNumberSection.setText(str(lengthDate))
        self.tableCategory.setRowCount(lengthDate)
        Row = 0
        for info in infoCategory:
            # Check Number Row IF greater than Of length Data Break Of Statment For
            if Row >=lengthDate :break
            # Insert Date To Table
            self.tableCategory.setItem(Row,0,QTableWidgetItem(str(info[0])))
            self.tableCategory.setItem(Row, 1, QTableWidgetItem(str(info[1]).decode("UTF-8")))
            self.tableCategory.setItem(Row, 2, QTableWidgetItem(str(info[7]).decode("UTF-8")))
            self.tableCategory.setItem(Row, 3, QTableWidgetItem(str(info[2]).decode("UTF-8")))

            self.tableCategory.setItem(Row, 4, QTableWidgetItem(str(info[6]).decode("UTF-8")))
            Row+=1 # Incriminate One To Variable Row

    """
    Function Delete Category
    """
    def DeletCategory(self):
        if self.tableCategory.selectedItems():
            MsgDelete = QMessageBox.information(self,'الغاء الصنف'.decode("UTF-8"),'هل انت متئكد من الغاء الصنف اذا تم الغاء \n الصنف سوف يتم الغاء جميع المواد التابعه له'.decode("UTF-8"),
                                                QMessageBox.Ok|QMessageBox.No,QMessageBox.No)
            if MsgDelete == QMessageBox.Ok:
                Row = self.tableCategory.currentRow()
                CategoryID = self.tableCategory.item(Row,0).text()
                result = self.con.update('Category','`ActiveCategory` = 0','CategoryID = {0}'.format(CategoryID))
                if result:
                    QMessageBox.information(self, 'الغاء الصنف'.decode("UTF-8"),
                                              'تم الغاء الصنف بنجاخ'.decode("UTF-8"))
                    self.ShowCategory()
                else:
                    QMessageBox.information(self, 'حذف الصنف'.decode("UTF-8"),
                                                        'حدث خلل في الغاء الصنف الرجاء المحاوله في وقت اخر'.decode("UTF-8"))
        else:
            QMessageBox.information(self,'حذف الصنف'.decode("UTF-8"),'يجب تحديد الصنف الذي تود الغائه'.decode("UTF-8"))



    """
    Function Edit Section Edit Section Consist 2 Function One Function
    Import Number Row Section Workers Edit Function Tow Check Vablie
    And Edit Section
    """
    def ImportCategoryToLineEdit(self,table): # Function One
        self.btnEditCategory.setEnabled(True)
        self.btnAddCategory.setEnabled(False)
        self.btnCategoryDelete.setEnabled(False)
        self.linEditCategorySearch.setEnabled(False)
        self.tableCategory.setEnabled(False)
        CategoryName = self.tableCategory.item(table.row(),1).text()
        SectionName = self.tableCategory.item(table.row(),2).text()
        self.lineEditCategoryName.setText(CategoryName)
        self.comboxShowSection.setItemText(0,SectionName)
        self.rowCatregory =  table.row()

    def EditCategory(self): # Function Tow

        """Information Category"""
        # Variable Category
        CategoryID   = self.tableCategory.item(self.rowCatregory,0).text()
        # Variable Name Category Old
        CategoryNameOld = self.tableCategory.item(self.rowCatregory, 1).text()
        # Variable Name Category New
        CategoryNameNew = self.lineEditCategoryName.text()

        """Informatoin Section"""
        # Variable Name Sectio Old
        SectionNameold = self.tableCategory.item(self.rowCatregory, 2).text()
        # Variable Name Section New
        SectionNameNew  = self.comboxShowSection.currentText()
        # Variable Section Id
        # Import Name Section Of Table Section Using Name Section
        SectionID = self.con.select("`SectionID`", "Section", "`SectionName` = '{0}'".format(SectionNameNew), 2)
        SectionID = SectionID[0]


        if CategoryNameNew == CategoryNameOld and SectionNameold != SectionNameNew:
            value = "`SectionID` = '{0}'".format(SectionID)
        elif SectionNameold == SectionNameNew and CategoryNameNew != CategoryNameOld:
            value = "`CategoryName` = '{0}'".format(CategoryNameNew)
        elif CategoryNameNew != CategoryNameOld or SectionNameold != SectionNameNew:
          value   = "`CategoryName` = '{0}',`SectionID` = '{1}'".format(CategoryNameNew, SectionID)
        else:
            QMessageBox.information(self, 'تعديل صنف'.decode('UTF-8'),
                                    'انت لم تقوم بتعديل اي شيء في صنف [ {0} ]'.decode('UTF-8').format(CategoryNameOld))
            return False

        # Ckeck Category Name Not Empty If Category Empty Show Message Error
        if not CategoryNameNew :
            QMessageBox.critical(self, 'تعديل صنف'.decode('UTF-8'),
                                  'اكتوب اسم صنف الجديد'.decode('UTF-8'))

        # If Category Not Empty Check If Name Category If Not Exist Of DataBase
        else:
            # Function CheckData Exist Of Class Connect Function CHeck Of Data Exist Database Or No
            CheckNameCategory = self.con.checkData("Category","`CategoryName`","'{0}' AND `CategoryID` != {1}".format(CategoryNameNew,CategoryID))

        # If CategoryNameNew Not Of Database Works Update CategoryName
        if CheckNameCategory ==False:
                # Function Update If Exist Of Class Connect Function Update Value Of Database
                result = self.con.update("Category",value,"`CategoryID` = {0}".format(CategoryID))
                if result:
                   QMessageBox.information(self,'تعديل صنف'.decode('UTF-8'),'تم تعديل صنف [ {0} ]  بنجاح '.decode('UTF-8').format(CategoryNameOld))
                   self.ShowCategory()
                else:
                   QMessageBox.critical(self, 'تعديل صنف'.decode('UTF-8'),
                                           'حدث خلل اثناء تعديل  صنف [ {0} ] الرجاء \n في وقة اخر  '.decode('UTF-8').format(CategoryNameOld))
                self.Cancel()
        else:
            QMessageBox.critical(self, 'تعديل صنف'.decode('UTF-8'),
                                 'اسم هاذا الصنف موجود بلفعل \n اذا لم يكون ظاهر قد يكون غير مفعل'.decode('UTF-8').format(
                                     CategoryNameNew))

    """
    Function Search Of Section Make Search By Name Section Or ID Section Or ID User Or Name User Or Date Add
    """
    def SearchCategory(self,even):
        Search = self.linEditCategorySearch.text()
        # if Form Search Empty Run Function ShowSection Import All Section Of Database
        if  Search == "" or Search == " " or not Search:
            self.ShowCategory()
        else:
            like = "Category.CategoryID LIKE '%{0}%' OR Category.CategoryName LIKE '%{1}%' OR Category.DateAdd LIKE '%{2}%' OR User.FullName LIKE '%{3}%' OR Section.SectionName LIKE '%{4}%'".format(Search,Search,Search,Search,Search)
            sql = """SELECT Category.*,User.FullName,Section.SectionName FROM Category INNER JOIN User ON Category.UserID = User.UserID INNER JOIN Section ON Category.SectionID = Section.SectionID WHERE ({0}) AND ActiveCategory = 1""".format(like)
            con = self.con.con # Variable Connect Database
            con = con.cursor()
            con.execute(sql)
            SearchResult = con.fetchall()
            lenghtData = len(SearchResult)
            self.tableCategory.setRowCount(int(lenghtData))
            Row = 0 # Number Row Of Table
            # Insert Search Result Of Table Section
            for info in SearchResult:
                if Row > lenghtData:break
                self.tableCategory.setItem(Row,0,QTableWidgetItem(str(info[0])))
                self.tableCategory.setItem(Row,1,QTableWidgetItem(str(info[1]).decode("UTF-8")))
                self.tableCategory.setItem(Row, 2, QTableWidgetItem(str(info[7]).decode("UTF-8")))
                self.tableCategory.setItem(Row,3,QTableWidgetItem(str(info[2])))
                self.tableCategory.setItem(Row,4,QTableWidgetItem(str(info[6]).decode("UTF-8")))
                Row+=1 # Incrimiate Steb By 1

    """
    Function Cancel
    """
    def Cancel(self):
        self.btnEditCategory.setEnabled(False)
        self.btnAddCategory.setEnabled(True)
        self.btnCategoryDelete.setEnabled(True)
        self.tableCategory.setEnabled(True)
        self.linEditCategorySearch.setEnabled(True)
        self.comboxShowSection.setItemText(0, " ")
        self.comboxShowSection.setCurrentIndex(0)
        self.lineEditCategoryName.clear()
