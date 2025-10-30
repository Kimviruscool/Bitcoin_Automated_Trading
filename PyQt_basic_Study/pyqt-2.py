#pyqt 윈도우 생성 , 상속

import sys
from PyQt5.QtWidgets import *

class Mywindow(QMainWindow): #Mywindow class 생성 (PyQt5가 제공하는 클래스를 상속받아 window생성)
    def __init__(self): #def 인자값 초기화하는 기능생성
        super().__init__() #부모로부터 생성된 함수를 호출하기위해 super. 을 사용
        #사용하는 이유 : 부모클래스 와 자식클래스 모두 __init__() 초기화 기능(외부 기능 : 메서드, 내부기능 : 함수)을 모두 사용할 수 있기때문에 super().사용
        #자식클래스에 초기화 함수를 사용하려면 self.__init__() 사용

app = QApplication(sys.argv)
window = Mywindow()
window.show()
app.exec_()