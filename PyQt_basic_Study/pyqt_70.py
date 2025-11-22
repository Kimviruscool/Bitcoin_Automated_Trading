# 나만의 HTS(Home Training system) 만들기

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

#추가1
from PyQt5.QtChart import QLineSeries, QChart

class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("MyWindowUI/chart.ui", self)
        self.ticker = ticker
        # 추가1 #그래프와 점찍기
        self.viewLimit = 128

        self.priceData = QLineSeries()
        self.priceData.append(0,10)
        self.priceData.append(1, 20)
        self.priceData.append(2, 10)

        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)

        self.priceView.setChart(self.priceChart)
        

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())