# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\viewUsers.ui'
#
# Created: Fri Apr 14 16:55:21 2017
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

class Ui_viewUsers(object):
    def setupUi(self, viewUsers):
        viewUsers.setObjectName(_fromUtf8("viewUsers"))
        viewUsers.setWindowModality(QtCore.Qt.ApplicationModal)
        viewUsers.resize(970, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/viewUsers.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        viewUsers.setWindowIcon(icon)
        viewUsers.setLayoutDirection(QtCore.Qt.RightToLeft)
        viewUsers.setStyleSheet(_fromUtf8(""))
        viewUsers.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.SaudiArabia))
        self.tableViewUsers = QtGui.QTableWidget(viewUsers)
        self.tableViewUsers.setGeometry(QtCore.QRect(10, 20, 661, 391))
        self.tableViewUsers.setObjectName(_fromUtf8("tableViewUsers"))
        self.tableViewUsers.setColumnCount(6)
        self.tableViewUsers.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableViewUsers.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableViewUsers.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableViewUsers.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableViewUsers.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableViewUsers.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableViewUsers.setHorizontalHeaderItem(5, item)
        self.groupBox = QtGui.QGroupBox(viewUsers)
        self.groupBox.setGeometry(QtCore.QRect(680, 20, 281, 391))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.NumberUser = QtGui.QLabel(self.groupBox)
        self.NumberUser.setGeometry(QtCore.QRect(58, 140, 91, 31))
        self.NumberUser.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberUser.setObjectName(_fromUtf8("NumberUser"))
        self.btnActiveUser = QtGui.QPushButton(self.groupBox)
        self.btnActiveUser.setEnabled(False)
        self.btnActiveUser.setGeometry(QtCore.QRect(150, 90, 121, 41))
        self.btnActiveUser.setObjectName(_fromUtf8("btnActiveUser"))
        self.textSearch = QtGui.QLineEdit(self.groupBox)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.textSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.textSearch.setObjectName(_fromUtf8("textSearch"))
        self.labShowImagesUser = QtGui.QLabel(self.groupBox)
        self.labShowImagesUser.setGeometry(QtCore.QRect(10, 187, 261, 191))
        self.labShowImagesUser.setText(_fromUtf8(""))
        self.labShowImagesUser.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/users.png")))
        self.labShowImagesUser.setScaledContents(True)
        self.labShowImagesUser.setObjectName(_fromUtf8("labShowImagesUser"))
        self.comboBoxActive = QtGui.QComboBox(self.groupBox)
        self.comboBoxActive.setGeometry(QtCore.QRect(10, 50, 261, 31))
        self.comboBoxActive.setObjectName(_fromUtf8("comboBoxActive"))
        self.comboBoxActive.addItem(_fromUtf8(""))
        self.comboBoxActive.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(150, 140, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnNotActiveUser = QtGui.QPushButton(self.groupBox)
        self.btnNotActiveUser.setGeometry(QtCore.QRect(9, 90, 121, 41))
        self.btnNotActiveUser.setObjectName(_fromUtf8("btnNotActiveUser"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(17, 170, 251, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(viewUsers)
        QtCore.QMetaObject.connectSlotsByName(viewUsers)

    def retranslateUi(self, viewUsers):
        viewUsers.setWindowTitle(_translate("viewUsers", "عرض المستخدمين", None))
        item = self.tableViewUsers.horizontalHeaderItem(0)
        item.setText(_translate("viewUsers", "معرف المستخدم", None))
        item = self.tableViewUsers.horizontalHeaderItem(1)
        item.setText(_translate("viewUsers", "الاسم الكامل ", None))
        item = self.tableViewUsers.horizontalHeaderItem(2)
        item.setText(_translate("viewUsers", "البريد الالكتروني", None))
        item = self.tableViewUsers.horizontalHeaderItem(3)
        item.setText(_translate("viewUsers", "رقم الهاتف", None))
        item = self.tableViewUsers.horizontalHeaderItem(4)
        item.setText(_translate("viewUsers", "الرقم الوطني", None))
        item = self.tableViewUsers.horizontalHeaderItem(5)
        item.setText(_translate("viewUsers", "تاريخ التسجيل", None))
        self.NumberUser.setText(_translate("viewUsers", "0", None))
        self.btnActiveUser.setText(_translate("viewUsers", "تفعيل المستخدم", None))
        self.textSearch.setPlaceholderText(_translate("viewUsers", "اكتب ما تود البحث عنه ", None))
        self.comboBoxActive.setItemText(0, _translate("viewUsers", "المستخدمين الفعالين", None))
        self.comboBoxActive.setItemText(1, _translate("viewUsers", "المستخدمين الغير فعالين", None))
        self.label.setText(_translate("viewUsers", "عدد المستخدمين :", None))
        self.btnNotActiveUser.setText(_translate("viewUsers", "الغاء تفعيل ", None))

import pathIcon_rc
