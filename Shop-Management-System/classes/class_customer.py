#_*_ coding:utf8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.Customers import *
from funcClasses.funCustomers import *
from connect import *
from connectFtp import *
import urllib
class customers(QWidget,Ui_Customers,funCustomers):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.tableCustomer.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableCustomer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCustomer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCustomer.setColumnHidden(6,True)
        self.tableCustomer.setColumnHidden(7,True)
        self.labCustID.setVisible(False)
        self.labUserID.setVisible(False)

        # Object Of Class Connect Database
        self.con = connect()
        # Object Of Class ConnectFtp Server
        self.connectFTP = connectFtp()

        # Function Show Customers Of Table
        self.ShowCustomers()

        """ [ Start Run Function Event ] """
        # Run Function AddCustomers
        self.btnCustomerAdd.clicked.connect(self.AddCustomers)
        self.btnCancel.clicked.connect(self.Cancel)
        self.btnCustomerEdit.clicked.connect(self.EditCustomer)
        self.labCustomerImage.mouseDoubleClickEvent = self.SelectImageCustomer
        self.comboBoxSelectActive.activated.connect(self.ShowCustomers)
        self.tableCustomer.doubleClicked.connect(self.ShowInfoOfForm)
        self.btnCustomerActive.clicked.connect(self.ActiveCustomer)
        self.btnCustomerNotActivet.clicked.connect(self.ActiveCustomer)
        self.lineEditCustomerSearch.keyReleaseEvent = self.SearchCustomers
        """ [ End Run Function Event ] """



    def SearchCustomers(self,e):
        Search = self.lineEditCustomerSearch.text()
        typeCustomers = str(self.comboBoxSelectActive.currentText())
        if typeCustomers == "العملاء الفعالين":
            ActiveCustomers = 1
        else:
            ActiveCustomers = 0

        # if Form Search Empty Run Function ShowCustomers Import All Section Of Database
        if  Search == "" or Search == " " or not Search:
            self.ShowCustomers()

        else:
            like = "customers.CustomersID LIKE '%{0}%' OR customers.CustomersName LIKE '%{1}%' OR customers.CustomersPhone LIKE '%{2}%' OR customers.CustomersEmail LIKE '%{3}%' OR customers.CustomersDate LIKE '%{4}%' OR user.Username LIKE '%{5}%'".format(Search,Search,Search,Search,Search,Search)
            sql = """SELECT customers.*,user.Username FROM customers INNER JOIN user on customers.UserID = user.UserID WHERE ({0}) AND customers.CustomersActive = {1}""".format(like,ActiveCustomers)
            print sql
            con = self.con.con # Variable Connect Database
            con = con.cursor()
            con.execute(sql)
            SearchResult = con.fetchall()
            lenghtData = len(SearchResult)

            self.tableCustomer.setRowCount(int(lenghtData))
            Row = 0 # Number Row Of Table
            # Insert Search Result Of Table Section
            for info in SearchResult:
                if Row > lenghtData:break
                self.tableCustomer.setItem(Row,0,QTableWidgetItem(str(info[0])))
                self.tableCustomer.setItem(Row,1,QTableWidgetItem(str(info[1]).decode("UTF-8")))
                self.tableCustomer.setItem(Row, 2, QTableWidgetItem(str(info[3]).decode("UTF-8")))
                self.tableCustomer.setItem(Row, 3, QTableWidgetItem(str(info[2]).decode("UTF-8")))
                self.tableCustomer.setItem(Row, 4, QTableWidgetItem(str(info[5]).decode("UTF-8")))
                self.tableCustomer.setItem(Row, 5, QTableWidgetItem(str(info[10]).decode("UTF-8")))
                self.tableCustomer.setItem(Row, 6, QTableWidgetItem(str(info[7]).decode("UTF-8")))
                self.tableCustomer.setItem(Row, 7, QTableWidgetItem(str(info[6]).decode("UTF-8")))
                Row+=1 # Incrimiate Steb By 1















