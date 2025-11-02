#pyQt시그널슬롯

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()


class MyWindow(QMainWindow): #다중 상속을 받는다.
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emittedf)
        mysignal.run()

    @pyqtSlot()
    def signal1_emittedf(self):
        print('signal1_emittedf')

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()