#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.mainWindow import *
from funcClasses.funClassMainWindow import *
from classes.class_Section import *
from classes.class_category import *
from classes.class_Store import *
from classes.class_item import *
from classes.class_SettingItem import *
from classes.class_customer import *
from classes.class_employes import *
from classes.class_addUsers import *
from classes.class_viewUsers import *
from classes.class_sales import *
from classes.class_chat import *
from classes.class_Settings import *
import os


class mainWindow(QMainWindow,Ui_MainWindow,funClassMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.resize(900,550)
        screen = QDesktopWidget()
        self.setGeometry(0, 30, screen.width() - 10, screen.height() -10)
        self.labUserID.setVisible(False)
        self.sales = sales()
        # -****-[ Start Event Function]-****- #
        self.logOut.triggered.connect(self.closeAll)
        self.addItem.triggered.connect(self.ShowFormItem)
        self.managmentSection.triggered.connect(self.ShowFormSection)
        self.manegmentCategory.triggered.connect(self.ShowFormCategory)
        self.SettingStor.triggered.connect(self.ShowFormStore)
        self.manegmentItem.triggered.connect(self.ShowFormSettingItem)
        self.SettingCustomers.triggered.connect(self.ShowFormSettingCustomers)
        self.SettingEmployes.triggered.connect(self.ShowSettingEmployes)
        self.menuAddUser.triggered.connect(self.ShowAddUsers)
        self.menuViewUser.triggered.connect(self.ShowViewUser)
        self.mainSales.triggered.connect(self.ShowSales)
        self.menuChat.triggered.connect(self.ShowChat)
        self.menuSettingAll.triggered.connect(self.ShowSettingsAll)
        # -****-[ End Event Function]-****- #

    def closeEvent(self,e):
        MsgLogOut = QMessageBox.question(self,'تسجيل الخروج'.decode('UTF-8'),'هل انت متئكد من تسجيل الخروج'.decode('UTF-8'),
                                         QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if MsgLogOut == QtGui.QMessageBox.Yes:
            e.accept()
            sys.exit()
        else:
            e.ignore()
    # Function Show Item
    def ShowFormItem(self):
        self.item = item()
        self.item.labUserID.setText(self.labUserID.text())
        self.item.show()

    # Function Show  Form Setting Item
    def ShowFormSettingItem(self):
        self.settingItem = settingItem()
        self.settingItem.ShowItem()
        self.settingItem.show()

    # Function Show Form Store
    def ShowFormStore(self):
        self.Store = store()
        self.Store.ShowStore()
        self.Store.show()

    # Function Show Form Category
    def ShowFormCategory(self):
        self.Category = Category()
        self.Category.ShowCategory()
        self.Category.labUserID.setText(self.labUserID.text())  # Import IDUser Of MainWindow To Category Window
        self.Category.show()

    # Function Show Form Section
    def ShowFormSection(self):
        self.Section = Section()
        self.Section.ShowSection()
        self.Section.labUserID.setText(self.labUserID.text())
        self.Section.show()

    # Function Show Form Setting Customrs
    def ShowFormSettingCustomers(self):
        self.Customers = customers()
        self.Customers.labUserID.setText(self.labUserID.text())
        self.Customers.show()

    # Function Show Setting Employes
    def ShowSettingEmployes(self):
        self.SettingEmployes = employes()
        self.SettingEmployes.showEmployes()
        self.SettingEmployes.labUserID.setText(self.labUserID.text())
        self.SettingEmployes.ShowSection()
        self.SettingEmployes.show()

    def ShowAddUsers(self):
        self.addUsers = addUser()
        self.addUsers.show()

    def ShowViewUser(self):
        self.viewUser = viewUsers()
        self.viewUser.ShowUsers()
        self.viewUser.show()

    def ShowSales(self):
        self.sales.show()
        self.sales.ShowItem()
        self.sales.ShowCus()


    def ShowChat(self):
        self.chat = chat()
        self.chat.show()

    def ShowSettingsAll(self):
        self.settings = Settings()
        self.settings.show()
