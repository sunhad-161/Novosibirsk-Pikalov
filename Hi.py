import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber
from random import choice


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = choice(range(10))
        self.y = choice(range(10))
        self.z = choice(range(10))
        self.steps = 10

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Числовая игра')

        self.plus = QPushButton('+' + str(self.y), self)
        self.plus.resize(self.plus.sizeHint())
        self.plus.move(170, 150)
        self.plus.clicked.connect(self.P)

        self.minus = QPushButton('-' + str(self.z), self)
        self.minus.resize(self.minus.sizeHint())
        self.minus.move(20, 150)
        self.minus.clicked.connect(self.M)

        self.label = QLabel(self)
        self.label.setText(str(self.x))
        self.label.move(80, 30)

        self.LCD_count = QLCDNumber(self.x, self)
        self.LCD_count.move(110, 80)

        self.count = 0

    def P(self):
        self.x += self.y
        self.steps -= 1

    def M(self):
        self.x -= self.z
        self.steps -= 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())