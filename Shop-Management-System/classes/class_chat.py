#_*_ coding: utf-8 _*_
from funcClasses.funClassAddUsers import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from Gui.chat import *
import unicodedata

PORTS = (9998, 9999)
PORT = 9999
SIZEOF_UINT32 = 4

class chat(QWidget,Ui_chat):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.socket = QTcpSocket()

        self.nextBlockSize = 0
        self.request = None

        self.textMessage.returnPressed.connect(self.issueRequest)
        self.labConnectServer.mousePressEvent = self.connectToServer

        self.socket.readyRead.connect(self.readFromServer)
        self.socket.disconnected.connect(self.serverHasStopped)
        self.connect(self.socket,
                     SIGNAL("error(QAbstractSocket::SocketError)"),
                     self.serverHasError)

        with open('Settings.Conf','r') as file:
            Settings = json.load(file)
        self.DB        = Settings['Settings']['DB']


    # Update GUI
    def updateUi(self, text):
        self.textBrowserShowMessage.insertHtml(str(text).decode())
        self.textBrowserShowMessage.moveCursor(QTextCursor.End)

    # Create connection to server
    def connectToServer(self,e):
        self.labConnectServer.setEnabled(False)
        self.socket.connectToHost(self.DB['Host'], PORT)
        self.textMessage.setEnabled(True)

    def issueRequest(self):
        self.request = QByteArray()
        stream = QDataStream(self.request, QIODevice.WriteOnly)


        stream.setVersion(QDataStream.Qt_4_2)
        stream.writeUInt32(0)
        stream.writeQString(self.textMessage.text())
        stream.device().seek(0)
        stream.writeUInt32(self.request.size() - SIZEOF_UINT32)
        self.socket.write(self.request)

        self.nextBlockSize = 0
        self.request = None
        self.textMessage.setText("")

    def readFromServer(self):
        stream = QDataStream(self.socket)
        stream.setVersion(QDataStream.Qt_4_2)

        while True:
            if self.nextBlockSize == 0:
                if self.socket.bytesAvailable() < SIZEOF_UINT32:
                    break
                self.nextBlockSize = stream.readUInt32()
            if self.socket.bytesAvailable() < self.nextBlockSize:
                break
            textFromServer = stream.readString()

            self.updateUi(textFromServer)
            self.nextBlockSize = 0

    def serverHasStopped(self):
        self.socket.close()
        self.labConnectServer.setEnabled(True)
        self.textMessage.setEnabled(False)

    def serverHasError(self):
        self.updateUi("Error: {} ".format(
                self.socket.errorString()))
        self.socket.close()
        self.labConnectServer.setEnabled(True)
        self.textMessage.setEnabled(False)