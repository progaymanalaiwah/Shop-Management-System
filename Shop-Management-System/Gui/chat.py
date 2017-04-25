# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\chat.ui'
#
# Created: Fri Apr 14 19:05:14 2017
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

class Ui_chat(object):
    def setupUi(self, chat):
        chat.setObjectName(_fromUtf8("chat"))
        chat.resize(353, 329)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/chat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        chat.setWindowIcon(icon)
        self.textBrowserShowMessage = QtGui.QTextBrowser(chat)
        self.textBrowserShowMessage.setGeometry(QtCore.QRect(6, 10, 341, 271))
        self.textBrowserShowMessage.setObjectName(_fromUtf8("textBrowserShowMessage"))
        self.textMessage = QtGui.QLineEdit(chat)
        self.textMessage.setEnabled(False)
        self.textMessage.setGeometry(QtCore.QRect(10, 290, 291, 31))
        self.textMessage.setObjectName(_fromUtf8("textMessage"))
        self.labConnectServer = QtGui.QLabel(chat)
        self.labConnectServer.setGeometry(QtCore.QRect(305, 290, 41, 31))
        self.labConnectServer.setText(_fromUtf8(""))
        self.labConnectServer.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/connect.png")))
        self.labConnectServer.setScaledContents(True)
        self.labConnectServer.setObjectName(_fromUtf8("labConnectServer"))
        self.idUser = QtGui.QLabel(chat)
        self.idUser.setGeometry(QtCore.QRect(70, 360, 51, 31))
        self.idUser.setObjectName(_fromUtf8("idUser"))

        self.retranslateUi(chat)
        QtCore.QMetaObject.connectSlotsByName(chat)

    def retranslateUi(self, chat):
        chat.setWindowTitle(_translate("chat", "محادثه", None))
        self.labConnectServer.setToolTip(_translate("chat", "الاتصال بل سيرفير", None))
        self.idUser.setText(_translate("chat", "LabUserID", None))

import pathIcon_rc
