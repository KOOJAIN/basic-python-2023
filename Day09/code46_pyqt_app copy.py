import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class MyApp(QWidget): #내가 MyApp이란 클래스를 만들건데 부모는 QWidget이야
   
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple window')
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # self.move(1920 // 2 - 200, 900 // 2 - 100)  # 띄우는 위치 조정(정중앙)
        self.resize(400, 200)
        self.show() # 핵심!!  # 파이썬 창이뜬다. 작업관리자에서 관리 활용하시길



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
