import sys
from datetime import datetime
from threading import Timer,Thread,Event
from time import sleep

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QRadioButton
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QDial
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

from motor import start, stop, right, left, clear
from form_detection import run
from ir_sensor import objectDetected

class MyThread(Thread):
    def __init__(self, event, updateImageSignal, mode):
        Thread.__init__(self)
        self.stopped = False
        self.updateImageSignal = updateImageSignal
        self.mode = mode

    def run(self):
        while not self.stopped:
            if objectDetected():
              print("Object detected")
              sleep(3)
              stop()
              run(self.updateImageSignal, self.mode)
        
    def kill(self):
        self.stopped = True
        

class Window(QWidget, QObject):
    updateImageSignal = pyqtSignal()
    
    def __init__(self):
        QObject.__init__(self)
        self.stopFlag = False
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.updateImageSignal.connect(self.updateImage)

        self.setWindowTitle('Sortare')
        self.setFixedSize(480, 320)

        self.label = QLabel(self)
        pixmap = QPixmap('150.png')
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label, 0, 0, 1, 3)

        self.start_btn = QPushButton(self)
        self.start_btn.setText("Start")
        self.start_btn.clicked.connect(self.start_clicked)
        layout.addWidget(self.start_btn, 1, 0)

        self.stop_btn = QPushButton(self)
        self.stop_btn.setText("Stop")
        self.stop_btn.clicked.connect(self.stop_clicked)
        layout.addWidget(self.stop_btn, 1, 1)

        self.radiobutton = QRadioButton("Forma")
        self.radiobutton.sortingType = 1
        self.radiobutton.setChecked(True)
        self.mode = 1
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
        #self.showFullScreen()

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))

    def start_clicked(self):
        print("Start clicked")
        start()
        self.thread = MyThread(self.stopFlag, self.updateImageSignal, self.mode)
        self.startThread()

    def updateImage(self):
        pixmap = QPixmap('output.jpg')
        self.label.setPixmap(pixmap)

    def stop_clicked(self):
        print("Stop clicked")
        stop()
        self.thread.kill()
    
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.mode = radioButton.sortingType
            print("Sortarea: %s" % (radioButton.sortingType))
            
    def startThread(self):
        self.stopFlag = False
        self.thread.start()


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())