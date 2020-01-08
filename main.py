import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from task import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        res = random.randint(5, 200)
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(100, 100, res, res)
        qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
