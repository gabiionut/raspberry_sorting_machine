import sys
import matplotlib.pyplot as plt
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QRadioButton
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QDial
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle('Timer')
        self.setFixedSize(480, 320)

        self.start_btn = QPushButton(self)
        self.start_btn.setText("Start")
        self.start_btn.clicked.connect(self.start_clicked)
        layout.addWidget(self.start_btn, 0, 0)

        self.stop_btn = QPushButton(self)
        self.stop_btn.setText("Stop")
        self.stop_btn.clicked.connect(self.stop_clicked)
        layout.addWidget(self.stop_btn, 0, 1)

        self.dial = QDial()
        self.dial.setMinimum(1)
        self.dial.setMaximum(10)
        self.dial.setValue(2)
        self.dial.valueChanged.connect(self.sliderMoved)
        layout.addWidget(self.dial, 1, 0)

        self.label = QLabel(self)
        pixmap = QPixmap('150.png')
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label, 1, 1)

        self.radiobutton = QRadioButton("Forma")
        self.radiobutton.sortingType = 1
        self.radiobutton.setChecked(True)
        self.radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(self.radiobutton, 2, 0)

        self.radiobutton = QRadioButton("Dimensiuni")
        self.radiobutton.sortingType = 2
        self.radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(self.radiobutton, 2, 1)

        self.radiobutton = QRadioButton("Culoare")
        self.radiobutton.sortingType = 3
        self.radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(self.radiobutton, 2, 2)

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))

    def start_clicked(self):
        print("Start clicked")
        pixmap = QPixmap('100.png')
        self.label.setPixmap(pixmap)

    def stop_clicked(self):
        print("Stop clicked")
    
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Sortarea: %s" % (radioButton.sortingType))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())