# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Category.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Category(object):
    def setupUi(self, Category):
        Category.setObjectName(_fromUtf8("Category"))
        Category.setWindowModality(QtCore.Qt.ApplicationModal)
        Category.resize(786, 405)
        Category.setLayoutDirection(QtCore.Qt.RightToLeft)
        Category.setAutoFillBackground(False)
        Category.setStyleSheet(_fromUtf8(""))
        Category.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Jordan))
        self.lineEditCategoryName = QtGui.QLineEdit(Category)
        self.lineEditCategoryName.setGeometry(QtCore.QRect(390, 20, 381, 31))
        self.lineEditCategoryName.setObjectName(_fromUtf8("lineEditCategoryName"))
        self.btnAddCategory = QtGui.QPushButton(Category)
        self.btnAddCategory.setGeometry(QtCore.QRect(210, 20, 140, 31))
        self.btnAddCategory.setObjectName(_fromUtf8("btnAddCategory"))
        self.tableCategory = QtGui.QTableWidget(Category)
        self.tableCategory.setGeometry(QtCore.QRect(10, 140, 761, 251))
        self.tableCategory.setLineWidth(1)
        self.tableCategory.setMidLineWidth(0)
        self.tableCategory.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableCategory.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableCategory.setAutoScroll(True)
        self.tableCategory.setTabKeyNavigation(True)
        self.tableCategory.setProperty("showDropIndicator", True)
        self.tableCategory.setDragEnabled(False)
        self.tableCategory.setDragDropOverwriteMode(True)
        self.tableCategory.setAlternatingRowColors(False)
        self.tableCategory.setShowGrid(True)
        self.tableCategory.setCornerButtonEnabled(True)
        self.tableCategory.setObjectName(_fromUtf8("tableCategory"))
        self.tableCategory.setColumnCount(5)
        self.tableCategory.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableCategory.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableCategory.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableCategory.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableCategory.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableCategory.setHorizontalHeaderItem(4, item)
        self.tableCategory.horizontalHeader().setVisible(True)
        self.tableCategory.horizontalHeader().setCascadingSectionResizes(False)
        self.tableCategory.horizontalHeader().setHighlightSections(True)
        self.tableCategory.horizontalHeader().setSortIndicatorShown(False)
        self.tableCategory.horizontalHeader().setStretchLastSection(False)
        self.tableCategory.verticalHeader().setVisible(True)
        self.tableCategory.verticalHeader().setCascadingSectionResizes(False)
        self.tableCategory.verticalHeader().setHighlightSections(True)
        self.tableCategory.verticalHeader().setSortIndicatorShown(False)
        self.tableCategory.verticalHeader().setStretchLastSection(False)
        self.btnCategoryDelete = QtGui.QPushButton(Category)
        self.btnCategoryDelete.setGeometry(QtCore.QRect(210, 100, 140, 31))
        self.btnCategoryDelete.setObjectName(_fromUtf8("btnCategoryDelete"))
        self.linEditCategorySearch = QtGui.QLineEdit(Category)
        self.linEditCategorySearch.setGeometry(QtCore.QRect(389, 100, 381, 31))
        self.linEditCategorySearch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.linEditCategorySearch.setObjectName(_fromUtf8("linEditCategorySearch"))
        self.labUserID = QtGui.QLabel(Category)
        self.labUserID.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.labUserID.setObjectName(_fromUtf8("labUserID"))
        self.label = QtGui.QLabel(Category)
        self.label.setGeometry(QtCore.QRect(50, 20, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.labNumberSection = QtGui.QLabel(Category)
        self.labNumberSection.setGeometry(QtCore.QRect(80, 60, 31, 31))
        self.labNumberSection.setAlignment(QtCore.Qt.AlignCenter)
        self.labNumberSection.setObjectName(_fromUtf8("labNumberSection"))
        self.btnEditCategory = QtGui.QPushButton(Category)
        self.btnEditCategory.setGeometry(QtCore.QRect(210, 60, 140, 31))
        self.btnEditCategory.setObjectName(_fromUtf8("btnEditCategory"))
        self.btnCancel = QtGui.QPushButton(Category)
        self.btnCancel.setGeometry(QtCore.QRect(30, 100, 140, 31))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.comboxShowSection = QtGui.QComboBox(Category)
        self.comboxShowSection.setGeometry(QtCore.QRect(390, 60, 381, 31))
        self.comboxShowSection.setObjectName(_fromUtf8("comboxShowSection"))

        self.retranslateUi(Category)
        QtCore.QMetaObject.connectSlotsByName(Category)
        Category.setTabOrder(self.lineEditCategoryName, self.linEditCategorySearch)
        Category.setTabOrder(self.linEditCategorySearch, self.btnAddCategory)
        Category.setTabOrder(self.btnAddCategory, self.tableCategory)
        Category.setTabOrder(self.tableCategory, self.btnCategoryDelete)

    def retranslateUi(self, Category):
        Category.setWindowTitle(_translate("Category", "الاصناف", None))
        self.lineEditCategoryName.setPlaceholderText(_translate("Category", "اكتوب اسم الصنف", None))
        self.btnAddCategory.setText(_translate("Category", "اظافة", None))
        self.tableCategory.setSortingEnabled(False)
        item = self.tableCategory.horizontalHeaderItem(0)
        item.setText(_translate("Category", "معرف الصنف", None))
        item = self.tableCategory.horizontalHeaderItem(1)
        item.setText(_translate("Category", "اسم الصنف", None))
        item = self.tableCategory.horizontalHeaderItem(2)
        item.setText(_translate("Category", "اسم القسم", None))
        item = self.tableCategory.horizontalHeaderItem(3)
        item.setText(_translate("Category", "تاريخ الاظافة", None))
        item = self.tableCategory.horizontalHeaderItem(4)
        item.setText(_translate("Category", "اسم المضيف", None))
        self.btnCategoryDelete.setText(_translate("Category", "الغاء الصنف", None))
        self.linEditCategorySearch.setPlaceholderText(_translate("Category", "اكتوب ما تود البحث عنه ", None))
        self.labUserID.setText(_translate("Category", "UserID", None))
        self.label.setText(_translate("Category", "عدد الاصناف", None))
        self.labNumberSection.setText(_translate("Category", "0", None))
        self.btnEditCategory.setText(_translate("Category", "تعديل", None))
        self.btnCancel.setText(_translate("Category", "الغاء", None))

