"""
ZetCode PyQt5 tutorial

In this example, we create a skeleton
of a calculator using QGridLayout.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class LQGridLayout(QWidget):

    def __init__(self):
        super().__init__()

    def __initUI__(self, parent):

        grid = QGridLayout()
        parent.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        parent.move(300, 150)
        parent.setWindowTitle('Calculator')
        parent.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LQGridLayout()
    sys.exit(app.exec_())
