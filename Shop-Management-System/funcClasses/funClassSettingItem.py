# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import urllib

class funClassSettingItem():
    """
    Function Show Item Of The Table
    """
    def ShowItem(self):

        self.labNumberItem.move(250, 10)
        ItemType = str(self.comboxShowItem.currentText())

        ActiveItem = 1
        if ItemType == "المنتجات الغير فعاله":
            ActiveItem = 0
            self.btnActive.setVisible(True)
        else:
            ActiveItem = 1
            self.btnActive.move(370, 10)
            self.btnNotActive.setVisible(True)
            self.btnActive.setVisible(False)


        # Vairable Connect Database Content On Function ConnectDB
        con = self.con.con;
        con = con.cursor()
        sql = """
        SELECT
            Item.* , User.FullName,Store.StoreName,Category.CategoryName
        FROM
            Item
        INNER JOIN
            User
        ON
            Item.UserID = User.UserID
        INNER JOIN
            Store
        ON
          Item.StoreID = Store.StoreID
        INNER JOIN
            Category
          ON
          Item.CategoryID = Category.CategoryID
        WHERE Item.ActiveItem = %d ORDER BY ItemID DESC
        """ % (ActiveItem)

        con.execute(sql)
        # Fetch All Date Of Database
        infoItem = con.fetchall()
        lengthDate = len(infoItem)
        # Determination Number Row Of Table
        self.labNumberItem.setText(str(lengthDate))
        self.tableSettingItem.setRowCount(lengthDate)
        Row = 0
        for info in infoItem:
            # Check Number Row IF greater than Of length Data Break Of Statment For
            if Row >= lengthDate: break
            # Insert Date To Table
            self.tableSettingItem.setItem(Row, 0, QTableWidgetItem(str(info[0]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 1, QTableWidgetItem(str(info[1]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 2, QTableWidgetItem(str(info[14]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 3, QTableWidgetItem(str(info[13]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 4, QTableWidgetItem(str(info[7]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 5, QTableWidgetItem(str(info[5]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 6, QTableWidgetItem(str(info[6]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 7, QTableWidgetItem(str(info[2]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 8, QTableWidgetItem(str(info[3]).decode("UTF-8")))
            self.tableSettingItem.setItem(Row, 9, QTableWidgetItem(str(info[12]).decode("UTF-8")))
            Row += 1  # Incriminate One To Variable Row

    """
    Function Active Tow Walk
    1 - Not Activate Item
    2 - Activet Item
    """
    def Active(self):
        if self.tableSettingItem.selectedItems():
            # Content Number Row If Select
            Row = self.tableSettingItem.currentRow()
            # Content ItemID iF Select
            itemID = self.tableSettingItem.item(Row, 0).text()
            # Content Valie Of Combox
            ShowType = self.comboxShowItem.currentText()

            if ShowType == "المنتجات الغير فعاله".decode('utf-8'):
                valueActive = 1
                MsgError = 'حدث خطء اثناء  تفعيل المنتج الرجاء المحاوله في ما بعد'.decode('utf-8')
                MsgOk = 'تم  تفعيل المنتج بنجاح'.decode('utf-8')
            else:
                valueActive = 0
                MsgError = 'حدث خطء اثناء الغاء تفعيل المنتج الرجاء المحاوله في ما بعد'.decode('utf-8')
                MsgOk = 'تم الغاء تفعيل المنتج بنجاح'.decode('utf-8')
            result = self.con.update('Item', 'ActiveItem = {0}'.format(valueActive), 'ItemID = {0}'.format(itemID))
            if result:
                QMessageBox.information(self, ' التفعيل'.decode("utf-8"), MsgOk)
                self.ShowItem()
            else:
                QMessageBox.information(self, ' التفعيل'.decode("utf-8"), MsgError)
        else:
            QMessageBox.information(self, 'الغاء التفعيل'.decode("utf-8"),
                                    'يجب تحديد المنتج الذي تود الغاء تفيله'.decode('utf-8'))


    """
    Function Edit Item
    """
    def EditItem(self):
        import classes.class_item as item
        EditItem = item.item()
        EditItem.show()
        Row = self.tableSettingItem.currentRow()
        ItemID = self.tableSettingItem.item(Row, 0).text()
        ItemName = self.tableSettingItem.item(Row,1).text()
        ItemCateory = self.tableSettingItem.item(Row, 2).text()
        CateoryID  = self.con.select('CategoryID','Category','CategoryName = "{0}"'.format(ItemCateory),2)[0]
        ItemStore = self.tableSettingItem.item(Row, 3).text()
        Price = self.tableSettingItem.item(Row, 7).text()
        DateOfProdutcion = self.tableSettingItem.item(Row, 5).text()
        completionDate = self.tableSettingItem.item(Row, 6).text()
        Quentity = self.tableSettingItem.item(Row, 8).text()
        NameImage = self.con.select("Image","Item","ItemID = '{0}'".format(ItemID),2)[0]
        print NameImage
        url = "http://" + self.connectFTP.HOSTFTP + "/Home/" + self.connectFTP.NameFile + "/Item/" + NameImage
        print url
        # Convert Image To Binary
        data = urllib.urlopen(url).read()
        pixmap = QPixmap()
        # Show Image Bainary Of PyQt
        pixmap.loadFromData(data)
        EditItem.labAddImageItem.setPixmap(pixmap)
        EditItem.lineEditNameItem.setText(ItemName)
        EditItem.lineEditPrice.setText(Price)
        EditItem.lineEditQuentity.setText(Quentity)
        EditItem.lineEditDateOfProduction.setText(DateOfProdutcion)
        EditItem.lineEditCompletionDate.setText(completionDate)
        EditItem.comboxStoreItem.setItemText(0,ItemStore)
        EditItem.comBoxCategoryItem.setItemText(0,ItemCateory)
        EditItem.labItemID.setText(ItemID)
        EditItem.btnAddItem.setVisible(False)
        EditItem.btnCancel.setVisible(False)
        EditItem.btnEditItem.setVisible(True)


