#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time,string,random,hashlib
class funClassItem():
    """
    Function Add Item To Database
    """
    def addItem(self):
        # Information Item
        nameItem         = self.lineEditNameItem.text()
        price            = self.lineEditPrice.text()
        quentity         = self.lineEditQuentity.text()
        completionDate   = self.lineEditCompletionDate.text()
        dateOfProduction = self.lineEditDateOfProduction.text()
        nameStore        = self.comboxStoreItem.currentText()
        nameCatgory      = self.comBoxCategoryItem.currentText()
        UserID           = self.labUserID.text()
        # function the checkFormatDate Check Of Format Data True Or False
        FormatDateProduction = self.checkFormatDate(dateOfProduction)
        FormatDateComletion  = self.checkFormatDate(completionDate)

        # Check The Name Item Is In Database Or Not
        CheckNameItem = self.con.select('ItemName','Item','ItemName = "{0}"'.format(nameItem),1)

        # PathImage Content Path Picture
        # If Select Image == Path Image else Show Message
        try:
            if self.pathImage != '':
                self.pathImage = self.pathImage
        except:
            self.pathImage = ''

        if not nameItem or not quentity or not price or not completionDate or not dateOfProduction:
            QMessageBox.critical(self,'اظافة منتج'.decode("UTF-8"),'يرجا ملئ جميع الحقول فهيه مطلوبه'.decode('UTF-8'))
        elif nameCatgory == 'الاصناف'.decode("UTF-8") :
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يرجا اختيار صنف المنتج'.decode('UTF-8'))
        elif nameStore == 'المخازن'.decode("UTF-8"):
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يرجا اختيار مخزن تخزين المنتج'.decode('UTF-8'))
        elif FormatDateProduction == False:
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يجب ان تكتوب تاريخ الانتاج بطريقه صحيحه  \n مثال : 05-02-2017'.decode('UTF-8'))
        elif FormatDateComletion == False:
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يجب ان تكتوب تاريخ الانتهاء بطريقه صحيحه  \n مثال : 30-12-2017'.decode('UTF-8'))
        elif self.pathImage == '':
            QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"), 'يب ان تقوم بختيار صووره'.decode('UTF-8'))
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
            storeID       = self.con.select("StoreID","Store","StoreName = '{0}'".format(nameStore),2)[0]
            # Import StoreID of Table categoryID
            categoryID    = self.con.select("CategoryID","Category","CategoryName = '{0}'".format(nameCatgory),2)[0]
            # Extenison Image
            extenison = self.pathImage.split(".")[-1]
            # Name Image
            while True:
                NameImage = self.RandomKeyImage() + "." +extenison
                result = self.con.select("Image","Item","Image = '{0}'".format(NameImage),1)
                if result:
                    NameImage = self.RandomKeyImage() + "." +extenison
                else:
                    break
            ColumnName  = '`ItemName`, `Price`, `Quentity`, `Image`, `DateOfProduction`, `CompletionDate`, `DateAdd`, `UserID`, `CategoryID`, `StoreID`'
            ValueColumn = "'{0}','{1}','{2}','{3}','{4}','{5}',now(),'{6}','{7}','{8}'".format(nameItem,price,quentity,NameImage,dateOfProduction,completionDate,UserID,categoryID,storeID)
            result = self.con.insert('Item',ColumnName,ValueColumn)
            # If Insert Item SHow Message Ok Else Message Error
            if result:
                # Upload Image To Ftp Server
                UploadImage = self.connectFTP.UploadFileFtp('Item',self.pathImage,NameImage)
                if UploadImage:
                    QMessageBox.information(self, 'اظافة منتج'.decode("UTF-8"),
                                         'تم اظافة المنتج بنجاح'.decode('UTF-8'))
                    self.Cancel()
            else:
                QMessageBox.critical(self, 'اظافة منتج'.decode("UTF-8"),
                                     'حذثت مشكله اثناء اظافة المنتج الرجاء المحاوله في وقة اخر'.decode('UTF-8'))

    """
    Three Function Show Name Category , Section And Store
    """
    def showItemCategory(self): # Fuunction One Show Name Category
        combCategory = self.comBoxCategoryItem # object Of comBoxCategoryItem
        infoCategory = self.con.select("CategoryName","Category","ActiveCategory = 1",0)
        # Array Context On All Name Category
        Category = ["الاصناف".decode("UTF-8")]
        for nameCategory in infoCategory:
            Category.append(str(nameCategory[0]).decode("UTF-8"))
        # Add Array To Combox
        combCategory.addItems(Category)

    def showItemStore(self): # Fuunction Three Show Name Store
        combStore = self.comboxStoreItem
        infoStore = self.con.select("StoreName","Store","ActiveStore = 1",0)
        # Array Context On All Name Store
        Store = ["المخازن".decode("UTF-8")]
        for nameStore in infoStore:
            Store.append(str(nameStore[0]).decode("UTF-8"))
        # Add Array To Combox
        combStore.addItems(Store)


    """
    Function Check Format Date If Format Ok Return True Else Return False
    """
    def checkFormatDate(self,date):
        try:
            time.strptime(str(date),'%Y-%m-%d')
            return True
        except ValueError:
            return False

    """Function Select Image Of Computer"""
    def SelectImage(self,event):
        filterImage = '*.jpge  *.png *.jpg *.gif ;; *.png;;*.jpge;;*.gif'
        self.pathImage = QFileDialog().getOpenFileNameAndFilter(self,'اختيار صوره'.decode('utf-8'),'',filterImage)[0]
        try:
            if self.pathImage:
                self.labAddImageItem.setPixmap(QPixmap(self.pathImage))
            else:
                self.labAddImageItem.setPixmap(QPixmap(":/images/defaultItem.png"))
        except:
            self.labAddImageItem.setPixmap(QPixmap(":/images/defaultItem.png"))

    # Function Create Random Key For Name Image
    def RandomKeyImage(self):
        millis = hashlib.md5(str(time.time())).hexdigest()[:16]
        stringLetters = list(string.ascii_letters + string.hexdigits)
        random.shuffle(stringLetters)
        stringLetters = ''.join(stringLetters[:9])
        keyImage = list(millis+stringLetters)
        random.shuffle(keyImage)
        keyImage = ''.join(keyImage)
        return keyImage





    """Function Cancel"""
    def Cancel(self):
        self.comboxStoreItem.setCurrentIndex(0)
        self.comBoxCategoryItem.setCurrentIndex(0)
        self.lineEditQuentity.clear()
        self.lineEditDateOfProduction.clear()
        self.lineEditCompletionDate.clear()
        self.lineEditPrice.clear()
        self.lineEditNameItem.clear()
        self.labAddImageItem.setPixmap(QPixmap(":/template/images/defaultItem.png"))

