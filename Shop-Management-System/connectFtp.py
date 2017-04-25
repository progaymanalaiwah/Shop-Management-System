from ftplib import FTP
import xml.etree.ElementTree as EL
import json
class connectFtp:

    def __init__(self):
        with open('Settings.Conf') as f:
            infoConnectFTP = json.load(f)
        self.NameFile = "Market"
        self.HOSTFTP = infoConnectFTP['Settings']['FTP']['Host']
        USERFTP = infoConnectFTP['Settings']['FTP']['Username']
        PWDFTP = infoConnectFTP['Settings']['FTP']['Password']
        self.ftp = self.loginFtp(self.HOSTFTP,USERFTP,PWDFTP)

    # Function Login Of Server FTP
    def loginFtp(self,HostFTP,UserFTP,PwdFtp):
        NameFile = 'Market'
        try:
            # Connect FTP
            ftp = FTP(HostFTP,UserFTP,PwdFtp)
        except Exception as e:
            print e

        # Content Of Files Of Dir FTP
        directoryOfFils = ftp.nlst()
        if NameFile in directoryOfFils:pass
        else:
            ftp.mkd(self.NameFile)
        ftp.cwd("/{0}".format(NameFile))
        return ftp


    # Function Upload File To Ftp Server
    def UploadFileFtp(self,directory,pathFile,NameFile):
        try:
            Files = self.ftp.nlst()
        except:
            Files = self.ftp.nlst()
        if directory in Files:pass
        else:self.ftp.mkd(directory)
        self.ftp.cwd(directory)
        File = open(pathFile,"rb")
        result = self.ftp.storbinary("STOR " +str(NameFile),File,1024)
        self.ftp.cwd("../")
        if result:return True
        else: return False









