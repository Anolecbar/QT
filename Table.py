import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Table(QWidget):
    def __init__(self, parent):
        super(Table, self).__init__()
        self.win = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setMaximumWidth(440)
        self.InitializeViews()
        pass

    def InitializeViews(self):
        self.t_btn = QPushButton(self,objectName='t_btn')
        self.t_menu = QLabel(self,objectName='t_menu')
        self.t_pictable = QWidget(self,objectName='t_pictable')
        self.t_pic1 = QLabel(self,objectName='t_pic1')
        self.t_pic2 = QLabel(self,objectName='t_pic2')
        
        self.t_pic1.setFixedSize(380,380)
        self.t_pic2.setFixedSize(380,380)
        self.t_btn.setFixedSize(160,40)
        self.t_pictable.setMinimumHeight(850)

        self.t_btn.setText('图  像')
        self.t_menu.setPixmap(QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/t_menu.jpg'))
        self.t_pic1.setPixmap(QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/img_1.png'))
        self.t_pic2.setPixmap(QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/img_2.png'))
        #self.t_pic1.setPixmap((QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/img_1.png').scaled(360,100)))
        #self.t_pic2.setPixmap((QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/img_2.png').scaled(360,100)))

        self.lay = QVBoxLayout()
        self.pic_lay = QVBoxLayout()
        self.setLayout(self.lay)
        self.t_pictable.setLayout(self.pic_lay)
        self.lay.addWidget(self.t_btn)
        self.lay.addWidget(self.t_menu)
        self.lay.addSpacing(20)
        self.lay.addWidget(self.t_pictable)
        self.lay.addStretch(1)
        self.pic_lay.addWidget(self.t_pic1)
        self.pic_lay.addWidget(self.t_pic2)

        self.lay.setSpacing(0)
        self.pic_lay.setContentsMargins(10, 10, 10, 10)
        

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Table(None)
    win.show()
    sys.exit(app.exec_())
    pass
