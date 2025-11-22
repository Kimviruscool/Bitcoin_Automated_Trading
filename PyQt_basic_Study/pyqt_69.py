# 나만의 HTS(Home Training system) 만들기

# https://github.com/sharebook-kr/book-cryptocurrency

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("MyWindowUI/chart.ui", self)
        self.ticker = ticker

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())