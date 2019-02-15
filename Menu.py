import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Menu(QWidget):
    def __init__(self, parent):
        super(Menu, self).__init__()
        self.win = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setMaximumWidth(220)
        self.InitializeViews()
        pass

    def InitializeViews(self):
        self.lb = QLabel(self,objectName='ad_lb')
        self.f_btn1 = QPushButton(self,objectName='f_btn1')
        self.f_btn2 = QPushButton(self,objectName='f_btn2')
        self.f_btn3 = QPushButton(self,objectName='f_btn3')
        self.f_btn4 = QPushButton(self,objectName='f_btn4')
        self.c_btn1_1 = QPushButton(self,objectName='c_btn1_1')
        self.c_btn1_2 = QPushButton(self,objectName='c_btn1_2')
        self.c_btn1_3 = QPushButton(self,objectName='c_btn1_3')
        self.c_btn1_4 = QPushButton(self,objectName='c_btn1_4')
        self.c_btn2_1 = QPushButton(self,objectName='c_btn2_1')
        self.c_btn2_2 = QPushButton(self,objectName='c_btn2_2')
        self.c_btn3_1 = QPushButton(self,objectName='c_btn3_1')
        self.c_btn3_2 = QPushButton(self,objectName='c_btn3_2')
        self.c_btn3_3 = QPushButton(self,objectName='c_btn3_3')
        self.c_btn4_1 = QPushButton(self,objectName='c_btn4_1')
        self.c_btn4_2 = QPushButton(self,objectName='c_btn4_2')
        self.c_wid1 = QWidget(self,objectName='c_wid1')
        self.c_wid2 = QWidget(self,objectName='c_wid2')
        self.c_wid3 = QWidget(self,objectName='c_wid3')
        self.c_wid4 = QWidget(self,objectName='c_wid4')

        self.lb.setPixmap(QPixmap('C:/Users/Lenovo/Desktop/QT/Resource/admin.png'))
        self.f_btn1.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K1.PNG'))
        self.f_btn2.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K2.PNG'))
        self.f_btn3.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K3.PNG'))
        self.f_btn4.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K4.PNG'))
        self.f_btn1.setIconSize(QSize(220,60))
        self.f_btn2.setIconSize(QSize(220,60))
        self.f_btn3.setIconSize(QSize(220,60))
        self.f_btn4.setIconSize(QSize(220,60))
        self.c_btn1_1.setText('新建档案')
        self.c_btn1_2.setText('保    存')
        self.c_btn1_3.setText('打    印')
        self.c_btn1_4.setText('导    出')
        self.c_btn2_1.setText('打    开')
        self.c_btn2_2.setText('新    建')
        self.c_btn3_1.setText('打    开')
        self.c_btn3_2.setText('预    测')
        self.c_btn3_3.setText('保    存')
        self.c_btn4_1.setText('软件设置')
        self.c_btn4_2.setText('参数设置')


        self.f_btn1.clicked.connect(self.hide_ext_1)
        self.f_btn2.clicked.connect(self.hide_ext_2)
        self.f_btn3.clicked.connect(self.hide_ext_3)
        self.f_btn4.clicked.connect(self.hide_ext_4)

        self.lb.setMaximumWidth(220)
        self.lb.setMaximumHeight(220)
        self.f_btn1.setMaximumWidth(220)
        self.f_btn2.setMaximumWidth(220)
        self.f_btn3.setMaximumWidth(220)
        self.f_btn4.setMaximumWidth(220)
        self.c_btn1_1.setMaximumWidth(220)
        self.c_btn1_2.setMaximumWidth(220)
        self.c_btn1_3.setMaximumWidth(220)
        self.c_btn1_4.setMaximumWidth(220)
        self.c_btn2_1.setMaximumWidth(220)
        self.c_btn2_2.setMaximumWidth(220)
        self.c_btn3_1.setMaximumWidth(220)
        self.c_btn3_2.setMaximumWidth(220)
        self.c_btn3_3.setMaximumWidth(220)
        self.c_btn4_1.setMaximumWidth(220)
        self.c_btn4_2.setMaximumWidth(220)
        self.c_wid1.setMaximumWidth(220)
        self.c_wid2.setMaximumWidth(220)
        self.c_wid3.setMaximumWidth(220)
        self.c_wid4.setMaximumWidth(220)


        self.f_lay = QVBoxLayout()
        self.c_lay1 = QVBoxLayout()
        self.c_lay2 = QVBoxLayout()
        self.c_lay3 = QVBoxLayout()
        self.c_lay4 = QVBoxLayout()
        self.setLayout(self.f_lay)
        self.c_wid1.setLayout(self.c_lay1)
        self.c_wid2.setLayout(self.c_lay2)
        self.c_wid3.setLayout(self.c_lay3)
        self.c_wid4.setLayout(self.c_lay4)

        self.f_lay.setSpacing(0)
        self.f_lay.setContentsMargins(0, 0, 0, 0)
        self.c_lay1.setSpacing(0)
        self.c_lay1.setContentsMargins(0, 0, 0, 0)
        self.c_lay2.setSpacing(0)
        self.c_lay2.setContentsMargins(0, 0, 0, 0)
        self.c_lay3.setSpacing(0)
        self.c_lay3.setContentsMargins(0, 0, 0, 0)
        self.c_lay4.setSpacing(0)
        self.c_lay4.setContentsMargins(0, 0, 0, 0)

        self.c_lay1.addWidget(self.c_btn1_1)
        self.c_lay1.addWidget(self.c_btn1_2)
        self.c_lay1.addWidget(self.c_btn1_3)
        self.c_lay1.addWidget(self.c_btn1_4)
        self.c_lay1.addStretch(1)
        self.c_lay2.addWidget(self.c_btn2_1)
        self.c_lay2.addWidget(self.c_btn2_2)
        self.c_lay2.addStretch(1)
        self.c_lay3.addWidget(self.c_btn3_1)
        self.c_lay3.addWidget(self.c_btn3_2)
        self.c_lay3.addWidget(self.c_btn3_3)
        self.c_lay3.addStretch(1)
        self.c_lay4.addWidget(self.c_btn4_1)
        self.c_lay4.addWidget(self.c_btn4_2)
        self.c_lay4.addStretch(1)

        self.f_lay.addWidget(self.lb)
        self.f_lay.addWidget(self.f_btn1)
        self.f_lay.addWidget(self.c_wid1)
        self.f_lay.addWidget(self.f_btn2)
        self.f_lay.addWidget(self.c_wid2)
        self.f_lay.addWidget(self.f_btn3)
        self.f_lay.addWidget(self.c_wid3)
        self.f_lay.addWidget(self.f_btn4)
        self.f_lay.addWidget(self.c_wid4)
        self.f_lay.addStretch(1)

    def hide_ext_1(self):
        if self.c_wid1.isHidden():
            self.c_wid1.show()
            self.f_btn1.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K1.PNG'))
        else:
            self.c_wid1.hide()
            self.f_btn1.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/B1.PNG'))
    
    def hide_ext_2(self):
        if self.c_wid2.isHidden():
            self.c_wid2.show()
            self.f_btn2.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K2.PNG'))
        else:
            self.c_wid2.hide()
            self.f_btn2.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/B2.PNG'))

    def hide_ext_3(self):
        if self.c_wid3.isHidden():
            self.c_wid3.show()
            self.f_btn3.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K3.PNG'))
        else:
            self.c_wid3.hide()
            self.f_btn3.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/B3.PNG'))

    def hide_ext_4(self):
        if self.c_wid4.isHidden():
            self.c_wid4.show()
            self.f_btn4.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/K4.PNG'))
        else:
            self.c_wid4.hide()
            self.f_btn4.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/B4.PNG'))

    def paintEvent(self, evt):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # 反锯齿
        painter.setRenderHint(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
    

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Menu(None)
    win.show()
    sys.exit(app.exec_())
    pass
