#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.Store import *
from funcClasses.funClassStore import *
from connect import *

class store (QWidget,Ui_Stor,funClassStore):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableStore.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableStore.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableStore.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.move(300,200)
        self.btnStoreEdit.setEnabled(False)

        self.con = connect()
        self.ShowStore()
        """[ Start Event ]"""
        self.btnStoreAdd.clicked.connect(self.addStore)
        self.btnStoreDelete.clicked.connect(self.notActivateStore)
        self.lineEditStoreSearch.keyReleaseEvent = self.SearchStore
        self.btnStoreEdit.clicked.connect(self.EditStore)
        self.tableStore.doubleClicked.connect(self.ImportStoreToLineEdit)
        self.btnCancel.clicked.connect(self.Cancel)
        """[ End Event  ]"""

