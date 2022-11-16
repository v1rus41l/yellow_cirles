import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow

from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn_draw.clicked.connect(self.paint)
        self.do_paint = False

    # def initUI(self):
    #     self.setGeometry(300, 300, 200, 200)
    #     self.setWindowTitle('Рисование')
    #     self.btn = QPushButton('Рисовать', self)
    #     self.btn.move(70, 150)
    #     self.do_paint = False
    #     self.btn_draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        x = randint(0, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(0, 500), randint(0, 500), x, x)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())