import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Titlebar import *
from Menu import *
from Pic import *
from Table import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.InitializeWindow()
    
    def InitializeWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100,100,1280,800)
        self.InitializeViews()
        self.setStyleSheet(str(self.LoadStyleFromQss('C:/Users/Lenovo/Desktop/QT/QSS.qss')))
    
    def InitializeViews(self):
        self.titleBar = TitleBar(self)
        self.menu = Menu(self)
        self.pic = Pic(self)
        self.tabel = Table(self)
        self.center = QWidget(self)
        self.client = QWidget(self,objectName='client')
        self.setCentralWidget(self.center)

        self.vlayout = QVBoxLayout(self)
        self.hlayout = QHBoxLayout(self)
        self.cli_lay = QHBoxLayout(self)


        self.vlayout.addWidget(self.titleBar)
        self.hlayout.addWidget(self.menu)
        self.cli_lay.addWidget(self.pic)
        self.cli_lay.addStretch(1)
        self.hlayout.addWidget(self.client)
        self.hlayout.addWidget(self.tabel)
        self.vlayout.addLayout(self.hlayout)
        self.center.setLayout(self.vlayout)
        self.client.setLayout(self.cli_lay)

        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        

        self.titleBar.SetIcon(QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/title.png'))
        self.titleBar.SetTitle('医 学 影 像 工 作 站')


    def LoadStyleFromQss(self, f):
        file = open(f)
        lines = file.readlines()
        file.close()
        res = ''
        for line in lines:
            res += line
        return res


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())
    pass

