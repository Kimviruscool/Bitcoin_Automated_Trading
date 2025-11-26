#pyQt시그널슬롯

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject): #클래스 정의 (Qobject 상속받음)
    signal1 = pyqtSignal() #signal1 사용자 정의 시그널(신호) 생성 #Signal = 신호
    signal2 = pyqtSignal(int, int) #signal2 사용자 정의 시그널 생성 type int 지정

    def run(self): #시그널 발생 메서드 정의
        self.signal1.emit() #시그널 emit(발생)에 연결된 슬롯함수 호출
        self.signal2.emit(1, 2) #시그널 발생에 연결된 슬롯함수 호출 인자값 int type 1, 2만 받음


class MyWindow(QMainWindow): #윈도우 상속받아 클래스정의
    def __init__(self): #초기화 메서드생성
        super().__init__() #부모 메서드의 초기화사용하여 초기화

        mysignal = MySignal() #시그널 = 신호 정의 객체 생성
        mysignal.signal1.connect(self.signal1_emitted) #생성한 객체를 신호호출을 연결 #signal1이 발생하면 (self.메서드/함수 이름) 발생됨
        mysignal.signal2.connect(self.signal2_emitted) #생성한 객체 신호호출에 연결 signal2가 발생하면 슬롯함수2(signal2_emitted)가 발생됨
        mysignal.run()

    @pyqtSlot() #@pyqtSlot(): 이 데코레이터는 해당 메서드 signal1_emitted가 시그널에 의해 호출될 수 있는 슬롯 함수임을 명시
    def signal1_emitted(self): #시그널에 연결된 슬롯 함수 정의
        print('signal1_emitted') #슬롯함수가 호출되면 콘솔에 출력

    @pyqtSlot(int, int) #슬롯함수 명시
    def signal2_emitted(self, arg1, arg2): #시그널2 메소드 생성 초기화 후, inttype의 인자값 arg1과 arg2만 받을 수 있음
        print('signal2_emitted', arg1, arg2) #슬롯함수 정의 #호출될시 콘솔에 출력

#app 실행
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()