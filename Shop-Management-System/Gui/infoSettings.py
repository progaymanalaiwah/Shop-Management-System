# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\infoSettings.ui'
#
# Created: Fri Apr 14 11:10:51 2017
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

class Ui_infoSettings(object):
    def setupUi(self, infoSettings):
        infoSettings.setObjectName(_fromUtf8("infoSettings"))
        infoSettings.resize(350, 127)
        infoSettings.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textUsername = QtGui.QLineEdit(infoSettings)
        self.textUsername.setGeometry(QtCore.QRect(10, 10, 331, 31))
        self.textUsername.setObjectName(_fromUtf8("textUsername"))
        self.textPassowrd = QtGui.QLineEdit(infoSettings)
        self.textPassowrd.setGeometry(QtCore.QRect(10, 50, 331, 31))
        self.textPassowrd.setObjectName(_fromUtf8("textPassowrd"))
        self.btnLogin = QtGui.QPushButton(infoSettings)
        self.btnLogin.setGeometry(QtCore.QRect(10, 90, 331, 31))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))

        self.retranslateUi(infoSettings)
        QtCore.QMetaObject.connectSlotsByName(infoSettings)

    def retranslateUi(self, infoSettings):
        infoSettings.setWindowTitle(_translate("infoSettings", "تسجيل الدخول", None))
        self.textUsername.setPlaceholderText(_translate("infoSettings", "اسم االمستخدم", None))
        self.textPassowrd.setPlaceholderText(_translate("infoSettings", "كلمة المرور", None))
        self.btnLogin.setText(_translate("infoSettings", "دخول", None))

