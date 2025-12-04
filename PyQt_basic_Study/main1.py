#main
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pybithumb import Bithumb
import pybithumb
import datetime
import time
from PyQt5.QtCore import QThread, pyqtSignal
from volatility import *


class VolatilityWorker(QThread):
    tradingSent = pyqtSignal(str,str,str)

    def __init__(self, ticker, bithumb):
        super().__init__()
        self.ticker = ticker
        self.bithumb = bithumb
        self.alive =True

    def run(self): #초기설정
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        ma5 = get_yesterday_ma5(self.ticker)
        wait_flag = False #현재 매수 상태인지 확인하는 플래그
        buy_price = 0 # 매수했을 때의 가격을 저장할 변수 초기화

        #Custom
        target_price = get_target_price(self.ticker)

        while self.alive:
            try:
                now = datetime.datetime.now()
                
                # 자정 초기화 및 매도 로직
                if mid < now < mid + datetime.timedelta(seconds=10):
                    target_price = get_target_price(self.ticker) #목표가 갱신
                    mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 내일 자정 시간 갱신
                    ma5 = get_yesterday_ma5(self.ticker) #5일 이동평균선 갱신

                    #코인 보유 여부 조건 확인
                    if wait_flag == True :
                        current_price = pybithumb.get_current_price(self.ticker)

                        # 자정인데 수익이면 매도
                        if current_price > buy_price:

                            desc = sell_crypto_currency(self.bithumb, self.ticker)
                            result = self.bithumb.get_order_completed(desc)

                            timestamp = result['data']['order_date']
                            dt = datetime.datetime.fromtimestamp(int(int(timestamp) /1000000))
                            tstring = dt.strftime("%Y/%m/%d %H:%M%S")
                            self.tradingSent.emit(tstring, "매도", result['data']['order_qty'])
                            wait_flag = False #매도 완료 후 미보유 상태로 변경
                        #자정인데 손실이면 보류
                        else :
                            tstring = now.strftime("%Y%m%d %H:%M%S")
                            self.tradingSent.emit(tstring, "자정홀딩(손실중)", "보류")
                            #wait_flag = True # 안바뀌니 계속 보유 유지

                #실시간 시세 조회 및 익절/손절 감시
                current_price = pybithumb.get_current_price(self.ticker)
                
                #매수 상태일 때만 수익률 계산 및 감시
                if wait_flag == True :
                    #수익률 = (현재가 - 매수가) / 매수가 * 100
                    if buy_price > 0:
                        yield_rate = ((current_price - buy_price) / buy_price) * 100
                    else :
                        yield_rate = 0
                        
                    #조건1 수익률 5% 도달 시 > 익절 매도
                    if yield_rate >= 5.0:
                        desc = sell_crypto_currency(self.bithumb, self.ticker)
                        result = self.bithumb.get_order_completed(desc)

                        timestamp = result['data']['order_date']
                        dt = datetime.datetime.fromtimestamp(int(int(timestamp) /1000000))
                        tstring = dt.strftime("%Y/%m/%d %H:%M%S")
                        self.tradingSent.emit(tstring, f"익절매도({yield_rate:.2f}%)", result['data']['order_qty'])
                        wait_flag = False
                    
                    #조건2 수익률 -3% 도달 시 > 손절 매도
                    elif yield_rate <= -3.0:
                        desc = sell_crypto_currency(self.bithumb, self.ticker)
                        result = self.bithumb.get_order_completed(desc)

                        timestamp = result['data']['order_date']
                        dt = datetime.datetime.fromtimestamp(int(int(timestamp) /1000000))
                        self.tradingSent.emit(tstring, f"손절매도({yield_rate:.2f}%)", result['data']['order_qty'])
                        wait_flag = False
                        
                #3. 매수 진입 로직 변동성 돌파
                if wait_flag == True :
                    # 현재가가 목표가를 넘고 5일 이동평균선보다 높으면 매수
                    if (current_price > target_price) and (current_price > ma5) :
                        desc = buy_crypto_currency(self.bithumb, self.ticker)
                        result = self.bithumb.get_order_completed(desc)

                        timestamp = result['data']['order_date']
                        dt = datetime.datetime.fromtimestamp(int(int(timestamp) /1000000))
                        tstring = dt.strftime("%Y/%m/%d %H:%M%S")
                        self.tradingSent.emit(tstring, "매수", result['data']['order_qty'])

                        wait_flag = True
                        buy_price = current_price # 매수 체결 가격 저장

            except Exception as e :
                print(f"에러발생 {e}")
                # pass
            time.sleep(1)

    def close(self):
        self.alive = False

form_class = uic.loadUiType("MyWindowUI/main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Home Trading System")

        self.ticker = "XRP"
        self.button.clicked.connect(self.clickBtn)

        with open("C:/Users/0000/Desktop/bithumb.txt") as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            self.apiKey.setText(apikey)
            self.secKey.setText(seckey)

    def clickBtn(self):
        if self.button.text() == "매매시작":
            #추가2
            apiKey = self.apiKey.text()
            secKey = self.secKey.text()
            if len(apiKey) != 32 or len(secKey) != 32:
                self.textEdit.append("KEY가 올바르지 않습니다.")
                return
            else:
                self.bithumb = Bithumb(apiKey,secKey)
                balance = self.bithumb.get_balance(self.ticker)
                if balance == None :
                    self.textEdit.append("KEY가 올바르지 않습니다")
                    return

            self.button.setText("매매중지")
            self.textEdit.append("----- START -----")
            self.textEdit.append(f"보유 현금 : {balance[2]}원")
            #추가4
            self.vw = VolatilityWorker(self.ticker, self.bithumb)
            self.vw.tradingSent.connect(self.receiveTradingSignal)
            self.vw.start()
        else :
            self.textEdit.append("----- END -----")
            self.button.setText("매매시작")

    def receiveTradingSignal(self, time, type, amount):
        self.textEdit.append(f"[{time}] {type} : {amount}")

    def closeEvent(self, event):
        self.vw.close()
        self.widget.closeEvent(event)
        self.widget_2.closeEvent(event)
        self.widget_3.closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())