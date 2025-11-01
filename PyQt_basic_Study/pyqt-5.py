#pyqt 코빗 시세 조회기 만들기

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("MyWindowUI/M2.ui")[0] #loadUiType() 메서드는 외부에서 만든 UI를 읽어서 파이썬 클래스생성 코드를 생성

class MyWindow(QMainWindow, form_class): #다중 상속을 받는다.
    def __init__(self):
        super().__init__()
        self.setupUi(self) #form_class 클래스에 정의된 메서드로 QtDesigner 에서 만든 클래스를 호출
        self.pushButton.clicked.connect(self.inquiry) #클릭 이벤트 추가 Designer에서 만든 기능연결

    def inquiry(self): #btn_clicked 기능 추가
        # print("inquiry 200") #디버깅
        price = pykorbit.get_current_price("BTC") #price 변수에 pykorbit 패키지를 사용하여 .get_current_price("코인가격")
        # print(price) #가격확인
        self.lineEdit.setText(str(price)) #앱 내부에 존재하는 lineEdit에 현재가 출력

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()