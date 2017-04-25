# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Store.ui'
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

class Ui_Stor(object):
    def setupUi(self, Stor):
        Stor.setObjectName(_fromUtf8("Stor"))
        Stor.setWindowModality(QtCore.Qt.ApplicationModal)
        Stor.resize(486, 291)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Arabic Kufi"))
        Stor.setFont(font)
        Stor.setLayoutDirection(QtCore.Qt.RightToLeft)
        Stor.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Jordan))
        self.lineEditStoreName = QtGui.QLineEdit(Stor)
        self.lineEditStoreName.setGeometry(QtCore.QRect(280, 10, 191, 31))
        self.lineEditStoreName.setObjectName(_fromUtf8("lineEditStoreName"))
        self.btnStoreAdd = QtGui.QPushButton(Stor)
        self.btnStoreAdd.setGeometry(QtCore.QRect(170, 10, 101, 31))
        self.btnStoreAdd.setObjectName(_fromUtf8("btnStoreAdd"))
        self.btnStoreDelete = QtGui.QPushButton(Stor)
        self.btnStoreDelete.setGeometry(QtCore.QRect(60, 10, 89, 31))
        self.btnStoreDelete.setObjectName(_fromUtf8("btnStoreDelete"))
        self.btnStoreEdit = QtGui.QPushButton(Stor)
        self.btnStoreEdit.setGeometry(QtCore.QRect(170, 50, 101, 31))
        self.btnStoreEdit.setObjectName(_fromUtf8("btnStoreEdit"))
        self.lineEditStoreSearch = QtGui.QLineEdit(Stor)
        self.lineEditStoreSearch.setGeometry(QtCore.QRect(280, 50, 191, 31))
        self.lineEditStoreSearch.setObjectName(_fromUtf8("lineEditStoreSearch"))
        self.tableStore = QtGui.QTableWidget(Stor)
        self.tableStore.setGeometry(QtCore.QRect(10, 90, 461, 192))
        self.tableStore.setObjectName(_fromUtf8("tableStore"))
        self.tableStore.setColumnCount(2)
        self.tableStore.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableStore.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableStore.setHorizontalHeaderItem(1, item)
        self.labNumberStore = QtGui.QLabel(Stor)
        self.labNumberStore.setGeometry(QtCore.QRect(10, 30, 41, 31))
        self.labNumberStore.setAlignment(QtCore.Qt.AlignCenter)
        self.labNumberStore.setObjectName(_fromUtf8("labNumberStore"))
        self.btnCancel = QtGui.QPushButton(Stor)
        self.btnCancel.setGeometry(QtCore.QRect(60, 50, 89, 31))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))

        self.retranslateUi(Stor)
        QtCore.QMetaObject.connectSlotsByName(Stor)

    def retranslateUi(self, Stor):
        Stor.setWindowTitle(_translate("Stor", "المخازن", None))
        self.lineEditStoreName.setPlaceholderText(_translate("Stor", "اسم المخزن", None))
        self.btnStoreAdd.setText(_translate("Stor", "اظافة", None))
        self.btnStoreDelete.setText(_translate("Stor", "الغاء المخزن", None))
        self.btnStoreEdit.setText(_translate("Stor", "نعديل", None))
        self.lineEditStoreSearch.setPlaceholderText(_translate("Stor", "اكتب ما تود البحث عنه", None))
        item = self.tableStore.horizontalHeaderItem(0)
        item.setText(_translate("Stor", "معرف المخزن", None))
        item = self.tableStore.horizontalHeaderItem(1)
        item.setText(_translate("Stor", "اسم المخزن", None))
        self.labNumberStore.setText(_translate("Stor", "0", None))
        self.btnCancel.setText(_translate("Stor", "الغاء", None))

