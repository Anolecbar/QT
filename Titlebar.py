import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TitleBar(QWidget):
    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.win = parent
        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setFixedHeight(60)
        self.InitializeViews()
        pass

    def InitializeViews(self):
        self.space = QLabel(self,objectName='space')
        self.iconLabel = QLabel(self,objectName='iconLabel')
        self.titleLabel = QLabel(self,objectName='titleLabel')
        self.minButton = QPushButton(self,objectName='minButton')
        self.restoreButton = QPushButton(self,objectName='restoreButton')
        self.closeButton = QPushButton(self,objectName='closeButton')

        self.minButton.setFixedHeight(60)
        self.restoreButton.setFixedHeight(60)
        self.closeButton.setFixedHeight(60)
        self.iconLabel.setFixedHeight(60)
        self.iconLabel.setMaximumWidth(80)

        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.minButton.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/min.png'))
        self.restoreButton.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/re.png'))
        self.closeButton.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/close.png'))


        self.minButton.clicked.connect(self.ShowMininizedWindow)
        self.restoreButton.clicked.connect(self.ShowRestoreWindow)
        self.closeButton.clicked.connect(self.CloseWindow)

        self.lay = QHBoxLayout(self)
        self.setLayout(self.lay)

        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)

        self.lay.addWidget(self.space)
        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

        self.lay.setStretch(0,2)
        self.lay.setStretch(1,1)
        self.lay.setStretch(2,40)
        self.lay.setStretch(3,2)
        self.lay.setStretch(4,2)
        self.lay.setStretch(5,2)

    def ShowMininizedWindow(self):
        self.win.showMinimized()

    def ShowMaximizedWindow(self):
        self.win.showMaximized()

    def ShowRestoreWindow(self):
        if self.win.isMaximized():
            self.win.showNormal()
            self.restoreButton.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/max.png'))
        else:
            self.win.showMaximized()
            self.restoreButton.setIcon(QIcon('C:/Users/Lenovo/Desktop/QT/Resource/re.png'))

    def CloseWindow(self):
        self.win.close()

    def SetTitle(self, str):
        self.titleLabel.setText(str)

    def SetIcon(self, pix):
        self.iconLabel.setPixmap(pix.scaled(self.iconLabel.size() - QSize(20, 20)))

    def mouseDoubleClickEvent(self, event):
        self.ShowRestoreWindow()
        return QWidget().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPos()
        return QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.isPressed:
            if self.win.isMaximized:
                self.win.showNormal()
            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.win.move(self.win.pos() + movePos)

        return QWidget().mouseMoveEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TitleBar(None)
    win.show()
    sys.exit(app.exec_())

    pass