import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
import random


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(300, 150, 500, 150)
        self.setWindowTitle('круг')

        self.add_button = QPushButton('круг', self)
        self.add_button.resize(50, 50)
        self.add_button.move(50, 0)
        self.add_button.clicked.connect(self.hello)

    def hello(self):
        print(123)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Arifmometr()
    example.show()
    sys.exit(app.exec())
