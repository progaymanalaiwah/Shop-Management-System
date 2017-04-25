# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Item.ui'
#
# Created: Thu Apr 13 20:31:53 2017
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

class Ui_Item(object):
    def setupUi(self, Item):
        Item.setObjectName(_fromUtf8("Item"))
        Item.setWindowModality(QtCore.Qt.ApplicationModal)
        Item.resize(631, 271)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Arabic Kufi"))
        font.setItalic(False)
        Item.setFont(font)
        Item.setLayoutDirection(QtCore.Qt.RightToLeft)
        Item.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Jordan))
        self.lineEditNameItem = QtGui.QLineEdit(Item)
        self.lineEditNameItem.setGeometry(QtCore.QRect(320, 10, 301, 29))
        self.lineEditNameItem.setObjectName(_fromUtf8("lineEditNameItem"))
        self.lineEditPrice = QtGui.QLineEdit(Item)
        self.lineEditPrice.setGeometry(QtCore.QRect(170, 10, 141, 29))
        self.lineEditPrice.setObjectName(_fromUtf8("lineEditPrice"))
        self.labAddImageItem = QtGui.QLabel(Item)
        self.labAddImageItem.setGeometry(QtCore.QRect(10, 100, 171, 161))
        self.labAddImageItem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labAddImageItem.setText(_fromUtf8(""))
        self.labAddImageItem.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/defaultItem.png")))
        self.labAddImageItem.setScaledContents(True)
        self.labAddImageItem.setObjectName(_fromUtf8("labAddImageItem"))
        self.lineEditDateOfProduction = QtGui.QLineEdit(Item)
        self.lineEditDateOfProduction.setGeometry(QtCore.QRect(330, 50, 291, 29))
        self.lineEditDateOfProduction.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditDateOfProduction.setReadOnly(False)
        self.lineEditDateOfProduction.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditDateOfProduction.setObjectName(_fromUtf8("lineEditDateOfProduction"))
        self.lineEditCompletionDate = QtGui.QLineEdit(Item)
        self.lineEditCompletionDate.setGeometry(QtCore.QRect(10, 50, 291, 29))
        self.lineEditCompletionDate.setReadOnly(False)
        self.lineEditCompletionDate.setObjectName(_fromUtf8("lineEditCompletionDate"))
        self.comBoxCategoryItem = QtGui.QComboBox(Item)
        self.comBoxCategoryItem.setGeometry(QtCore.QRect(220, 130, 401, 31))
        self.comBoxCategoryItem.setObjectName(_fromUtf8("comBoxCategoryItem"))
        self.lineEditQuentity = QtGui.QLineEdit(Item)
        self.lineEditQuentity.setGeometry(QtCore.QRect(10, 10, 141, 29))
        self.lineEditQuentity.setObjectName(_fromUtf8("lineEditQuentity"))
        self.btnAddItem = QtGui.QPushButton(Item)
        self.btnAddItem.setGeometry(QtCore.QRect(230, 190, 121, 41))
        self.btnAddItem.setObjectName(_fromUtf8("btnAddItem"))
        self.btnCancel = QtGui.QPushButton(Item)
        self.btnCancel.setGeometry(QtCore.QRect(470, 190, 121, 41))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.comboxStoreItem = QtGui.QComboBox(Item)
        self.comboxStoreItem.setGeometry(QtCore.QRect(220, 90, 401, 31))
        self.comboxStoreItem.setObjectName(_fromUtf8("comboxStoreItem"))
        self.btnEditItem = QtGui.QPushButton(Item)
        self.btnEditItem.setGeometry(QtCore.QRect(350, 220, 121, 41))
        self.btnEditItem.setObjectName(_fromUtf8("btnEditItem"))
        self.labItemID = QtGui.QLabel(Item)
        self.labItemID.setGeometry(QtCore.QRect(210, 250, 62, 15))
        self.labItemID.setObjectName(_fromUtf8("labItemID"))
        self.labUserID = QtGui.QLabel(Item)
        self.labUserID.setGeometry(QtCore.QRect(270, 250, 62, 15))
        self.labUserID.setObjectName(_fromUtf8("labUserID"))

        self.retranslateUi(Item)
        QtCore.QMetaObject.connectSlotsByName(Item)

    def retranslateUi(self, Item):
        Item.setWindowTitle(_translate("Item", "المنتجات", None))
        self.lineEditNameItem.setPlaceholderText(_translate("Item", "اسم المنتج", None))
        self.lineEditPrice.setPlaceholderText(_translate("Item", "الثمن", None))
        self.lineEditDateOfProduction.setPlaceholderText(_translate("Item", "2020-12-20 :  تاريخ الانتاج", None))
        self.lineEditCompletionDate.setPlaceholderText(_translate("Item", "2017-12-20 : تاريخ الانتهاء", None))
        self.comBoxCategoryItem.setToolTip(_translate("Item", "اختر صنف المنتج", None))
        self.lineEditQuentity.setPlaceholderText(_translate("Item", "الكميه", None))
        self.btnAddItem.setText(_translate("Item", "اظافة", None))
        self.btnCancel.setText(_translate("Item", "الغاء", None))
        self.comboxStoreItem.setToolTip(_translate("Item", "اختر مكان التخزين", None))
        self.btnEditItem.setText(_translate("Item", "تعديل الصنف", None))
        self.labItemID.setText(_translate("Item", "ItemID", None))
        self.labUserID.setText(_translate("Item", "UserID", None))

import pathIcon_rc
