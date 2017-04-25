#_*_ coding:utf8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.Item import *
from funcClasses.funClassItem import *
from connect import *
from connectFtp import *


class item(QWidget,Ui_Item,funClassItem):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.move(300,190)
        self.btnEditItem.setGeometry(300, 190, 150, 41)
        self.btnEditItem.setVisible(False)
        self.labUserID.setVisible(False)
        self.labItemID.setVisible(False)

        # Object From Class Connect Database
        self.con = connect()
        # Object From Class Connect FTP server
        self.connectFTP = connectFtp()


        """[ Run Function ]"""
        # Function Show Name Category Of Combox
        self.showItemCategory()
        # Function Show Name Store Of Combox
        self.showItemStore()


        """[ Start Event ]"""
        # Button Add Item To Database
        self.btnAddItem.clicked.connect(self.addItem)
        # Button Cancel
        self.btnCancel.clicked.connect(self.Cancel)
        self.btnEditItem.clicked.connect(self.EditItem)
        # Select Image
        self.labAddImageItem.mouseDoubleClickEvent = self.SelectImage
        """[ End Event ]"""


    def EditItem(self):
        # Information Item
        ItemID            = self.labItemID.text()
        nameItem          = self.lineEditNameItem.text()
        price             = self.lineEditPrice.text()
        quentity          = self.lineEditQuentity.text()
        completionDate    = self.lineEditCompletionDate.text()
        dateOfProduction  = self.lineEditDateOfProduction.text()
        nameStore         = self.comboxStoreItem.currentText()
        nameCatgory       = self.comBoxCategoryItem.currentText()

        UserID = '1'  # the Variable Content UserID

        # function the checkFormatDate Check Of Format Data True Or False
        FormatDateProduction = self.checkFormatDate(dateOfProduction)
        FormatDateComletion = self.checkFormatDate(completionDate)

        # Check The Name Item Is In Database Or Not
        CheckNameItem = self.con.select('ItemName', 'Item', 'ItemName = "{0}" and ItemID != {1}'.format(nameItem,ItemID), 1)

        # PathImage Content Path Picture
        # If Select Image == Path Image else Show Message
        try:
            if self.pathImage != '':
                self.pathImage = self.pathImage
        except:
            self.pathImage = False

        if not nameItem or not quentity or not price or not completionDate or not dateOfProduction:
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يرجا ملئ جميع الحقول فهيه مطلوبه'.decode('UTF-8'))
        elif nameCatgory == 'الاصناف'.decode("UTF-8"):
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يرجا اختيار صنف المنتج'.decode('UTF-8'))
        elif nameStore == 'المخازن'.decode("UTF-8"):
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يرجا اختيار مخزن تخزين المنتج'.decode('UTF-8'))
        elif FormatDateProduction == False:
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"),
                                 'يجب ان تكتوب تاريخ الانتاج بطريقه صحيحه  \n مثال : 05-02-2017'.decode('UTF-8'))
        elif FormatDateComletion == False:
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"),
                                 'يجب ان تكتوب تاريخ الانتهاء بطريقه صحيحه  \n مثال : 30-12-2017'.decode('UTF-8'))
        elif CheckNameItem == True:
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'المنتج الذي ادخلته موجود مسبقا '.decode('UTF-8'))
        else:
            # Check Of Value quentity int If Not Int SHow Message And Return False
            try:
                int(quentity)
            except:
                QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يجب ان لا تكون الكميه نص'.decode('UTF-8'))
                return False
            # Check Of Value price int If Not Int SHow Message And Return False
            try:
                int(price)
            except:
                QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يجب ان لا يكون السعر نص'.decode('UTF-8'))
                return False

            # Import StoreID of Table Store
            storeID = self.con.select("StoreID", "Store", "StoreName = '{0}'".format(nameStore), 2)[0]
            # Import StoreID of Table categoryID
            categoryID = self.con.select("CategoryID", "Category", "CategoryName = '{0}'".format(nameCatgory), 2)[0]


            # Extenison Image
            if self.pathImage != False:
                extenison = self.pathImage.split(".")[-1]
                NameImage = self.RandomKeyImage() + "." + extenison
            else:
                NameImage = self.con.select("Image", "Item", "ItemID = {0}".format(ItemID), 2)[0]
            NameImageOld = self.con.select("Image", "Item", "ItemID = {0}".format(ItemID), 2)[0]

            ColumnValue = """
                `ItemName`          ='{0}',
                `Price`             ='{1}',
                `Quentity`          ='{2}',
                `Image`             ='{3}',
                `DateOfProduction`  ='{4}',
                `CompletionDate`    ='{5}',
                `UserID`            ='{6}',
                `CategoryID`        ='{7}',
                `StoreID`           ='{8}'
            """.format(nameItem,price,quentity,NameImage,dateOfProduction,completionDate,UserID,categoryID,storeID)


            result = self.con.update("Item",ColumnValue,"ItemID = {0}".format(ItemID))

            if result:
                if self.pathImage == False:
                    QMessageBox.information(self, 'تعديل منتج'.decode("UTF-8"),
                                            'تم تعديل المنتج بنجاح'.decode('UTF-8'))
                else:
                    # Upload Image To Ftp Server
                    UploadImage = self.connectFTP.UploadFileFtp('Item', self.pathImage, NameImage)
                    self.connectFTP.ftp.cwd('Item')
                    self.connectFTP.ftp.delete(NameImageOld)
                    self.connectFTP.ftp.cwd('../')
                    if UploadImage:
                        QMessageBox.information(self, 'تعديل منتج'.decode("UTF-8"),
                                                'تم تعديل المنتج بنجاح'.decode('UTF-8'))
                    else:
                        QMessageBox.critical(self, 'تعديل منتج'.decode("UTF-8"),
                                 'حذثت مشكله اثناء تحميل الصوره الرجاء محاوله تغير الصوره  في وقة اخر'.decode('UTF-8'))
                self.Cancel()
                self.close()

            else:
                QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"),
                                     'حذثت مشكله اثناء تعديل المنتج '.decode('UTF-8'))











