#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.employes import *
from funcClasses.funEmployes import *
from connect import *
from connectFtp import *
import urllib
import pdfkit
from PyQt4.QtWebKit import *
class employes(QWidget,Ui_employes,funEmployes):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tableEmployes.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableEmployes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEmployes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.labUserID.setVisible(False)


        # Object From Class Connect Database
        self.con = connect()
        # Object From Class Connect FTP Server
        self.connectFTP = connectFtp()

        # Run Function At Show Form
        self.ShowSection()
        self.showEmployes()

        """[ Start Event ]"""
        self.btnEmploAdd.clicked.connect(self.addEmployee)
        self.btnCancel.clicked.connect(self.Cancel)
        self.labEmploye.mouseDoubleClickEvent = self.SelectImageEployee
        self.btnEmploNotActive.clicked.connect(self.ActiveEmploye)
        self.btnEmploActive.clicked.connect(self.ActiveEmploye)
        self.comboxEmploActive.activated.connect(self.showEmployes)
        self.textEmploSearch.keyReleaseEvent = self.SearchEmploye
        self.tableEmployes.mouseDoubleClickEvent = self.infoEmployesOfForm
        self.btnEmploEdit.clicked.connect(self.editEmployes)
        self.comboxEmploReport.activated.connect(self.reportEmployes)
        """[ End Event ]"""




    def reportEmployes(self):
        typeReport = str(self.comboxEmploReport.currentText())
        if typeReport == 'كل الموظفين':
            self.setEnabled(False)
            self.createReportHtmlPage()
            saveReport = QFileDialog.getSaveFileNameAndFilter(self,'حفظ التقرير'.decode('utf-8'),'ReportEmployees','*.pdf')[0]
            try:
                if not saveReport:
                    self.setEnabled(True)
                    return False
                config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
                convert = pdfkit.from_file('report/reportEmployees.html', str(saveReport), configuration=config)
                if convert:
                    QMessageBox.information(self, 'طباعة تقرير'.decode('utf-8'),
                                            'تم انشاء تقرير الموظفين بنجاح'.decode('utf-8'))
                try:
                    os.system("start " + str(saveReport))
                except:
                    pass
                self.setEnabled(True)
            except:
                self.setEnabled(True)
                return False




