#_*_ coding:utf8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.Category import *
from funcClasses.funClassCategory import *
from connect import *

class Category(QWidget,Ui_Category,funClassCategory):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableCategory.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCategory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCategory.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.move(200,200)
        self.labUserID.setVisible(False)
        self.btnEditCategory.setEnabled(False)
        self.con = connect()
        # Function View All Section Of Combox
        self.viewSection()
        self.ShowCategory()

        """[ Start Event ]"""
        # Btn Add Category To Database
        self.btnAddCategory.clicked.connect(self.addCategory)
        # Btn Delete Category Of Database
        self.btnCategoryDelete.clicked.connect(self.DeletCategory)
        # Btn Edit Category
        self.btnEditCategory.clicked.connect(self.EditCategory)
        # Btn Cancel
        self.btnCancel.clicked.connect(self.Cancel)
        # Table Category
        self.tableCategory.doubleClicked.connect(self.ImportCategoryToLineEdit)
        # Line Edit Search Of Database
        self.linEditCategorySearch.keyReleaseEvent = self.SearchCategory

        """[ End Event]"""
