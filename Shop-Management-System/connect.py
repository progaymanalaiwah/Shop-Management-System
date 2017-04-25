import MySQLdb
import xml.etree.ElementTree as EL
import json
class connect():
    def __init__(self):


        with open('Settings.Conf') as f:
            infoConnectDB = json.load(f)


        host   = infoConnectDB['Settings']['DB']['Host']
        user   = infoConnectDB['Settings']['DB']['Username']
        nameDB = infoConnectDB['Settings']['DB']['Name']
        pwd    = infoConnectDB['Settings']['DB']['Password'] if None else  ''
        self.con = self.connectDB(host,user,pwd,nameDB)

    #function Connect Databas
    def connectDB(self,host,user,pwd,nameDB):
        try:
            con = MySQLdb.connect(host,user,pwd,nameDB,use_unicode=True, charset="utf8")
            return con
        except Exception as e:

            print("Error Connect Database : " + str(e))


    """
    Function Update Value COntent Of DataBase
    And Return If Delete True Not Delete Return False
    sql = UPDATE NameTable SEL (`Username` = 'admin',Password = 'aadmin123456') WHERE UserID = 1
    """
    def update(self,NameTable,ColumnAndValue,Where):
        sql = """UPDATE {0} SET {1} WHERE {2}""".format(NameTable,ColumnAndValue,Where)
        print sql
        con = self.con.cursor()
        result = con.execute(sql)
        self.con.commit()
        return result

    """
    Function Delete Value Of Database
    """
    def delete(self,NameTable,NameColumn,ID):
        con = self.con.cursor()
        sql = "DELETE FROM {0} WHERE {1} = {2}".format(NameTable,NameColumn,ID)
        result = con.execute(sql)
        self.con.commit()
        if result:
            return True
        else:return False


    """
    Function Insert Database
    Variable
        - INSER INTO NameTable(ColumnTable)VALUES (ColumnValue)
    """
    def insert(self,NameTable,ColumnTable,ColumnValue):
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(NameTable,ColumnTable,ColumnValue)
        print sql
        con = self.con.cursor()
        result = con.execute(sql)
        self.con.commit()
        if result:return True
        else     :return False


    """
    function Select Database
    variable
        - nameColumn: Name Column Table
        - nameTable : Name Table Database
        - where: Default False Not Where
            if where True = Example:
            valueWhere : Username = admin
        - typeReturn: Default 0 Return FetchAll
            - 1 Return rowcount
            - 2 Return fetchone
    """
    def select(self,nameColumn,nameTabel,where = False,typeReturn = 0):
        if where == False : where = ''
        else:where = "WHERE " + where
        sql = """
        SELECT %s FROM %s %s
        """ %(nameColumn,nameTabel,where)
        print sql

        con = self.con.cursor()
        try:
            con.execute(sql)
            if typeReturn == 0:
                return con.fetchall()
            elif typeReturn == 1:
                return con.rowcount
            elif typeReturn == 2:
                return con.fetchone()
        except:
            self.con.rollback()
            self.con.close()
            con.close()
            print "Error Execute Run Query"
            return False

    """
    Function Check Of Value IF Found Database Or Not Found
    If Found Return True If Not Found Return  False
    """
    def checkData(self,NameTable,NameColumn,Date,where= False):
        Count = self.select(NameColumn,NameTable,"{0} = {1}".format(NameColumn,Date),1)
        if Count > 0 :return True
        else:return False

