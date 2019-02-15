import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Pic(QWidget):
    def __init__(self, parent):
        super(Pic, self).__init__()
        self.win = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setMaximumWidth(1320)
        self.InitializeViews()
        pass

    def InitializeViews(self):
        self.pic_lb = QLabel(self,objectName='pic_lb')
        self.pic_btn = QLabel(self,objectName='pic_btn')
        self.pic_ext = QPushButton(self,objectName='pic_ext')
        self.pic_lb.setFixedSize(1291,322)
        self.pic_lb.setPixmap((QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/label_viz.png').scaled(1230,322)))
        self.pic_btn.setPixmap(QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/pic_btn.png'))
        self.pic_ext.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/ext.PNG'))
        self.pic_ext.setIconSize(QSize(60,60))
        self.setMaximumWidth(1320)
        self.pic_btn.setMaximumHeight(40)
        self.vlay = QVBoxLayout()
        self.hlay = QHBoxLayout()
        self.up_hlay = QHBoxLayout()
        self.setLayout(self.vlay)
        
        self.up_hlay.addStretch(1)
        self.up_hlay.addWidget(self.pic_ext)
        self.vlay.addLayout(self.up_hlay)
        self.vlay.addWidget(self.pic_lb)
        self.hlay.addStretch(1)
        self.hlay.addWidget(self.pic_btn)
        self.hlay.addStretch(1)
        self.vlay.addLayout(self.hlay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Pic(None)
    win.show()
    sys.exit(app.exec_())
    pass