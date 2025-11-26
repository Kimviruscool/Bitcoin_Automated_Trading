#pyqt 커스터마이징

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow): #Mywindow class 생성 (PyQt5가 제공하는 클래스를 상속받아 window생성)
    def __init__(self): #def 인자값 초기화하는 기능생성
        super().__init__() #부모로부터 생성된 함수를 호출하기위해 super. 을 사용
        #사용하는 이유 : 부모클래스 와 자식클래스 모두 __init__() 초기화 기능(외부 기능 : 메서드, 내부기능 : 함수)을 모두 사용할 수 있기때문에 super().사용
        #자식클래스에 초기화 함수를 사용하려면 self.__init__() 사용
        self.setGeometry(100,200,300,400) #setGeometry를 사용하여 윈도우 기준화면1에 (왼쪽여백1,왼쪽여백높이2,윈도우사이즈,윈도우높이) 인터페이스를 생성
        self.setWindowTitle("PyQt5") #setWindowTitle을 사용하여 제목, 타이틀바 변경
        self.setWindowIcon(QIcon("../file/graph.png")) #setWindowIcon(QIcon("아이콘이름.파일속성"))

        btn = QPushButton("버튼1", self) #버튼 생성
        btn.move(10,10) #move 이용해서 윈도우 내 버튼에 여백 x,y좌표 여백 x= 10, y= 10 만큼 추가
        btn.clicked.connect(self.btnClicked) #버튼.클릭시.연결(self.기능) #버튼 클릭시 연결된 기능 사용 이벤트 추가

        btn2 = QPushButton("버튼2", self)
        btn2.move(10,40) #move 이용해서 윈도우 내 버튼에 여백 x,y좌표 여백 x= 10, y= 40 만큼 추가

    def btnClicked(self):
        print("Button clicked")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()