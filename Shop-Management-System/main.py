from classes.class_login import *
import sys,json
from classes.class_employes import *
from classes.class_infoSettings import *

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("fonts/DroidKufi-Regular.ttf")
    with open('Settings.Conf') as f:
        theme = json.load(f)
    with open(theme['Settings']['Info']['Theme']) as style:
        style = style.read()
    try:
        Main = login()
        Main.show()
    except:
        setting = infoSettings()
        setting.show()


    app.setStyleSheet(style)
    app.exec_()
if __name__ == '__main__':main()

