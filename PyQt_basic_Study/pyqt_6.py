#pyqt 타이머

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self); #timer 초기화
        self.timer.start(1000); #타이머 시작 1초 간격으로 이벤트발생
        self.timer.timeout.connect(self.timeout); #타이머 종료 1초간격으로  timeout 이벤트발생

    def timeout(self):
        cur_time = QTime.currentTime() #Qtime class의 메서드를 호출하여 현재 시스템 시간을 QTime객체로 가져옴
        str_time = cur_time().toString("hh:mm:ss") #가져온 객체를 .toString() 을 사용하여 문자열로 변환
        self.statusbar.showMessage(str_time) #QMainWindow의 상태 표시줄에 시간을 표시

app = QApplication(sys.argv)
window = Mywindow()
window.show()
app.exec_()