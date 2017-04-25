# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created: Fri Apr 14 16:47:54 2017
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

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.resize(308, 448)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Arabic Kufi"))
        login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setWindowOpacity(0.98)
        login.setLayoutDirection(QtCore.Qt.RightToLeft)
        login.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Jordan))
        self.label = QtGui.QLabel(login)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(24, 40, 271, 211))
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/login.png")))
        self.label.setScaledContents(True)
        self.label.setMargin(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.linEditUser = QtGui.QLineEdit(login)
        self.linEditUser.setEnabled(True)
        self.linEditUser.setGeometry(QtCore.QRect(16, 270, 281, 29))
        self.linEditUser.setMaxLength(20)
        self.linEditUser.setAlignment(QtCore.Qt.AlignCenter)
        self.linEditUser.setReadOnly(False)
        self.linEditUser.setObjectName(_fromUtf8("linEditUser"))
        self.lineEditPassword = QtGui.QLineEdit(login)
        self.lineEditPassword.setGeometry(QtCore.QRect(16, 320, 281, 31))
        self.lineEditPassword.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditPassword.setMaxLength(25)
        self.lineEditPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.labReturnPass = QtGui.QLabel(login)
        self.labReturnPass.setGeometry(QtCore.QRect(84, 360, 211, 31))
        self.labReturnPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labReturnPass.setObjectName(_fromUtf8("labReturnPass"))
        self.btnLogin = QtGui.QPushButton(login)
        self.btnLogin.setGeometry(QtCore.QRect(7, 398, 121, 41))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.btnClose = QtGui.QPushButton(login)
        self.btnClose.setGeometry(QtCore.QRect(177, 398, 121, 41))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.labLoginUser = QtGui.QLabel(login)
        self.labLoginUser.setGeometry(QtCore.QRect(0, 0, 308, 31))
        self.labLoginUser.setStyleSheet(_fromUtf8(""))
        self.labLoginUser.setAlignment(QtCore.Qt.AlignCenter)
        self.labLoginUser.setObjectName(_fromUtf8("labLoginUser"))

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        login.setTabOrder(self.btnClose, self.linEditUser)
        login.setTabOrder(self.linEditUser, self.lineEditPassword)
        login.setTabOrder(self.lineEditPassword, self.btnLogin)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "تسجيل الدخول", None))
        self.linEditUser.setPlaceholderText(_translate("login", "اسم المستخدم", None))
        self.lineEditPassword.setPlaceholderText(_translate("login", "كلمة المرور", None))
        self.labReturnPass.setText(_translate("login", "هل نسية كلمة المرور ؟", None))
        self.btnLogin.setText(_translate("login", "دخول", None))
        self.btnClose.setText(_translate("login", "الغاء", None))
        self.labLoginUser.setText(_translate("login", "تسجيل الدخول", None))

import pathIcon_rc
