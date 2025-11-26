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
#추가5
import time
import pybithumb
from PyQt5.QtCore import QThread, pyqtSignal

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

        #추가6
        self.pw = PriceWorker(ticker)
        self.pw.dataSent.connect(self.appendData)
        self.pw.start()

    #추가4
    def appendData(self, currPrice):
        if len(self.priceData) == self.viewLimit:
            self.priceData.remove(0)
        dt = QDateTime.currentDateTime()
        self.priceData.append(dt.toMSecsSinceEpoch(), currPrice)
        self.__updateAxis() #실시간으로 추가되는 데이터으 위치를 지정

    def __updateAxis(self):
        pvs = self.priceData.pointsVector()
        dtStart = QDateTime.currentDateTime().fromMSecsSinceEpoch(int(pvs[0].x()))
        if len(self.priceData) == self.viewLimit:
            dtLast = QDateTime.fromMSecsSinceEpoch(int(pvs[-1].x()))
        else:
            dtLast = dtStart.addSecs(self.viewLimit)

        ax = self.priceChart.axisX()
        ax.setRange(dtStart, dtLast)

        ay = self.priceChart.axisY()
        dataY = [v.y() for v in pvs]
        ay.setRange(min(dataY), max(dataY))

    #추가7
    def closeEvent(self, event):
        self.pw.close()

#추가5
class PriceWorker(QThread):
    dataSent = pyqtSignal(float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        while self.alive:
            data = pybithumb.get_current_price(self.ticker)
            time.sleep(1)
            self.dataSent.emit(data)

    def close(self):
        self.alive = False

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())