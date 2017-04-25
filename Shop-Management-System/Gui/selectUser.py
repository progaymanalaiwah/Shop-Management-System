# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\selectUser.ui'
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

class Ui_SelectUser(object):
    def setupUi(self, SelectUser):
        SelectUser.setObjectName(_fromUtf8("SelectUser"))
        SelectUser.setWindowModality(QtCore.Qt.WindowModal)
        SelectUser.resize(543, 359)
        SelectUser.setLayoutDirection(QtCore.Qt.RightToLeft)
        SelectUser.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.SaudiArabia))
        self.textUserSearcch = QtGui.QLineEdit(SelectUser)
        self.textUserSearcch.setGeometry(QtCore.QRect(5, 10, 531, 31))
        self.textUserSearcch.setAlignment(QtCore.Qt.AlignCenter)
        self.textUserSearcch.setObjectName(_fromUtf8("textUserSearcch"))
        self.tableSelectUser = QtGui.QTableWidget(SelectUser)
        self.tableSelectUser.setGeometry(QtCore.QRect(5, 50, 531, 301))
        self.tableSelectUser.setObjectName(_fromUtf8("tableSelectUser"))
        self.tableSelectUser.setColumnCount(4)
        self.tableSelectUser.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableSelectUser.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableSelectUser.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableSelectUser.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableSelectUser.setHorizontalHeaderItem(3, item)

        self.retranslateUi(SelectUser)
        QtCore.QMetaObject.connectSlotsByName(SelectUser)

    def retranslateUi(self, SelectUser):
        SelectUser.setWindowTitle(_translate("SelectUser", "اختيار مستخدم ", None))
        self.textUserSearcch.setPlaceholderText(_translate("SelectUser", "البحث ....", None))
        item = self.tableSelectUser.horizontalHeaderItem(0)
        item.setText(_translate("SelectUser", "معرف المستخدم ", None))
        item = self.tableSelectUser.horizontalHeaderItem(1)
        item.setText(_translate("SelectUser", "الاسم الكامل ", None))
        item = self.tableSelectUser.horizontalHeaderItem(2)
        item.setText(_translate("SelectUser", "الرقم الوطني ", None))
        item = self.tableSelectUser.horizontalHeaderItem(3)
        item.setText(_translate("SelectUser", "البريد الالكتروني ", None))

