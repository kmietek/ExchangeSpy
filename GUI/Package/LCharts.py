from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QScrollArea, QGridLayout, QLabel

from PyQt5.QtGui import QIcon
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class LCharts(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        layout = QGridLayout(parent)
        layout.setContentsMargins(0, 0, 0, 0)
        parent.setLayout(layout)

        scroll = QScrollArea(parent)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll, 0, 0)
        scroll2 = QScrollArea(parent)
        scroll2.setWidgetResizable(True)
        layout.addWidget(scroll2, 0, 1)

        scrollContent = QWidget(scroll)
        scrollLayout = QGridLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)

        scrollContent2 = QWidget(scroll2)
        scrollLayout2 = QGridLayout(scrollContent2)
        scrollContent2.setLayout(scrollLayout2)


        for i in range(0, 4):
            charts = QWidget();
            charts.setMinimumHeight(200)
            charts.setMinimumWidth(300)
            chartsL = QGridLayout();
            charts.setLayout(chartsL)
            chartsL.addWidget(QLabel("BTC"),0, 0,1,1)
            chartsL.addWidget(QPushButton("EDIT"),0,3,1,1)
            chartsL.addWidget(PlotCanvas(charts, width=5, height=5),1,0,1,4)

            scrollLayout.addWidget(charts)
            i = i + 1
            scrollLayout2.addWidget(QPushButton(str(i)))

        scroll.setWidget(scrollContent)
        scroll2.setWidget(scrollContent2)


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=50):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)

        ax.plot(data, 'r-')
        ax.set_title('Charts BTC')
        self.draw()
