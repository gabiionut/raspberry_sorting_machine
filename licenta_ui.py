import sys
from datetime import datetime
from threading import Timer,Thread,Event
from time import sleep

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QRadioButton
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QDial
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from motor import start, stop, right, left, clear
from form_detection import run, stopDetection
from ir_sensor import objectDetected

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = False

    def run(self):
        while not self.stopped:
            if objectDetected():
              print("Object detected")
              sleep(3)
              stop()
              run()
        
    def kill(self):
        self.stopped = True
        

class Window(QWidget):
    def __init__(self):
        self.stopFlag = False
        # self.thread = MyThread(self.stopFlag)
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle('Timer')
        self.setFixedSize(480, 320)

        self.label = QLabel(self)
        pixmap = QPixmap('150.png')
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label, 0, 0)

        self.start_btn = QPushButton(self)
        self.start_btn.setText("Start")
        self.start_btn.clicked.connect(self.start_clicked)
        layout.addWidget(self.start_btn, 0, 1)

        self.stop_btn = QPushButton(self)
        self.stop_btn.setText("Stop")
        self.stop_btn.clicked.connect(self.stop_clicked)
        layout.addWidget(self.stop_btn, 0, 2)

        self.dial = QDial()
        self.dial.setMinimum(1)
        self.dial.setMaximum(10)
        self.dial.setValue(2)
        self.dial.valueChanged.connect(self.sliderMoved)
        layout.addWidget(self.dial, 1, 0)

        self.radiobutton = QRadioButton("Forma")
        self.radiobutton.sortingType = 1
        self.radiobutton.setChecked(True)
        self.radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(self.radiobutton, 1, 0)

        self.radiobutton = QRadioButton("Dimensiuni")
        self.radiobutton.sortingType = 2
        self.radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(self.radiobutton, 1, 1)

        self.radiobutton = QRadioButton("Culoare")
        self.radiobutton.sortingType = 3
        self.radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(self.radiobutton, 1, 2)
        #self.showFullScreen()

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))

    def start_clicked(self):
        print("Start clicked")
        start()
        self.thread = MyThread(self.stopFlag)
        self.startThread()

    def updateImage(self):
        pixmap = QPixmap('image.jpg')
        self.label.setPixmap(pixmap)

    def stop_clicked(self):
        print("Stop clicked")
        stop()
        self.thread.kill()
    
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Sortarea: %s" % (radioButton.sortingType))
            
    def startThread(self):
        self.stopFlag = False
        self.thread.start()

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())