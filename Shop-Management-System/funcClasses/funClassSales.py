#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys,os,time,string,random,urllib


class funClassSales:

    def openCalc(self,e):
        os.system("calc");

    def showDayAndTime(self):
        datAndTime = time.strftime("%d-%m-%Y %I:%M:%S %p");
        self.labTimeAndDay.setText(datAndTime);

    def CreateBillID(self):
        id = list(string.ascii_uppercase + string.digits)
        BillID = "".join(random.choice(id) for i in range(10,25))
        return BillID

    """ [ Start Item ] """
    def SelectItem(self):
        self.tableSelectItem.show()
        self.ShowItem()

    def ShowItem(self):
        data = self.con.select('ItemID,ItemName,Price','item')
        lenght = len(data)
        self.tableSelectItem.setRowCount(lenght)
        row = 0
        for InfoItem in data:
            self.tableSelectItem.setItem(row,0,QTableWidgetItem(str(InfoItem[0]).decode()))
            self.tableSelectItem.setItem(row,1,QTableWidgetItem(str(InfoItem[1]).decode()))
            self.tableSelectItem.setItem(row,2,QTableWidgetItem(str(InfoItem[2]).decode()))
            row+=1

    def addItemToForm(self):
        rowSelect = self.tableSelectItem.currentRow()
        itemID   = self.tableSelectItem.item(rowSelect,0).text()
        itemName = self.tableSelectItem.item(rowSelect,1).text()
        price    = self.tableSelectItem.item(rowSelect,2).text()
        self.textItemPrice.setText(price)
        self.textItemName.setText(itemName)
        self.textItemID.setText(itemID)
        self.textQu.setText("1")
        self.textTotalItem.setText(price)
        self.btnaddItem.setEnabled(True)
        self.tableSelectItem.close()

    def SearchTableItem(self,e):
        con = self.con.con
        con = con.cursor()
        SearchWord = self.textSearchItem.text()
        sql = """
        SELECT ItemID,ItemName,Price FROM item WHERE ItemID LIKE '%{0}%' OR ItemName LIKE '%{1}%' OR Price LIKE '%{2}%'
        """.format(SearchWord,SearchWord,SearchWord)
        print sql
        con.execute(sql)
        info = con.fetchall()
        lenght = len(info)
        self.tableSelectItem.setRowCount(lenght)
        row = 0
        for InfoItem in info:
            self.tableSelectItem.setItem(row,0,QTableWidgetItem(str(InfoItem[0]).decode()))
            self.tableSelectItem.setItem(row,1,QTableWidgetItem(str(InfoItem[1]).decode()))
            self.tableSelectItem.setItem(row,2,QTableWidgetItem(str(InfoItem[2]).decode()))
            row+=1
        if not SearchWord or SearchWord == " ":
            self.ShowItem()
    def QuItem(self,e):
        Qu = self.textQu.text()
        pr = self.textItemPrice.text()
        if not Qu or Qu == " " or Qu == "  ":
            self.textQu.setText("1")
        elif not pr or pr == " ":
            return False
        else:
            self.textTotalItem.setText(str(int(Qu) * int(pr)))

    def AddItemToTable(self):
        NumberRowTable = self.tableSales.rowCount()
        Price = self.textItemPrice.text()
        itemName = self.textItemName.text()
        itemID = self.textItemID.text()
        Qu    = self.textQu.text()
        TotalItem = self.textTotalItem.text()
        for i in range(0,int(NumberRowTable)+1):
            try:
                if self.tableSales.item(i,0).text() == itemID:
                    QMessageBox.critical(self,'اضافة منتج'.decode(),'انا المنتج الذي طلبته موجود '.decode())
                    self.tableSales.selectRow(i)
                    return False
            except:pass
        QuOld = self.con.select('Quentity', 'item', 'ItemID={}'.format(itemID))[0][0]
        if int(Qu) > int(QuOld):
            QMessageBox.critical(self, 'اضافة منتج'.decode(), 'الكميه المطلوبه غير متوفره'.decode())
            return False
        self.tableSales.setRowCount(NumberRowTable+ 1)
        self.tableSales.setItem(NumberRowTable,0,QTableWidgetItem(str(itemID)))
        self.tableSales.setItem(NumberRowTable,1,QTableWidgetItem(str(itemName).decode()))
        self.tableSales.setItem(NumberRowTable,2,QTableWidgetItem(str(Price)))
        self.tableSales.setItem(NumberRowTable,3,QTableWidgetItem(str(Qu)))
        self.tableSales.setItem(NumberRowTable,4,QTableWidgetItem(str(TotalItem)))
        self.textItemPrice.clear()
        self.textItemName.clear()
        self.textItemID.clear()
        self.textQu.clear()
        self.textTotalItem.clear()
        self.btnaddItem.setEnabled(False)
        self.label_24.setText(str(NumberRowTable+1))
        labTo = 0
        for i in range(0,int(NumberRowTable)+1):
                toatal =  int(self.tableSales.item(i,4).text())
                labTo+=toatal
        self.labTotalAll.setText(str(labTo))

    def removeItemFromTable(self):
        if self.tableSales.selectedItems():
            row = self.tableSales.currentRow()
            self.tableSales.removeRow(row)
            QMessageBox.information(self,'حذف منتج '.decode(),'تم حذف المنتج بنجاح'.decode())
        else:
            QMessageBox.critical(self,'حذف منتج '.decode(),'الرجاء تحديد المنتح الذي تود حذفه'.decode())
        NumberRowTable = self.tableSales.rowCount()
        self.label_24.setText(str(NumberRowTable))
        labTo = 0
        for i in range(0,int(NumberRowTable)):
                toatal =  int(self.tableSales.item(i,4).text())
                labTo+=toatal
        self.labTotalAll.setText(str(labTo))



    def SelectEditItem(self):
        self.btnaddItem.setEnabled(False)
        self.btnDeleteItem.setEnabled(False)
        self.btnSelectItem.setEnabled(False)
        self.btnEditItem.setEnabled(True)
        self.tableSales.setEnabled(False)
        row = self.tableSales.currentRow()
        self.rowEdit = row
        ItemID = self.tableSales.item(row,0).text()
        ItemName = self.tableSales.item(row,1).text()
        price = self.tableSales.item(row,2).text()
        Qu    =self.tableSales.item(row,3).text()
        QuTo = self.tableSales.item(row,4).text()
        self.textItemID.setText(ItemID)
        self.textItemName.setText(ItemName)
        self.textItemPrice.setText(price)
        self.textTotalItem.setText(QuTo)
        self.textQu.setText(Qu)

    def EditItem(self):
        QuOld = self.con.select('Quentity', 'item', 'ItemID={}'.format(self.textItemID.text()))[0][0]
        if int(self.textQu.text()) > int(QuOld):
            QMessageBox.critical(self, 'اضافة منتج'.decode(), 'الكميه المطلوبه غير متوفره'.decode())
            return False
        self.tableSales.setItem(self.rowEdit,0,QTableWidgetItem(str(self.textItemID.text())))
        self.tableSales.setItem(self.rowEdit,1,QTableWidgetItem(str(self.textItemName.text()).decode()))
        self.tableSales.setItem(self.rowEdit,2,QTableWidgetItem(str(self.textItemPrice.text())))
        self.tableSales.setItem(self.rowEdit,3,QTableWidgetItem(str(self.textQu.text())))
        self.tableSales.setItem(self.rowEdit,4,QTableWidgetItem(str(self.textTotalItem.text())))
        self.textItemPrice.clear()
        self.textItemName.clear()
        self.textItemID.clear()
        self.textQu.clear()
        self.textTotalItem.clear()
        self.btnaddItem.setEnabled(False)
        labTo = 0
        NumberRowTable = self.tableSales.rowCount()
        for i in range(0,int(NumberRowTable)):
                toatal =  int(self.tableSales.item(i,4).text())
                labTo+=toatal

        self.labTotalAll.setText(str(labTo))
        self.btnDeleteItem.setEnabled(True)
        self.btnSelectItem.setEnabled(True)
        self.btnEditItem.setEnabled(False)
        self.tableSales.setEnabled(True)
        QMessageBox.information(self,'تعديل المنتج'.decode(),'تم تعديل المنتج بنجاح'.decode())

    def AddSales(self,e):
        self.textQu.setEnabled(True)
        self.tableSales.setEnabled(True)
        self.labSelectCus.setEnabled(True)
        self.btnDeleteItem.setEnabled(True)
        self.btnSelectItem.setEnabled(True)
        self.textSearchCustomer.setEnabled(True)
        self.labSave.setEnabled(True)
        self.textSearchItem.setEnabled(True)
        self.labBillID.setText(self.CreateBillID())
        self.labAddSales.setEnabled(False)

    def SearchCus(self,e):
        con = self.con.con
        con = con.cursor()
        SearchWord = self.textSearchCustomer.text()
        sql = """
        SELECT CustomersID,CustomersName FROM customers WHERE CustomersID LIKE '%{0}%' OR CustomersName LIKE '%{1}%'
        """.format(SearchWord,SearchWord)
        print sql
        con.execute(sql)
        info = con.fetchall()
        lenght = len(info)
        self.tableSelectCust.setRowCount(lenght)
        row = 0
        for InfoItem in info:
            self.tableSelectCust.setItem(row,0,QTableWidgetItem(str(InfoItem[0]).decode()))
            self.tableSelectCust.setItem(row,1,QTableWidgetItem(str(InfoItem[1]).decode()))
            row+=1
        if not SearchWord or SearchWord == " ":
            self.ShowCus()

    def addCustToForm(self):
        rowSelect = self.tableSelectCust.currentRow()
        CusID   = self.tableSelectCust.item(rowSelect,0).text()
        CusName = self.tableSelectCust.item(rowSelect,1).text()
        self.labCusID.setText(CusID)
        self.labNameCus.setText(CusName)
        img = self.con.select('CustomerImage','customers','CustomersID = {0}'.format(CusID),2)[0]
        url = "http://" + self.connectFTP.HOSTFTP + "/Home/" + self.connectFTP.NameFile + "/Customers/" + img
        op = urllib.urlopen(url).read()
        px = QPixmap()
        px.loadFromData(op)
        self.labSelectCus.setPixmap(px)
        self.tableSelectCust.close()

    def SelctCust(self,e):
        self.ShowCus()
        self.tableSelectCust.show()

    def ShowCus(self):
        data = self.con.select('CustomersID,CustomersName','customers')
        lenght = len(data)
        self.tableSelectCust.setRowCount(lenght)
        row = 0
        for InfoItem in data:
            self.tableSelectCust.setItem(row,0,QTableWidgetItem(str(InfoItem[0]).decode()))
            self.tableSelectCust.setItem(row,1,QTableWidgetItem(str(InfoItem[1]).decode()))
            row+=1

    def SaveSales(self,e):
        CountSales = self.tableSales.rowCount()
        if CountSales != 0:
            Row = 1
            for i in range(CountSales):
                itemID = self.tableSales.item(i,0).text()
                Qu     = self.tableSales.item(i,3).text()
                QuOld = self.con.select('Quentity','item','ItemID={}'.format(itemID))[0][0]
                QuNew = int(QuOld) - int(Qu)
                self.con.update('item','Quentity = {}'.format(QuNew),'ItemID={}'.format(itemID))
                Row+=1
            QMessageBox.information(self,'حفظ البيعه'.decode(),'تم الحفظ بنجاح يمكنك طباعة الفاتوره'.decode())
            self.labSave.setEnabled(False)
            self.labPrint.setEnabled(True)
            self.btnEditItem.setEnabled(False)
            self.btnDeleteItem.setEnabled(False)
