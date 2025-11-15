from PyQt5.QtCore import *

class worker(QThread):
    def run(self):
        while True:
            print("Hi")
            self.sleep(1)