import cv2
import numpy as np
from stack_images import stackImages
from get_contours import getContours
from resize import resize
from picamera import PiCamera
from time import sleep
from motor import start, stop, right, left, clear
from canny import canny

camera = PiCamera()
stopped = False

def empty(a):
    pass

def classifyForm(form, mode, setLabelSignal):
    print(mode)
    if mode == 1:
        byForm(form, setLabelSignal)
    if mode == 2:
        bySize(form, setLabelSignal)
    if mode == 3:
        byColor(form, setLabelSignal)
        
    sleep(4)
        
def byForm(form, setLabelSignal):
    if form.corners == 4:
        print("Patrulater")
        sleep(1)
        left()
        sleep(1)
        start()
        setLabelSignal.emit("Patrulater")

    if form.corners == 3:
        print("Triunghi")
        sleep(1)
        right()
        sleep(1)
        start()
        setLabelSignal.emit("Triunghi")

    if form.corners == 6:
        print("Hexagon")
        setLabelSignal.emit("Hexagon")

def bySize(form, setLabelSignal):
    print(form.area)
    if (form.area <= 10000):
        print("Small")
        sleep(1)
        right()
        sleep(1)
        start()
        setLabelSignal.emit("Small")

    if (form.area > 10000):
        print("Big")
        sleep(1)
        right()
        sleep(1)
        start()
        setLabelSignal.emit("Big")

def byColor(form, setLabelSignal):
    # TODO: By color
    print(form.color)
    h = form.color[0]
    s = form.color[1]
    v = form.color[2]
    
    if (h >50 and h<80 and s>50 and s<90 and v>50 and v<80):
        print("Galben")
        setLabelSignal.emit("Galben")
    if (h >150 and h<180 and s>25 and s<55 and v>50 and v<80):
        print("Verde")
        setLabelSignal.emit("Verde")
    

def run(updateImageSignal, mode, setLabelSignal):
    camera.capture('image.jpg')
    ogImg = cv2.imread('image.jpg')
    colorImg = ogImg.copy()
    img = resize(ogImg, 50)
    imgContour = img.copy()
    
    img = img[20:200, 0:500]
    imgContour = imgContour[20:200, 0:500]
    
    cv2.imwrite('imageCrop.jpg', imgContour)

    form = canny(imgContour)
    print(form.corners)
    imgContour = resize(imgContour, 50)
    cv2.imwrite('output.jpg', imgContour)
    updateImageSignal.emit()
    classifyForm(form, mode, setLabelSignal)

