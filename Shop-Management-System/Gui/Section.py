# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Section.ui'
#
# Created: Fri Apr 14 10:32:06 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Section(object):
    def setupUi(self, Section):
        Section.setObjectName(_fromUtf8("Section"))
        Section.setWindowModality(QtCore.Qt.ApplicationModal)
        Section.resize(786, 367)
        Section.setLayoutDirection(QtCore.Qt.RightToLeft)
        Section.setAutoFillBackground(False)
        Section.setStyleSheet(_fromUtf8(""))
        Section.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Jordan))
        self.lineEditSectionName = QtGui.QLineEdit(Section)
        self.lineEditSectionName.setGeometry(QtCore.QRect(388, 20, 381, 31))
        self.lineEditSectionName.setObjectName(_fromUtf8("lineEditSectionName"))
        self.btnAddSection = QtGui.QPushButton(Section)
        self.btnAddSection.setGeometry(QtCore.QRect(90, 20, 140, 31))
        self.btnAddSection.setObjectName(_fromUtf8("btnAddSection"))
        self.tableSection = QtGui.QTableWidget(Section)
        self.tableSection.setGeometry(QtCore.QRect(13, 100, 761, 251))
        self.tableSection.setLineWidth(1)
        self.tableSection.setMidLineWidth(0)
        self.tableSection.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableSection.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableSection.setAutoScroll(True)
        self.tableSection.setTabKeyNavigation(True)
        self.tableSection.setProperty("showDropIndicator", True)
        self.tableSection.setDragEnabled(False)
        self.tableSection.setDragDropOverwriteMode(True)
        self.tableSection.setAlternatingRowColors(False)
        self.tableSection.setShowGrid(True)
        self.tableSection.setCornerButtonEnabled(True)
        self.tableSection.setObjectName(_fromUtf8("tableSection"))
        self.tableSection.setColumnCount(4)
        self.tableSection.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableSection.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableSection.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableSection.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableSection.setHorizontalHeaderItem(3, item)
        self.tableSection.horizontalHeader().setVisible(True)
        self.tableSection.horizontalHeader().setCascadingSectionResizes(False)
        self.tableSection.horizontalHeader().setHighlightSections(True)
        self.tableSection.horizontalHeader().setSortIndicatorShown(False)
        self.tableSection.horizontalHeader().setStretchLastSection(False)
        self.tableSection.verticalHeader().setVisible(True)
        self.tableSection.verticalHeader().setCascadingSectionResizes(False)
        self.tableSection.verticalHeader().setHighlightSections(True)
        self.tableSection.verticalHeader().setSortIndicatorShown(False)
        self.tableSection.verticalHeader().setStretchLastSection(False)
        self.btnSectionDelete = QtGui.QPushButton(Section)
        self.btnSectionDelete.setGeometry(QtCore.QRect(240, 60, 140, 31))
        self.btnSectionDelete.setObjectName(_fromUtf8("btnSectionDelete"))
        self.linEditSectionSearch = QtGui.QLineEdit(Section)
        self.linEditSectionSearch.setGeometry(QtCore.QRect(389, 60, 381, 31))
        self.linEditSectionSearch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.linEditSectionSearch.setObjectName(_fromUtf8("linEditSectionSearch"))
        self.labUserID = QtGui.QLabel(Section)
        self.labUserID.setGeometry(QtCore.QRect(20, 0, 61, 21))
        self.labUserID.setObjectName(_fromUtf8("labUserID"))
        self.label = QtGui.QLabel(Section)
        self.label.setGeometry(QtCore.QRect(0, 19, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.labNumberSection = QtGui.QLabel(Section)
        self.labNumberSection.setGeometry(QtCore.QRect(30, 60, 31, 31))
        self.labNumberSection.setAlignment(QtCore.Qt.AlignCenter)
        self.labNumberSection.setObjectName(_fromUtf8("labNumberSection"))
        self.btnEditSection = QtGui.QPushButton(Section)
        self.btnEditSection.setGeometry(QtCore.QRect(240, 20, 140, 31))
        self.btnEditSection.setObjectName(_fromUtf8("btnEditSection"))
        self.btnCancel = QtGui.QPushButton(Section)
        self.btnCancel.setGeometry(QtCore.QRect(90, 60, 140, 31))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))

        self.retranslateUi(Section)
        QtCore.QMetaObject.connectSlotsByName(Section)
        Section.setTabOrder(self.lineEditSectionName, self.linEditSectionSearch)
        Section.setTabOrder(self.linEditSectionSearch, self.btnAddSection)
        Section.setTabOrder(self.btnAddSection, self.tableSection)
        Section.setTabOrder(self.tableSection, self.btnSectionDelete)

    def retranslateUi(self, Section):
        Section.setWindowTitle(_translate("Section", "الاقسام", None))
        self.lineEditSectionName.setPlaceholderText(_translate("Section", "اكتوب اسم القسم ", None))
        self.btnAddSection.setText(_translate("Section", "اظافة", None))
        self.tableSection.setSortingEnabled(False)
        item = self.tableSection.horizontalHeaderItem(0)
        item.setText(_translate("Section", "معرف القسم", None))
        item = self.tableSection.horizontalHeaderItem(1)
        item.setText(_translate("Section", "اسم القسم", None))
        item = self.tableSection.horizontalHeaderItem(2)
        item.setText(_translate("Section", "تاريخ القسم", None))
        item = self.tableSection.horizontalHeaderItem(3)
        item.setText(_translate("Section", "اسم المضيف", None))
        self.btnSectionDelete.setText(_translate("Section", "الغاء القسم", None))
        self.linEditSectionSearch.setPlaceholderText(_translate("Section", "اكتوب ما تود البحث عنه ", None))
        self.labUserID.setText(_translate("Section", "UserID", None))
        self.label.setText(_translate("Section", "عدد الاقسام ", None))
        self.labNumberSection.setText(_translate("Section", "0", None))
        self.btnEditSection.setText(_translate("Section", "تعديل", None))
        self.btnCancel.setText(_translate("Section", "الغاء", None))

