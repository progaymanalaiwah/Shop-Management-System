#_*_ coding: utf-8 _*_
import sys,os,json
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
import connect
import unicodedata
PORT = 9999
SIZEOF_UINT32 = 4

class ServerDlg(QPushButton):

    def __init__(self, parent=None):
        super(ServerDlg, self).__init__(
                "&Close Server", parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.tcpServer = QTcpServer(self)
        self.tcpServer.listen(QHostAddress("0.0.0.0"), PORT)
        self.connect(self.tcpServer, SIGNAL("newConnection()"),
                    self.addConnection)
        self.connections = []
        with open('Settings.Conf') as f:
            Settings = json.load(f)

        self.Username = str(Settings['Settings']['Info']['Username'])



        #self.connect(self, SIGNAL("clicked()"), self.close())

    def addConnection(self):
        clientConnection = self.tcpServer.nextPendingConnection()
        clientConnection.nextBlockSize = 0
        self.connections.append(clientConnection)

        self.connect(clientConnection, SIGNAL("readyRead()"),
                self.receiveMessage)
        self.connect(clientConnection, SIGNAL("disconnected()"),
                self.removeConnection)
        self.connect(clientConnection, SIGNAL("error()"),
                self.socketError)

    def receiveMessage(self):
        for s in self.connections:
            if s.bytesAvailable() > 0:
                stream = QDataStream(s)
                stream.setVersion(QDataStream.Qt_4_2)

                if s.nextBlockSize == 0:
                    if s.bytesAvailable() < SIZEOF_UINT32:
                        return
                    s.nextBlockSize = stream.readUInt32()
                if s.bytesAvailable() < s.nextBlockSize:
                    return

                textFromClient = str(stream.readQString()).decode()
                s.nextBlockSize = 0
                self.sendMessage(textFromClient,
                                 s.socketDescriptor())
                s.nextBlockSize = 0

    def sendMessage(self, text, socketId):
        for s in self.connections:
            if s.socketDescriptor() == socketId:
                message = "<span style='color:#d35400'>You></span>  {}<br>".format(text)

            else:
                message = "<span style='color:#d35400'>{}> </span>  {}<br>".format(self.Username,text)

            reply = QByteArray()
            stream = QDataStream(reply, QIODevice.WriteOnly)
            stream.setVersion(QDataStream.Qt_4_2)
            stream.writeUInt32(0)
            stream.writeString(message)
            stream.device().seek(0)
            stream.writeUInt32(reply.size() - SIZEOF_UINT32)
            s.write(reply)

    def removeConnection(self):
        pass

    def socketError(self):
        pass



