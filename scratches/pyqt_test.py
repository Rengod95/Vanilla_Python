import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('test.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi()

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()