#main
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pybithumb import Bithumb

form_class = uic.loadUiType("MyWindowUI/main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #추가1
        self.setWindowTitle("Home Trading System")

        self.ticker = "BTC"
        self.button.clicked.connect(self.clickBtn)

        #추가3
        with open("bithumb.txt") as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            self.apiKey.setText(apikey)
            self.secKey.setText(seckey)

    #추가1
    def clickBtn(self):
        if self.button.text() == "매매시작":
            #추가2
            apiKey = self.apiKey.text()
            secKey = self.secKey.text()
            if len(apiKey) != 32 or len(secKey) != 32:
                self.textEdit.append("KEY가 올바르지 않습니다.")
                return
            else:
                self.b = Bithumb(apiKey,secKey)
                balance = self.b.get_balance(self.ticker)
                if balance == None :
                    self.textEdit.append("KEY가 올바르지 않습니다")
                    return

            self.button.setText("매매중지")
            self.textEdit.append("----- START -----")
            self.textEdit.append(f"보유 현금 : {balance[2]}원")
        else :
            self.textEdit.append("----- END -----")
            self.button.setText("매매시작")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())