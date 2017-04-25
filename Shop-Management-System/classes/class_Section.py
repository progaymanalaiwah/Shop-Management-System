#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.Section import *
from funcClasses.funClassSection import *
from connect import *


"""
Class Section Content Setting Window And Run Function On Window Section Of Event
"""
class Section (QWidget,Ui_Section,funClassSection):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableSection.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSection.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSection.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.move(200,200)
        self.labUserID.setVisible(False)
        self.btnEditSection.setEnabled(False)
        self.con = connect() #Object Of Class Connect

        """[ Start Event ]"""
        # Add Section To Database
        self.btnAddSection.clicked.connect(self.addSection)

        # Delete Sction Of Database
        self.btnSectionDelete.clicked.connect(self.DeletSection)

        # button Cancel
        self.btnCancel.clicked.connect(self.Cancel)

        # Run Function Show Section
        self.ShowSection();

        # Edit Section
        self.tableSection.doubleClicked.connect(self.ImportSectionToLineEdit)
        self.btnEditSection.clicked.connect(self.EditSection)

        # Search Section
        self.linEditSectionSearch.keyReleaseEvent = self.SearchSection
        """[ End Event ]"""














