#from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu,QGridLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)

        self.statusBar().showMessage('准备就绪')

        self.setGeometry(100,100,1280,800)
        self.setWindowTitle('关注微信公众号：学点编程吧--上下文菜单')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.png'),'保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'),'另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('new.png'),'新建(&N)',self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')
        newAct.triggered.connect(self.openimage)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.label = QLabel()
        self.label.setScaledContents(True)
        grid.addWidget(self.label,0,0,20,20)




        self.showMaximized()

    def  openimage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', './', 'Images (*.jpg *.gif *.png)')
        self.label.setPixmap(QPixmap(fname))



    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())