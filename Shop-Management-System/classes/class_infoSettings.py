#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.infoSettings import *
import json,hashlib
from classes.class_Settings import *
class infoSettings(QWidget,Ui_infoSettings):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.Se = Settings()

        self.btnLogin.clicked.connect(self.loginSettings)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())



    def loginSettings(self):
        with open('Settings.Conf') as f:
            Info  = json.load(f)
        InfoSettings = Info['Settings']['InfoSettings']
        Username = hashlib.sha1(self.textUsername.text()).hexdigest()
        password = hashlib.sha1(self.textPassowrd.text()).hexdigest()
        if Username == InfoSettings['Username'] and password == InfoSettings['Password']:
            self.Se.show()
            self.close()
