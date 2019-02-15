"""from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.IninUI()
    
    def IninUI(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)

        self.setGeometry(100,100,1280,800)

        self.lb = QLabel()
        grid.addWidget(self.lb,0,0,9,9)

        bn = QPushButton()
        bn.setText('A')
        bn.clicked.connect(self.open)
        grid.addWidget(bn,0,10,1,1)

        bn2 = QPushButton()
        bn2.setText('B')
        grid.addWidget(bn2,1,11,1,1)

        self.showMaximized()
    
    def open(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', './', 'Gif (*.gif )')
        movie = QMovie(fname)
        self.lb.setMovie(movie)
        movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

"""

"""from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys
app = QtWidgets.QApplication (sys.argv)
window = QtWidgets.QWidget ()
window.setWindowTitle ("QToolBox")
window.resize (200, 100)
toolBox = QtWidgets.QToolBox ()
toolBox.addItem (QtWidgets.QPushButton ("Tab Content 6"), "Tab &1")
toolBox.addItem (QtWidgets.QLabel ("Tab Content 2"), "Tab &2")
toolBox.addItem (QtWidgets.QLabel ("Tab Content 3"),QtGui.QIcon('editcut.png'), "Tab &3")
toolBox.setCurrentIndex (0)
vbox = QtWidgets.QVBoxLayout ()
vbox.addWidget (toolBox)
window.setLayout (vbox)
window.show ()
sys.exit (app.exec_ ())"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.IninUI()

    def IninUI(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        wid.setLayout(layout)

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
        self.f_wid = QWidget(self,objectName='f_wid')
        self.c_wid1 = QWidget(self,objectName='c_wid1')
        self.c_wid2 = QWidget(self,objectName='c_wid2')
        self.c_wid3 = QWidget(self,objectName='c_wid3')
        self.c_wid4 = QWidget(self,objectName='c_wid4')





        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
