import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class LAbsolute(QWidget):

    def __init__(self):
        super().__init__()



    def __initUI__(self,parent):

        lbl1 = QLabel('Zetcode', parent)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', parent)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', parent)
        lbl3.move(55, 70)

        parent.setGeometry(300, 300, 250, 150)
        parent.setWindowTitle('Absolute')
        parent.show()

    def __getLayout__(self):
        return self

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LAbsolute()
    sys.exit(app.exec_())