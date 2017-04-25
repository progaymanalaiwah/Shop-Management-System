#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from classes.class_mainWindow import *
import sys

class funClassMainWindow:

    #function Close All Project Even menu Logout
    def closeAll(self):
        MsgLogOut = QMessageBox.question(self,'تسجيل الخروج'.decode('UTF-8'),'هل انت متئكد من تسجيل الخروج'.decode('UTF-8'),
                                         QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if MsgLogOut == QMessageBox.Yes:
            sys.exit()
