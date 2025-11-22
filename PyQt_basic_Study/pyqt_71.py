# 나만의 HTS(Home Training system) 만들기

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

#추가1
from PyQt5.QtChart import QLineSeries, QChart
#추가2 #안티엘리어싱 모듈추가 및 적용
from PyQt5.QtGui import QPainter
#추가3 #PyQt 날짜 모듈 추가
from PyQt5.QtChart import QLineSeries, QChart, QValueAxis, QDateTimeAxis
from PyQt5.QtCore import Qt, QDateTime


class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("MyWindowUI/chart.ui", self)
        self.ticker = ticker
        # 추가1
        self.viewLimit = 128

        self.priceData = QLineSeries()
        # self.priceData.append(0,10)
        # self.priceData.append(1, 20)
        # self.priceData.append(2, 10)
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)

        #추가2
        self.priceChart.legend().hide()

        #추가3
        axisX = QDateTimeAxis()
        axisX.setFormat("hh:mm:ss")
        axisX.setTickCount(4)
        dt = QDateTime.currentDateTime()
        axisX.setRange(dt, dt.addSecs(self.viewLimit))

        axisY = QValueAxis()
        axisY.setVisible(False)

        self.priceChart.addAxis(axisX, Qt.AlignBottom)
        self.priceChart.addAxis(axisY, Qt.AlignRight)
        self.priceData.attachAxis(axisX)
        self.priceData.attachAxis(axisY)
        self.priceChart.layout().setContentsMargins(0,0,0,0)

        #추가2
        self.priceView.setChart(self.priceChart)
        self.priceView.setRenderHints(QPainter.Antialiasing)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())