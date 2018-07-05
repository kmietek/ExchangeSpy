"""
ZetCode
PyQt5
tutorial

In
this
example, we
position
two
push
buttons in the
bottom - right
corner
of
the
window.

Author: Jan
Bodnar
Website: zetcode.com
Last
edited: August
2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class LBoxLayout(QWidget):

    def __init__(self):
        super().__init__()




    def __initUI__(self, parent):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        parent.setLayout(vbox)

        parent.setGeometry(300, 300, 300, 150)
        parent.setWindowTitle('Buttons')
        parent.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = LBoxLayout()
    sys.exit(app.exec_())