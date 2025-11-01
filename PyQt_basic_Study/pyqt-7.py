#pyqt 코빗 시세 조회기 만들기

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("MyWindowUI/M3.ui")[0] #loadUiType() 메서드는 외부에서 만든 UI를 읽어서 파이썬 클래스생성 코드를 생성

class MyWindow(QMainWindow, form_class): #다중 상속을 받는다.
    def __init__(self):
        super().__init__()
        self.setupUi(self) #form_class 클래스에 정의된 메서드로 QtDesigner 에서 만든 클래스를 호출

        self.timer = QTimer(self) #Qtimer객체 생성하여 현재 클래스를 부모로하여 초기화진행
        self.timer.start(1000) #타이머를 시작하고 1초마다 timeout 이벤트신호를 발생시키도록 설정
        self.timer.timeout.connect(self.inquiry) #타이머의 timeout 이벤트신호를 self.inquiry 메서드에 연결(1초마다 inquiry 메서드 실행)

    def inquiry(self): #시간, 시세 반환해주는 메서드 정의
        # print("inquiry 200") #디버깅

        cur_time = QTime.currentTime() #Qtime클래스의 정적 메서드를 호출하여 현재시간 저장
        str_time = cur_time.toString("hh:mm:ss") #저장된 시간을 .toString()을 사용하여 문자열로 반환
        self.statusBar().showMessage(str_time) #반환된 데이터를 showMessage를 통해 출력

        price = pykorbit.get_current_price("BTC") #price 변수에 pykorbit 패키지를 사용하여 .get_current_price("코인가격")
        self.lineEdit.setText(str(price)) #앱 내부에 존재하는 lineEdit에 현재가 출력

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()