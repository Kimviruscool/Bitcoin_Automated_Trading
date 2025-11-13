# Timer alarm

import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

form_calss = uic.loadUiType("MyWindowUI/bull.ui")[0]

class MyWindow(QMainWindow, form_calss):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)


    def timeout(self):
        print("5sec")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()