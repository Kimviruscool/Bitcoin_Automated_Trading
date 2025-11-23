#oder_book

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class OrderbookWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__()
        uic.loadUi("MyWindowUI/orderbook.ui", self)
        self.ticker = ticker

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ow = OrderbookWidget()
    ow.show()
    exit(app.exec_())
