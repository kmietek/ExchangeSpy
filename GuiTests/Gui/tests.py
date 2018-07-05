import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from GuiTests.Gui.Layouts import LAbsolute, LBoxLayout, LQGridLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()
        layout = LQGridLayout.LQGridLayout()

        layout.__initUI__(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())