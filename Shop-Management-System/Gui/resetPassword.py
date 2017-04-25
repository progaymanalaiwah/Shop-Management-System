# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resetPassword.ui'
#
# Created: Fri Apr 14 16:49:34 2017
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

class Ui_resetPassword(object):
    def setupUi(self, resetPassword):
        resetPassword.setObjectName(_fromUtf8("resetPassword"))
        resetPassword.resize(470, 175)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/resetPassword.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resetPassword.setWindowIcon(icon)
        resetPassword.setLayoutDirection(QtCore.Qt.RightToLeft)
        resetPassword.setStyleSheet(_fromUtf8(""))
        resetPassword.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.SaudiArabia))
        self.label = QtGui.QLabel(resetPassword)
        self.label.setGeometry(QtCore.QRect(11, 10, 171, 151))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/resetPassword.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.textUsername = QtGui.QLineEdit(resetPassword)
        self.textUsername.setGeometry(QtCore.QRect(200, 10, 261, 31))
        self.textUsername.setObjectName(_fromUtf8("textUsername"))
        self.textEmail = QtGui.QLineEdit(resetPassword)
        self.textEmail.setGeometry(QtCore.QRect(200, 50, 261, 31))
        self.textEmail.setObjectName(_fromUtf8("textEmail"))
        self.textNumberID = QtGui.QLineEdit(resetPassword)
        self.textNumberID.setGeometry(QtCore.QRect(200, 90, 261, 31))
        self.textNumberID.setObjectName(_fromUtf8("textNumberID"))
        self.btnReset = QtGui.QPushButton(resetPassword)
        self.btnReset.setGeometry(QtCore.QRect(350, 130, 111, 41))
        self.btnReset.setObjectName(_fromUtf8("btnReset"))
        self.btnLoginReset = QtGui.QPushButton(resetPassword)
        self.btnLoginReset.setGeometry(QtCore.QRect(200, 130, 111, 41))
        self.btnLoginReset.setObjectName(_fromUtf8("btnLoginReset"))
        self.textNewPasword = QtGui.QLineEdit(resetPassword)
        self.textNewPasword.setEnabled(False)
        self.textNewPasword.setGeometry(QtCore.QRect(200, 50, 261, 31))
        self.textNewPasword.setObjectName(_fromUtf8("textNewPasword"))
        self.textCheckPassword = QtGui.QLineEdit(resetPassword)
        self.textCheckPassword.setEnabled(False)
        self.textCheckPassword.setGeometry(QtCore.QRect(200, 90, 261, 31))
        self.textCheckPassword.setObjectName(_fromUtf8("textCheckPassword"))
        self.btnOkRestPassword = QtGui.QPushButton(resetPassword)
        self.btnOkRestPassword.setGeometry(QtCore.QRect(350, 130, 111, 41))
        self.btnOkRestPassword.setObjectName(_fromUtf8("btnOkRestPassword"))
        self.textaddCode = QtGui.QLineEdit(resetPassword)
        self.textaddCode.setGeometry(QtCore.QRect(200, 10, 261, 31))
        self.textaddCode.setObjectName(_fromUtf8("textaddCode"))
        self.btnCheckCode = QtGui.QPushButton(resetPassword)
        self.btnCheckCode.setGeometry(QtCore.QRect(350, 130, 111, 41))
        self.btnCheckCode.setObjectName(_fromUtf8("btnCheckCode"))

        self.retranslateUi(resetPassword)
        QtCore.QMetaObject.connectSlotsByName(resetPassword)

    def retranslateUi(self, resetPassword):
        resetPassword.setWindowTitle(_translate("resetPassword", "اعادت تعيني كلمة المرور", None))
        self.textUsername.setPlaceholderText(_translate("resetPassword", "اسم المستخدم", None))
        self.textEmail.setPlaceholderText(_translate("resetPassword", "البريد الالكتروني", None))
        self.textNumberID.setPlaceholderText(_translate("resetPassword", "الرقم الوطني", None))
        self.btnReset.setText(_translate("resetPassword", "استعاده", None))
        self.btnLoginReset.setText(_translate("resetPassword", "تسجيل الدخول", None))
        self.textNewPasword.setPlaceholderText(_translate("resetPassword", "كلمة المرور", None))
        self.textCheckPassword.setPlaceholderText(_translate("resetPassword", "اعادة كتابت كلمة المرور", None))
        self.btnOkRestPassword.setText(_translate("resetPassword", "تعين كلمة المرور", None))
        self.textaddCode.setPlaceholderText(_translate("resetPassword", "ادخل الكود", None))
        self.btnCheckCode.setText(_translate("resetPassword", "تحقق", None))

import pathIcon_rc
