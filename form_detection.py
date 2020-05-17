import cv2
import numpy as np
from stack_images import stackImages
from get_contours import getContours
from resize import resize
from picamera import PiCamera
from time import sleep
from motor import start, stop, right, left, clear

camera = PiCamera()
stopped = False

def empty(a):
    pass

def classifyForm(form, mode):
    if mode == 1:
        byForm(form)
    if mode == 2:
        bySize(form)
    if mode == 3:
        byColor(form)
        
def byForm(form):
    if form.corners == 4:
        print("Patrulater")
        sleep(1)
        left()
        sleep(1)
        start()
        sleep(15)
        right()
    if form.corners == 3:
        print("Triunghi")
        sleep(1)
        right()
        sleep(1)
        start()
        sleep(12)
        left()
    if form.corners == 6:
        print("Hexagon")

def bySize(form):
    if (form.area <= 35792):
        print("Small")
        start()
        left()
    if (form.area > 35792):
        print("Big")
        start()
        right()

def byColor(form):
    # TODO: By color
    print("By color")
    

def run(updateImageSignal, mode):
    #left()
    #GPIO.cleanup()
    #camera.crop(0.25, 0.25, 0.5, 0.5)
    #camera.start_preview()
    camera.capture('image.jpg')
    #camera.stop_preview()
    ogImg = cv2.imread('image.jpg')
    colorImg = ogImg.copy()
    img = resize(ogImg, 50)
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = 40
    threshold2 = 40

    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    form = getContours(imgDil, imgContour)
    imgContour = resize(imgContour, 50)
    cv2.imwrite('output.jpg', imgContour)
    updateImageSignal.emit()
    classifyForm(form, mode)

    #imgStack = stackImages(0.8, ([img, imgCanny],
                                 #[imgDil, imgContour]))
    #cv2.imshow("Result", imgStack)
    #cv2.waitKey(0)
    #stop()
    #clear()

