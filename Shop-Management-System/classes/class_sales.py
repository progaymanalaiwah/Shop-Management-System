#_*_ coding: utf-8 _*_
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Gui.sales import *
from funcClasses.funClassSales import *
from connect import *
from connectFtp import *
import pdfkit,os


class sales(QWidget,Ui_sales,funClassSales):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.showDayAndTime()
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.tableSales.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSales.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableSales.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.con =connect()
        self.connectFTP = connectFtp()
        with open('Settings.Conf', 'r') as file:
            Settings = json.load(file)
        Username = Settings['Settings']['Info']['Username']
        Username = self.con.select('FullName','user','Username = "{0}"'.format(Username),2)[0]
        Category = Settings['Settings']['Info']['Category']
        self.labNameSalse.setText(Username)
        self.labNameSection.setText(Category)

        # Create Table Item And Table Customer
        self.tableSelectItem = QTableWidget()
        self.tableSelectItem.setGeometry(100,100,400,300)
        self.tableSelectItem.setColumnCount(3)
        self.tableSelectItem.setHorizontalHeaderLabels(['معرف المنتج'.decode(),'اسم المنتج'.decode(),'ثمن المنتج'.decode()])
        self.tableSelectItem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSelectItem.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableSelectItem.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSelectItem.setWindowTitle('اختيار منتج'.decode())
        self.tableSelectItem.doubleClicked.connect(self.addItemToForm)

        self.tableSelectCust = QTableWidget()
        self.tableSelectCust.setGeometry(300,300,400,300)
        self.tableSelectCust.setColumnCount(2)
        self.tableSelectCust.setHorizontalHeaderLabels(['معرف العميل'.decode(),'اسم العميل'.decode()])
        self.tableSelectCust.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSelectCust.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableSelectCust.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSelectCust.setWindowTitle('اختيار عميل'.decode())
        self.tableSelectCust.doubleClicked.connect(self.addCustToForm)
        self.btnSelectItem.setEnabled(False)


        # Run Function Clock
        self.timer = QTimer()
        self.timer.timeout.connect(self.showDayAndTime)
        self.timer.start(1000) # 10 seconds

        """ [ Start Event ] """
        self.labCalc.mousePressEvent = self.openCalc
        self.btnSelectItem.clicked.connect(self.SelectItem)
        self.textSearchItem.keyReleaseEvent = self.SearchTableItem
        self.textQu.keyReleaseEvent  = self.QuItem
        self.btnaddItem.clicked.connect(self.AddItemToTable)
        self.btnDeleteItem.clicked.connect(self.removeItemFromTable)
        self.tableSales.doubleClicked.connect(self.SelectEditItem)
        self.btnEditItem.clicked.connect(self.EditItem)
        self.labAddSales.mousePressEvent = self.AddSales
        self.labSelectCus.mousePressEvent =self.SelctCust
        self.textSearchCustomer.keyReleaseEvent = self.SearchCus
        self.labSave.mousePressEvent = self.SaveSales
        self.labPrint.mousePressEvent = self.PrintReportBill

        """ [ End Event ] """




    def PrintReportBill(self,e):
        CountSales = self.tableSales.rowCount()
        if CountSales != 0:
            self.setEnabled(False)
            self.labPrint.setEnabled(False)
            Time        = self.labTimeAndDay.text()
            BillID      = self.labBillID.text()
            NameUser    = self.labNameSalse.text()
            NameSection = self.labNameSection.text()
            NameCus     = self.labNameCus.text()
            CusID       = self.labCusID.text()
            NumberItem  = self.label_24.text()
            Toatal      = self.labTotalAll.text()
            textReport  = """
            <!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Sales</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap-rtl.min.css">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>

	<div class="container">
		<header class="header">
			<h2 class="titleMarket">شركة محمد عيسى</h2>
		</header>
			<div class="panel panel-primary">
				<div class="panel-heading" style="position: relative;">
					<table width="50%">
					  <col width="20">
  					 <col width="20">
  					 <col width="20">
  					 <col width="10">
						<tr>
							<td >عدد المنتجات : </td>
							<td class="td-color">[ {0} ]</td>
							<td >المبلغ الاجمالي :</td>
							<td class="td-color">[ {1} ]</td>
						</tr>
					</table>
					<span class="pull-left date-time">{2}</span>
					<div class="clear"></div>
				</div>
			</div>
		<div class="">

			<div class="pull-right" style="width: 49%">
				<div class="panel panel-primary">
				  <div class="panel-heading">معلومات الفاتوره</div>
				  <div class="panel-body">
					<table width="100%">
						<tr>
							<td >معرف الفاتوره :</td>
							<td>{3}</td>
						</tr>
						<tr>
							<td>اسم البائع :</td>
							<td>{4}</td>
						</tr>
						<tr>
							<td> القسم :</td>
							<td>{5}</td>
						</tr>
					</table>
				  </div>
				</div>
			</div>

			<div class="pull-left" style="width: 49%">
				<div class="panel panel-primary">
				  <div class="panel-heading">معلومات العميل</div>
				  <div class="panel-body">
					<table width="100%">
						<tr>
							<td >معرف العميل :</td>
							<td>{6}</td>
						</tr>
						<tr>
							<td>اسم العميل :</td>
							<td>{7}</td>
						</tr>

					</table>
				  </div>
				</div>
			</div>
		</div>
		<div class="clear"></div>
		<table class="table table-striped">
		  <thead>
		    <tr>
		      <th>#</th>
		      <th>معرف المنتج</th>
		      <th>اسم المنتج</th>
		      <th>الثمن</th>
		      <th>الكميه</th>
		      <th>الثمن الكلي</th>
		    </tr>
		  </thead>
		  <tbody>
            """.format(NumberItem,Toatal,Time,BillID,NameUser,NameSection,CusID,NameCus)
            file = open('report/reportSales.html', 'w')
            file.write(textReport)
            file.close()
            reportSales = open('report/reportSales.html', 'a+')
            number = 1
            for i in range(CountSales):
                textNew = """
                	<tr>
                      <th scope="row">{0}</th>
                      <td>{1}</td>
                      <td>{2}</td>
                      <td>{3}</td>
                      <td>{4}</td>
                      <td>{5}</td>
                    </tr>
                """.format(number,
                           self.tableSales.item(i,0).text(),
                           self.tableSales.item(i, 1).text(),
                           self.tableSales.item(i, 2).text(),
                           self.tableSales.item(i, 3).text(),
                           self.tableSales.item(i, 4).text())
                reportSales.write(textNew)
                number +=1
            reportSales.write("""
            		  </tbody>
                    </table>
                </div>
                <script src="js/jquery-3.2.1.min.js"></script>
                <script src="js/bootstrap.min.js"></script>
                <script src="js/main.js"></script>
            </body>
            </html>
            """)
            reportSales.close()

            saveReport = QFileDialog.getSaveFileNameAndFilter(self,'حفظ التقرير'.decode(),'ReportSales.pdf','*.pdf')[0]
            if saveReport:
                config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
                convert  = pdfkit.from_file('report/reportSales.html',str(saveReport),configuration=config)
                if convert:
                    QMessageBox.information(self,'حفظ الفاتوره'.decode(),'تم حفظ الفاتوره في المسار \n [ {} ]'.decode().format(saveReport))
            self.setEnabled(True)
            try:
                os.system("start "+str(saveReport))
            except:pass
            self.labAddSales.setEnabled(True)
            self.Cancel()



    def Cancel(self):
        self.labTotalAll.setText("")
        self.label_24.setText("")
        self.labPrint.setEnabled(False)
        self.labBillID.setText("")
        self.labCusID.setText("")
        self.labNameCus.setText("")
        self.textItemID.clear()
        self.textItemName.clear()
        self.textTotalItem.clear()
        self.textSearchCustomer.clear()
        self.textItemPrice.clear()
        self.textQu.clear()
        self.textSearchItem.clear()
        self.btnaddItem.setEnabled(False)
        self.tableSales.setRowCount(0)
        self.labSelectCus.setPixmap(QPixmap(":/template/images/UserDefault.png"))
