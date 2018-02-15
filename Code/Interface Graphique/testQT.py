import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont

import main5


class Example(QWidget):

    def __init__(self):
        super().__init__(main5.Ui_MainWindow)

        self.setupUI()

    '''def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        w = QWidget()
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Simple')
        self.show()'''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
