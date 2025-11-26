#pyqt Qt디자이너

import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("MyWindowUI/M1.ui")[0] #loadUiType() 메서드는 외부에서 만든 UI를 읽어서 파이썬 클래스생성 코드를 생성

class MyWindow(QMainWindow, form_class): #QMainWindow 메서드와 , form class 다중 상속을 받는다.
    def __init__(self):
        super().__init__()
        self.setupUi(self) #form_class 클래스에 정의된 메서드로 QtDesigner 에서 만든 클래스를 호출
        self.pushButton.clicked.connect(self.btn_clicked) #클릭 이벤트 추가 Designer에서 만든 기능연결

    def btn_clicked(self): #btn_clicked 기능 추가
        print("Button clicked") #버튼 클릭시 활성화 출력이벤트

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()