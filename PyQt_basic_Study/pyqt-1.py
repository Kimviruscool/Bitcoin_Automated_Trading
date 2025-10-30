#PyQt 사용

import sys
from PyQt5.QtWidgets import *
#PyQt5 =  앱 개발시 사용되는 패키지 중 하나
# 사용자 인터페이스기능을 추가해줌

app = QApplication(sys.argv) #pyQt App 생성 () , sys.argv 대신 다른것이 들어가도 상관없음 ex : 프로그램, 프로젝트 이름

# label = QLabel("Hello") #PyQt 실행 후 내용 추가
# label.show() # 앱에 출력

btn = QPushButton("Hello btn") #버튼 객체 생성
btn.show() #앱에 버튼 출력

app.exec_() # App 실행 #이벤트 루프 생성 #(while , for문 없이 자동으로 계속해서 돌아감)

#PyQt5에는 다양한 컴포넌트 존재
# HTML 로 비교
# QGroupBox = div 태그 , 박스 생성
# QLabel = h1~h5 태그 , text 태그
# QTextEdit = input태그 type=text
# QDateEdit = type="date"
# QTimeEdit = type="time"
# QLineEdit = TYPE="text"

