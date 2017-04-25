# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SettingItem.ui'
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

class Ui_SettingItem(object):
    def setupUi(self, SettingItem):
        SettingItem.setObjectName(_fromUtf8("SettingItem"))
        SettingItem.setWindowModality(QtCore.Qt.ApplicationModal)
        SettingItem.resize(1240, 555)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Arabic Kufi"))
        SettingItem.setFont(font)
        SettingItem.setLayoutDirection(QtCore.Qt.RightToLeft)
        SettingItem.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Jordan))
        SettingItem.setInputMethodHints(QtCore.Qt.ImhExclusiveInputMask)
        self.lineEditSearchItem = QtGui.QLineEdit(SettingItem)
        self.lineEditSearchItem.setGeometry(QtCore.QRect(760, 10, 471, 29))
        self.lineEditSearchItem.setObjectName(_fromUtf8("lineEditSearchItem"))
        self.tableSettingItem = QtGui.QTableWidget(SettingItem)
        self.tableSettingItem.setGeometry(QtCore.QRect(4, 48, 1231, 501))
        self.tableSettingItem.setObjectName(_fromUtf8("tableSettingItem"))
        self.tableSettingItem.setColumnCount(10)
        self.tableSettingItem.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableSettingItem.setHorizontalHeaderItem(9, item)
        self.btnNotActive = QtGui.QPushButton(SettingItem)
        self.btnNotActive.setGeometry(QtCore.QRect(370, 10, 121, 31))
        self.btnNotActive.setObjectName(_fromUtf8("btnNotActive"))
        self.comboxShowItem = QtGui.QComboBox(SettingItem)
        self.comboxShowItem.setGeometry(QtCore.QRect(510, 10, 221, 31))
        self.comboxShowItem.setObjectName(_fromUtf8("comboxShowItem"))
        self.comboxShowItem.addItem(_fromUtf8(""))
        self.comboxShowItem.addItem(_fromUtf8(""))
        self.btnActive = QtGui.QPushButton(SettingItem)
        self.btnActive.setEnabled(True)
        self.btnActive.setGeometry(QtCore.QRect(240, 10, 121, 31))
        self.btnActive.setObjectName(_fromUtf8("btnActive"))
        self.labNumberItem = QtGui.QLabel(SettingItem)
        self.labNumberItem.setGeometry(QtCore.QRect(10, 10, 62, 31))
        self.labNumberItem.setStyleSheet(_fromUtf8("color:#1abc9c;\n"
"font-weight:bold;"))
        self.labNumberItem.setAlignment(QtCore.Qt.AlignCenter)
        self.labNumberItem.setObjectName(_fromUtf8("labNumberItem"))

        self.retranslateUi(SettingItem)
        QtCore.QMetaObject.connectSlotsByName(SettingItem)

    def retranslateUi(self, SettingItem):
        SettingItem.setWindowTitle(_translate("SettingItem", "اعدادات المنتجات", None))
        self.lineEditSearchItem.setPlaceholderText(_translate("SettingItem", "اكتوب ما تود البحث عنه", None))
        item = self.tableSettingItem.horizontalHeaderItem(0)
        item.setText(_translate("SettingItem", "معرف المنتج", None))
        item = self.tableSettingItem.horizontalHeaderItem(1)
        item.setText(_translate("SettingItem", "اسم المنتج", None))
        item = self.tableSettingItem.horizontalHeaderItem(2)
        item.setText(_translate("SettingItem", "صنف المنتج", None))
        item = self.tableSettingItem.horizontalHeaderItem(3)
        item.setText(_translate("SettingItem", "مكان التخزين", None))
        item = self.tableSettingItem.horizontalHeaderItem(4)
        item.setText(_translate("SettingItem", "تاريخ الاظافة", None))
        item = self.tableSettingItem.horizontalHeaderItem(5)
        item.setText(_translate("SettingItem", "تاريج الانتاج ", None))
        item = self.tableSettingItem.horizontalHeaderItem(6)
        item.setText(_translate("SettingItem", "تاريخ الانتهاء", None))
        item = self.tableSettingItem.horizontalHeaderItem(7)
        item.setText(_translate("SettingItem", "الثمن", None))
        item = self.tableSettingItem.horizontalHeaderItem(8)
        item.setText(_translate("SettingItem", "الكميه", None))
        item = self.tableSettingItem.horizontalHeaderItem(9)
        item.setText(_translate("SettingItem", " المضيف", None))
        self.btnNotActive.setText(_translate("SettingItem", "الغاء المنتج", None))
        self.comboxShowItem.setItemText(0, _translate("SettingItem", "المنتجات الفعاله", None))
        self.comboxShowItem.setItemText(1, _translate("SettingItem", "المنتجات الغير فعاله", None))
        self.btnActive.setText(_translate("SettingItem", "تفعيل المنتج", None))
        self.labNumberItem.setText(_translate("SettingItem", "0", None))

import pathIcon_rc
